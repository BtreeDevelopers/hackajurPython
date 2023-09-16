from flask import Blueprint, request
import traceback
from modules.generateDocuments import generate_doc

router = Blueprint('document', __name__, url_prefix='/document')

@router.route("/teste", methods=["GET"])
def teste():
    return {"message": "hello world!!"}

@router.route("/gear-confissao-de-divida", methods=["POST"])
def change_password_router():
    try:
        data = request.json
        bucket_link = generate_doc(data)
        return {'error': 'false', 'message': 'Arquivo salvo com sucesso', "url": bucket_link, 'status': 200}
    except Exception as e:
        err_msg = f'It was not possible to send the email. Cause: {traceback.format_exc()}'
        print(err_msg)
        raise e