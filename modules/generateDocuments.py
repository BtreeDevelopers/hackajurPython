from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image
from reportlab.lib.styles import getSampleStyleSheet
from datetime import datetime
from num2words import num2words
import locale
import base64
from utils.utils import cep_with_mask, cpf_with_mask, cnpj_with_mask
from io import BytesIO
from templates.debtConfessionTemplate import return_debt_confession_document
from google.cloud import storage
import requests
import traceback
from PIL import Image as pilImage
from models.documentModel import Documento

meses = [
    "Janeiro", "Fevereiro", "Março", "Abril",
    "Maio", "Junho", "Julho", "Agosto",
    "Setembro", "Outubro", "Novembro", "Dezembro"
]

url_list = []

def generate_proposal_1(documento):
    try:
        pdf_file = f"proposta1_{documento.nome}_{documento.data_assinatura_contrato}.pdf"
        pdf_file = pdf_file.replace(" ", "")
        doc = SimpleDocTemplate(pdf_file, pagesize=letter)
        styles = getSampleStyleSheet()
        story = []

        document = return_debt_confession_document(documento.nome, documento.nacionalidade, documento.endereco, documento.estado_civil, documento.cpf, documento.numero_formatado,
                                                   documento.por_extenso, documento.data_assinatura_formatada)

        for paragraph in document.split('\n'):
            p = Paragraph(paragraph.replace('<b>', '<font name="Helvetica-Bold">').replace('</b>', '</font>'),
                          styles['Normal'])
            story.append(p)
            story.append(Spacer(1, 6))

        imagem = Image(documento.imagem_io, width=150, height=100)
        imagem.hAlign = 'LEFT'

        story.append(imagem)

        doc.build(story)

        save_doc_bucket(pdf_file)
    except Exception as e:
        err_msg = f'It was not possible to send the email. Cause: {traceback.format_exc()}'
        print(err_msg)
        raise e

def generate_proposal_2(documento):
    try:
        doc = SimpleDocTemplate(documento.pdf_file, pagesize=letter)
        styles = getSampleStyleSheet()
        story = []

        document = return_debt_confession_document(documento.nome, documento.nacionalidade, documento.endereco, documento.estado_civil, documento.cpf, documento.numero_formatado,
                                                   documento.por_extenso, documento.data_assinatura_formatada)

        for paragraph in document.split('\n'):
            p = Paragraph(paragraph.replace('<b>', '<font name="Helvetica-Bold">').replace('</b>', '</font>'),
                          styles['Normal'])
            story.append(p)
            story.append(Spacer(1, 6))

        imagem = Image(documento.imagem_io, width=150, height=100)
        imagem.hAlign = 'LEFT'

        story.append(imagem)

        doc.build(story)
    except Exception as e:
        err_msg = f'It was not possible to send the email. Cause: {traceback.format_exc()}'
        print(err_msg)
        raise e

def generate_proposal_3(documento):
    try:
        doc = SimpleDocTemplate(documento.pdf_file, pagesize=letter)
        styles = getSampleStyleSheet()
        story = []

        document = return_debt_confession_document(documento.nome, documento.nacionalidade, documento.endereco, documento.estado_civil, documento.cpf, documento.numero_formatado,
                                                   documento.por_extenso, documento.data_assinatura_formatada)

        for paragraph in document.split('\n'):
            p = Paragraph(paragraph.replace('<b>', '<font name="Helvetica-Bold">').replace('</b>', '</font>'),
                          styles['Normal'])
            story.append(p)
            story.append(Spacer(1, 6))

        imagem = Image(documento.imagem_io, width=150, height=100)
        imagem.hAlign = 'LEFT'

        story.append(imagem)

        doc.build(story)
    except Exception as e:
        err_msg = f'It was not possible to send the email. Cause: {traceback.format_exc()}'
        print(err_msg)
        raise e

def generate_proposal_4(documento):
    try:
        doc = SimpleDocTemplate(documento.pdf_file, pagesize=letter)
        styles = getSampleStyleSheet()
        story = []

        document = return_debt_confession_document(documento.nome, documento.nacionalidade, documento.endereco, documento.estado_civil, documento.cpf, documento.numero_formatado,
                                                   documento.por_extenso, documento.data_assinatura_formatada)

        for paragraph in document.split('\n'):
            p = Paragraph(paragraph.replace('<b>', '<font name="Helvetica-Bold">').replace('</b>', '</font>'),
                          styles['Normal'])
            story.append(p)
            story.append(Spacer(1, 6))

        imagem = Image(documento.imagem_io, width=150, height=100)
        imagem.hAlign = 'LEFT'

        story.append(imagem)

        doc.build(story)
    except Exception as e:
        err_msg = f'It was not possible to send the email. Cause: {traceback.format_exc()}'
        print(err_msg)
        raise e

def generate_proposal_5(documento):
    try:
        doc = SimpleDocTemplate(documento.pdf_file, pagesize=letter)
        styles = getSampleStyleSheet()
        story = []

        document = return_debt_confession_document(documento.nome, documento.nacionalidade, documento.endereco, documento.estado_civil, documento.cpf, documento.numero_formatado,
                                                   documento.por_extenso, documento.data_assinatura_formatada)

        for paragraph in document.split('\n'):
            p = Paragraph(paragraph.replace('<b>', '<font name="Helvetica-Bold">').replace('</b>', '</font>'),
                          styles['Normal'])
            story.append(p)
            story.append(Spacer(1, 6))

        imagem = Image(documento.imagem_io, width=150, height=100)
        imagem.hAlign = 'LEFT'

        story.append(imagem)

        doc.build(story)
    except Exception as e:
        err_msg = f'It was not possible to send the email. Cause: {traceback.format_exc()}'
        print(err_msg)
        raise e

def generate_proposal_6(documento):
    try:
        doc = SimpleDocTemplate(documento.pdf_file, pagesize=letter)
        styles = getSampleStyleSheet()
        story = []

        document = return_debt_confession_document(documento.nome, documento.nacionalidade, documento.endereco, documento.estado_civil, documento.cpf, documento.numero_formatado,
                                                   documento.por_extenso, documento.data_assinatura_formatada)

        for paragraph in document.split('\n'):
            p = Paragraph(paragraph.replace('<b>', '<font name="Helvetica-Bold">').replace('</b>', '</font>'),
                          styles['Normal'])
            story.append(p)
            story.append(Spacer(1, 6))

        imagem = Image(documento.imagem_io, width=150, height=100)
        imagem.hAlign = 'LEFT'

        story.append(imagem)

        doc.build(story)
    except Exception as e:
        err_msg = f'It was not possible to send the email. Cause: {traceback.format_exc()}'
        print(err_msg)
        raise e

def generate_proposal_7(documento):
    try:
        doc = SimpleDocTemplate(documento.pdf_file, pagesize=letter)
        styles = getSampleStyleSheet()
        story = []

        document = return_debt_confession_document(documento.nome, documento.nacionalidade, documento.endereco, documento.estado_civil, documento.cpf, documento.numero_formatado,
                                                   documento.por_extenso, documento.data_assinatura_formatada)

        for paragraph in document.split('\n'):
            p = Paragraph(paragraph.replace('<b>', '<font name="Helvetica-Bold">').replace('</b>', '</font>'),
                          styles['Normal'])
            story.append(p)
            story.append(Spacer(1, 6))

        imagem = Image(documento.imagem_io, width=150, height=100)
        imagem.hAlign = 'LEFT'

        story.append(imagem)

        doc.build(story)
    except Exception as e:
        err_msg = f'It was not possible to send the email. Cause: {traceback.format_exc()}'
        print(err_msg)
        raise e

def generate_proposal_8(documento):
    try:
        doc = SimpleDocTemplate(documento.pdf_file, pagesize=letter)
        styles = getSampleStyleSheet()
        story = []

        document = return_debt_confession_document(documento.nome, documento.nacionalidade, documento.endereco, documento.estado_civil, documento.cpf, documento.numero_formatado,
                                                   documento.por_extenso, documento.data_assinatura_formatada)

        for paragraph in document.split('\n'):
            p = Paragraph(paragraph.replace('<b>', '<font name="Helvetica-Bold">').replace('</b>', '</font>'),
                          styles['Normal'])
            story.append(p)
            story.append(Spacer(1, 6))

        imagem = Image(documento.imagem_io, width=150, height=100)
        imagem.hAlign = 'LEFT'

        story.append(imagem)

        doc.build(story)
    except Exception as e:
        err_msg = f'It was not possible to send the email. Cause: {traceback.format_exc()}'
        print(err_msg)
        raise e

def save_doc_bucket(pdf_file):
    try:
        client = storage.Client.from_service_account_json('./firebase/firebase-key.json')
        bucket_name = 'hackajuralgar.appspot.com'
        pdf_file_path = pdf_file
        bucket = client.get_bucket(bucket_name)
        blob = bucket.blob(pdf_file_path)
        blob.upload_from_filename('./'+pdf_file)
        blob.make_public()
        url_list.append(blob.public_url)
    except Exception as e:
        err_msg = f'It was not possible to generate porposal 1. Cause: {traceback.format_exc()}'
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

    documento = Documento(nome, nacionalidade, endereco, estado_civil, cpf_with_mask(cpf), numero_formatado, por_extenso,
                          data_assinatura_formatada, data_assinatura_contrato, imagem_io)

    generate_proposal_1(documento)

    return url_list