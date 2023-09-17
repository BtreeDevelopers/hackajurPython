from flask import Blueprint, request
import traceback
from modules.send_message import debt_notice, automatic_login, download_doc, pendencia_contrato

router = Blueprint('send_email', __name__, url_prefix='/enviar-email')

@router.route("/teste", methods=["GET"])
def teste():
    return {"message": "hello world!!"}

@router.route("/anuncio-de-divida", methods=["POST"])
def anuncio_de_divida():
    try:
        data = request.json
        nome = data["nome"]
        email = data["email"]
        valor_divida = data["valor_divida"]
        nome_divida = data["nome_divida"]
        debt_notice(nome, email, valor_divida, nome_divida)
        return {'error': 'false', 'message': 'E-mail enviado com sucesso', 'status': 200}
    except Exception as e:
        err_msg = f'It was not possible to send the email. Cause: {traceback.format_exc()}'
        print(err_msg)
        raise e

@router.route("/login-automatico", methods=["POST"])
def login_automatico():
    try:
        data = request.json
        nome = data["nome"]
        email = data["email"]
        link = data["link"]
        automatic_login(nome, email, link)
        return {'error': 'false', 'message': 'E-mail enviado com sucesso', 'status': 200}
    except Exception as e:
        err_msg = f'It was not possible to send the email. Cause: {traceback.format_exc()}'
        print(err_msg)
        raise e

@router.route("/download-documento", methods=["POST"])
def download_documento():
    try:
        data = request.json
        nome = data["nome"]
        email = data["email"]
        link = data["link"]
        download_doc(nome, email, link)
        return {'error': 'false', 'message': 'E-mail enviado com sucesso', 'status': 200}
    except Exception as e:
        err_msg = f'It was not possible to send the email. Cause: {traceback.format_exc()}'
        print(err_msg)
        raise e

@router.route("/pendencia_contrato", methods=["POST"])
def pendencia_contrato_enviar():
    try:
        data = request.json
        nome = data["nome"]
        email = data["email"]
        link = data["link"]
        pendencia_contrato(nome, email, link)
        return {'error': 'false', 'message': 'E-mail enviado com sucesso', 'status': 200}
    except Exception as e:
        err_msg = f'It was not possible to send the email. Cause: {traceback.format_exc()}'
        print(err_msg)
        raise e