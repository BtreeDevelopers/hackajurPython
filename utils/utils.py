import locale
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

def cpf_with_mask(cpf):
    cpf_regex = re.compile(r'(\d{3})(\d{3})(\d{3})(\d{2})')
    return cpf_regex.sub(r'\1.\2.\3-\4', cpf)

def cnpj_with_mask(cnpj):
    cnpj_regex = re.compile(r'(\d{2})(\d{3})(\d{3})(\d{4})(\d{2})')
    return cnpj_regex.sub(r'\1.\2.\3/\4-\5', cnpj)

def formatted_number_value(valor):
    locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')
    return locale.currency(valor, grouping=True)