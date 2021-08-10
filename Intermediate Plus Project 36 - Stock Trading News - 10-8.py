import requests as rq
import datetime as dt
import os
import json
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

WEEKDAYS = [2, 3, 4, 5]
SYMBOLS = ['AAPL', 'TSLA', 'GOOG']
NUMBER_STOCKS = len(SYMBOLS)
SYMBOLS_KEYS = {
    'AAPL': 'Apple',
    "TSLA": 'Tesla',
    'GOOG': 'Google'
}

email_address = 'email'
password = 'password'
to = "email"

yesterday = dt.date.today() - dt.timedelta(days=1)
str_date = str(yesterday)
dict_results = {
    str_date: {}

}
previous_day = None


# If the date is a Monday, retrieving the data for the day before will cause an error. This checks and makes
# sure that if the day is Monday, it calls the data from Friday
if dt.date.today().weekday() in WEEKDAYS:
    previous_day = str(dt.date.today() - dt.timedelta(days=2))
    print(dt.date.today())
elif dt.date.today().weekday() == 1:
    previous_day = str(dt.date.today() - dt.timedelta(days=4))


# Market data API
marketstack_api_access_key = os.environ.get('marketstack_api_key')
api = "http://api.marketstack.com/v1/eod"
parameters = {
    'access_key': marketstack_api_access_key,
    'symbols': 'AAPL,TSLA,GOOG',
    'date_from': yesterday
}


# API request
get = rq.get(api, params=parameters)
get.raise_for_status()
data = get.json()


# Adding new data to JSON log
for i in range(NUMBER_STOCKS):
    tkr = data['data'][i]['symbol']
    tkr_close = data['data'][i]['close']
    dict_results[str_date][tkr] = tkr_close


def percentage(current, initial):
    """Percentage Difference Calculator, inputs are current data vs old data"""
    result = 100 * ((current - initial)/initial)
    return result


# Attempts to retrieve data from json log. Saves new data back to the log.
log_tickers_meet_criteria = []
try:
    with open("stock_log.json", 'r') as file:
        old_data = json.load(file)
        old_data.update(dict_results)
        for ticker in SYMBOLS:
            try:
                comp1 = old_data[str_date][ticker]
                comp2 = old_data[previous_day][ticker]
                res = percentage(comp1, comp2)
                if res <= -5 or res >= 5:
                    log_tickers_meet_criteria.append([ticker, res])

            except KeyError:
                print('No value to compare with')


except FileNotFoundError:
    with open('stock_log.json', 'w') as file:
        json.dump(dict_results, file)

with open('stock_log.json', 'w') as file:
    json.dump(old_data, file, indent=4)


# News API request
articles = []
if len(log_tickers_meet_criteria) > 0:
    for i in range(len(log_tickers_meet_criteria)):
        news_api = os.environ.get('news_api_key')
        news_api_endpoint = 'https://newsapi.org/v2/everything'
        news_parameters = {
            'q': SYMBOLS_KEYS[log_tickers_meet_criteria[i][0]],  # changes the aapl symbol to Apple for example
            'from': str_date,
            'sortBy': 'popularity',
            'apiKey': news_api
        }
        news_data = rq.get(news_api_endpoint, params=news_parameters)
        dt = news_data.json()
        try:
            article1_title = dt['articles'][0]['title']
            article1_desc = dt['articles'][0]['description']
            articles.append([article1_title, article1_desc])
            article2_title = dt['articles'][1]['title']
            article2_desc = dt['articles'][1]['description']
            articles.append([article2_title, article2_desc])
        except:
            pass
        print(dt)


# Auto Email Sender
if len(log_tickers_meet_criteria) > 0:
    with smtplib.SMTP(host="smtp-mail.outlook.com", port=587) as connection:
        # Secures connection to email server
        connection.starttls()

        connection.login(user=email_address, password=password)
        msg = MIMEMultipart('alternative')
        msg['Subject'] = f"Stock News"
        msg['From'] = email_address
        msg['To'] = to
        message = ""
        for result in log_tickers_meet_criteria:
            if result[1] > 0:
                x = 'An increase of '
            else:
                x = 'A decrease of '
            message = message + f"Stock: {result[0]} - Price: {x}{result[1]:.2f} percent<br><br>"

        for item in articles:
            message = message + f'<b>Subject</b>: {item[0]}<br><br><b>Content</b>: {item[1]}<br><br>'

        html = f'<html><body><p>{message}</p></body></html>'
        part2 = MIMEText(html, 'html')
        msg.attach(part2)
        connection.send_message(from_addr=email_address, to_addrs=to, msg=msg)
