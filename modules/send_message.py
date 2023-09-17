from templates.debtNoticeTemplate import return_debt_notice_template
from templates.automaticLoginTemplate import return_automatic_login_template
from templates.downloadDocTemplate import return_download_doc_template
from templates.pendenciaAssinaturatemplate import return_pendencia_assinatura
from utils.utils import send_email, formatted_number_value
import traceback

def debt_notice(nome, email, valor_divida, nome_divida):
    try:
        payload = return_debt_notice_template(nome, formatted_number_value(float(valor_divida)), nome_divida)
        subject = "Notificação de Dívida Ativa - Oportunidade de Negociação"
        send_email(payload, email, subject)
    except Exception as e:
        err_msg = f'It was not possible to send the email. Cause: {traceback.format_exc()}'
        print(err_msg)
        raise e

def automatic_login(nome, email, link):
    try:
        payload = return_automatic_login_template(nome, link)
        subject = "Acesso Rápido ao Nosso Sistema - Negocie Sua Dívida"
        send_email(payload, email, subject)
    except Exception as e:
        err_msg = f'It was not possible to send the email. Cause: {traceback.format_exc()}'
        print(err_msg)
        raise e

def download_doc(nome, email, link):
    try:
        payload = return_download_doc_template(nome, link)
        subject = "Seu Contrato Assinado - Download Disponível!"
        send_email(payload, email, subject)
    except Exception as e:
        err_msg = f'It was not possible to send the email. Cause: {traceback.format_exc()}'
        print(err_msg)
        raise e

def pendencia_contrato(nome, email, link):
    try:
        payload = return_pendencia_assinatura(nome, link)
        subject = "Pendência de Assinatura no Contrato"
        send_email(payload, email, subject)
    except Exception as e:
        err_msg = f'It was not possible to send the email. Cause: {traceback.format_exc()}'
        print(err_msg)
        raise e
