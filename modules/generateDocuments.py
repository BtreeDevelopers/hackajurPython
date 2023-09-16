from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image
from reportlab.lib.styles import getSampleStyleSheet
from datetime import datetime
from num2words import num2words
import locale
import base64
from utils.utils import cep_with_mask
from io import BytesIO
from templates.debtConfessionTemplate import return_debt_confession_document
from google.cloud import storage
import requests
import traceback
from PIL import Image as pilImage

meses = [
    "Janeiro", "Fevereiro", "Março", "Abril",
    "Maio", "Junho", "Julho", "Agosto",
    "Setembro", "Outubro", "Novembro", "Dezembro"
]

def save_doc_bucket(pdf_file):
    try:
        client = storage.Client.from_service_account_json('./firebase/firebase-key.json')
        bucket_name = 'hackajuralgar.appspot.com'
        pdf_file_path = pdf_file
        bucket = client.get_bucket(bucket_name)
        blob = bucket.blob(pdf_file_path)
        blob.upload_from_filename('./'+pdf_file)
        blob.make_public()
        return blob.public_url
    except Exception as e:
        err_msg = f'It was not possible to send the email. Cause: {traceback.format_exc()}'
        print(err_msg)
        raise e

def get_Image_from_bucket(url_assinatura):
    try:
        response = requests.get(url_assinatura)
        if response.status_code == 200:
            image = BytesIO(response.content)

            return image
        else:
            print(f"Erro ao baixar a imagem. Código de status: {response.status_code}")
    except Exception as e:
        err_msg = f'It was not possible to send the email. Cause: {traceback.format_exc()}'
        print(err_msg)
        raise e

def return_complete_address(endereco, numero_endereco, bairro, cidade, uf, cep):
    cep = cep_with_mask(cep)
    address = f"""{endereco}, {numero_endereco} - {bairro}, {cidade} - {uf}, {cep}"""
    return address

def numero_por_extenso(numero):
    return num2words(numero, lang='pt_BR')

def generate_doc(data):
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
    vencimento_divida = data["vencimento_divida"]
    url_bucket = data["url_bucket"]
    locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')
    numero_formatado = locale.currency(valor, grouping=True)
    por_extenso = numero_por_extenso(valor)
    endereco = return_complete_address(endereco, numero_endereco, bairro, cidade, uf, cep)

    data_assinatura_contrato = datetime.now()
    data_assinatura_formatada = f"{data_assinatura_contrato.day} de {meses[data_assinatura_contrato.month - 1]} de {data_assinatura_contrato.year}"

    imagem_io = get_Image_from_bucket(url_bucket)

    pdf_file = f"""confissão_de_divida_{nome}_{data_assinatura_contrato}.pdf"""
    doc = SimpleDocTemplate(pdf_file, pagesize=letter)
    styles = getSampleStyleSheet()
    story = []

    document = return_debt_confession_document(nome, nacionalidade, endereco, estado_civil, cpf, numero_formatado, por_extenso, data_assinatura_formatada)

    for paragraph in document.split('\n'):
        p = Paragraph(paragraph.replace('<b>', '<font name="Helvetica-Bold">').replace('</b>', '</font>'),
                      styles['Normal'])
        story.append(p)
        story.append(Spacer(1, 6))

    imagem = Image(imagem_io, width=150, height=100)
    imagem.hAlign = 'LEFT'

    story.append(imagem)

    doc.build(story)

    url = save_doc_bucket(pdf_file)

    return url