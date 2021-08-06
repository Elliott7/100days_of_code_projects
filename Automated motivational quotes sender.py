from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
import datetime as dt
import random

email_address = ''
password = ''
send_address = ''

now = dt.datetime.now()
if now.weekday() == 4:
    with open('quotes.txt', 'r') as quotes_file:
        text = quotes_file.read().split('\n')
        choice = random.choice(text)

        msg = MIMEMultipart('alternative')
        msg['Subject'] = "Your Motivational Quote For The Day"
        msg['From'] = email_address
        msg['To'] = send_address
        html = f'<html><body><p>{choice}</p></body></html>'
        part2 = MIMEText(html, 'html')
        msg.attach(part2)

    with smtplib.SMTP(host="smtp-mail.outlook.com", port=587) as auto_email:

        auto_email.starttls()
        auto_email.login(user=email_address, password=password)
        auto_email.send_message(from_addr=email_address, to_addrs=send_address, msg=msg)
