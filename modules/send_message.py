from templates.debtNoticeTemplate import return_debt_notice_template
from utils.utils import send_email

def debt_notice(username, useremail):
    try:
        payload = return_debt_notice_template(username)
        subject = "Quite sua divida conosco"
        send_email(payload, useremail, subject)
    except Exception as e:
        err_msg = f'It was not possible to send the email. Cause: {traceback.format_exc()}'
        print(err_msg)
        raise e
