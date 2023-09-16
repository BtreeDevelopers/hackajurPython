from flask import Blueprint, request
import traceback
from modules.send_message import debt_notice

router = Blueprint('send_email', __name__, url_prefix='/send_email')

@router.route("/teste", methods=["GET"])
def teste():
    return {"message": "hello world!!"}

@router.route("/debt-notice", methods=["POST"])
def change_password_router():
    try:
        data = request.json
        nome = data["nome"]
        email = data["email"]
        # link = data["link"]
        debt_notice(nome, email)
        return {'error': 'false', 'message': 'E-mail enviado com sucesso', 'status': 200}
    except Exception as e:
        err_msg = f'It was not possible to send the email. Cause: {traceback.format_exc()}'
        print(err_msg)
        raise e