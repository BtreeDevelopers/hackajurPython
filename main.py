from flask import Flask
from flask_cors import CORS
from services.generateDocumentsService import router as generateDocumentsRouter
from dotenv import load_dotenv
import os

load_dotenv()
app = Flask(__name__)
CORS(app)

app.register_blueprint(generateDocumentsRouter)

app.run(port=os.getenv('PORT'))