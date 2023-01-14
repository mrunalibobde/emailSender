# go over to our gmail account and setup 2 factor authentication
# generate app password
# create a function to send the mail
# rvvfpolboovagzrb

from email.message import EmailMessage
from passy import password
import ssl
import smtplib

email_sender = "Enter sender's gmail"
email_password = password

email_receiver ="Enter receiver's gmail"

subject = "Greetings"
body="""
Hello, Good Morning!!
"""

em = EmailMessage()
em['From']=email_sender
em['To']=email_receiver
em['Subject']=subject
em.set_content(body)

context=ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com',465,context=context) as smtp:
    smtp.login(email_sender,email_password)
    smtp.sendmail(email_sender,email_receiver,em.as_string())


