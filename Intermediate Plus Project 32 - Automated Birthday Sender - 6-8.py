"""
Project Thirty-Two - Automated Birthday Email Sender
Interesting project around the automation of emails using SMTPlib
"""

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import random
import datetime as dt


email_address = 'email_address'
password = 'password'
birthdays = []

today = dt.datetime.now()

letters = ["letter_templates/letter_1.txt", 'letter_templates/letter_2.txt', 'letter_templates/letter_3.txt']
letter_choice = random.choice(letters)

with open('birthdays.txt', 'r') as birthdays_file:
    details = birthdays_file.read().split('\n')
    for person in details:
        person = person.split(',')
        if today.day == int(person[2]) and today.month == int(person[3]):
            to_send = True
            recipients_name = person[0]
            recipients_email = person[1]
            birthdays.append([recipients_name, recipients_email])


if to_send:
    for bday_person in birthdays:
        with open(letter_choice, 'r') as file:
            message = file.read()
            message = f'{message.replace("[NAME]", bday_person[0])}'

        msg = MIMEMultipart('alternative')
        msg['Subject'] = "Happy Birthday"
        msg['From'] = email_address
        msg['To'] = bday_person[1]

        html = f'<html><body><p>{message}</p></body></html>'
        part2 = MIMEText(html, 'html')
        msg.attach(part2)

        with smtplib.SMTP(host="smtp-mail.outlook.com", port=587) as connection:

            # Secures connection to email server
            connection.starttls()

            connection.login(user=email_address, password=password)
            connection.send_message(from_addr=email_address, to_addrs=bday_person[1], msg=msg)
            # connection.sendmail(from_addr=email_address, to_addrs=send_address, msg='Hello')
#