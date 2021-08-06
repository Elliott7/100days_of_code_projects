"""
Simple script outlining how to automate emails being sent out
"""

import smtplib

email_address = 'email@hotmail.com'
password = 'password'
send_address = ''

with smtplib.SMTP(host="smtp-mail.outlook.com", port=587) as connection:

    # Secures connection to email server
    connection.starttls()

    connection.login(user=email_address, password=password)

    connection.sendmail(from_addr=email_address, to_addrs=send_address, msg='Hello')
    # connection.send_message(from_addr=email_address, to_addrs=send_address, msg=msg)
