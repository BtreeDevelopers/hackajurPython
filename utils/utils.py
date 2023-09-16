import re
import smtplib
import email.message
import os

def send_email(payload, useremail, subject):

    msg = email.message.Message()
    msg['Subject'] = subject
    msg['From'] = os.getenv('EMAIL')
    msg['To'] = useremail
    password = os.getenv('EMAIL_PASSWORD')
    msg.add_header('Content-Type', 'text/html')
    msg.set_payload(payload)

    s = smtplib.SMTP('smtp.gmail.com: 587')
    s.starttls()
    # Login Credentials for sending the mail
    s.login(msg['From'], password)
    s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))

def cep_with_mask(cep):
    masked_cep = re.sub(r'^(\d{5})-?(\d{3})$', r'\1-\2', cep)
    return masked_cep