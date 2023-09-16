from flask import Flask
from flask_cors import CORS
# from services.send_mail import router as sendMailRouter
from dotenv import load_dotenv
import os

load_dotenv()
app = Flask(__name__)
CORS(app)

# app.register_blueprint(sendMailRouter)

app.run(port=os.getenv('PORT'))