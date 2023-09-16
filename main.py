from flask import Flask
from flask_cors import CORS
from services.generateDocumentsService import router as generateDocumentsRouter
from services.snedEmail import router as sendEmailRouter
from dotenv import load_dotenv
import os

load_dotenv()
app = Flask(__name__)
CORS(app)

app.register_blueprint(generateDocumentsRouter)
app.register_blueprint(sendEmailRouter)

app.run(port=os.getenv('PORT'))