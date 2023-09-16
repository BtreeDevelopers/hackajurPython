from flask import Blueprint, request
import traceback

router = Blueprint('document', __name__, url_prefix='/document')

@router.route("/teste", methods=["GET"])
def teste():
    return {"message": "hello world!!"}

@router.route("/generate", methods=["POST"])
def change_password_router():
    try:
        data = request.json
        nome = data["nome"]
        nacionalidade = data["nacionalidade"]
        estado_civil = data["estado_civil"]
        cpf = data["cpf"]
        endereco = data["endereco"]
        numero_endereco = data["numero_endereco"]
        bairro = data["bairro"]
        cidade = data["cidade"]
        uf = data["uf"]
        cep = data["cep"]
        valor = data["valor"]
        vencumento_divida = data["vencimento_divida"]
        url_bucket = data["url_bucket"]
        # change_password_email(username, useremail, link)
        return {'error': 'false', 'message': 'E-mail enviado com sucesso', 'status': 200}
    except Exception as e:
        err_msg = f'It was not possible to send the email. Cause: {traceback.format_exc()}'
        print(err_msg)
        raise e

@router.route("/welcome_email", methods=["POST"])
def welcome_router():
    try:
        data = request.json
        username = data["userName"]
        useremail = data["userEmail"]
        welcome_email(username, useremail)
        return {'error': 'false', 'message': 'E-mail enviado com sucesso', 'status': 200}
    except Exception as e:
        err_msg = f'It was not possible to send the email. Cause: {traceback.format_exc()}'
        print(err_msg)
        raise e