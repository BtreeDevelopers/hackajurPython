from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image
from reportlab.lib.styles import getSampleStyleSheet
from datetime import datetime
from num2words import num2words
import locale
import base64

from templates.propostaCartaoDeCreditoTemplate import return_propsta_cartao_credito_template
from utils.utils import cep_with_mask, cpf_with_mask, cnpj_with_mask, calcula_valor_descontado, calculate_valor_parcela, gerar_chave_pix_aleatoria
from io import BytesIO
from templates.debtConfessionTemplate import return_debt_confession_document
from templates.propostaFiadorTemplate import return_proposta_fiador_template
from templates.propostaParcelaSemGarantiaTemplate import return_parcelamento_sem_garantia
from templates.propostaPixTemplate import return_pix_template
from google.cloud import storage
import requests
import traceback
from PIL import Image as pilImage
from models.documentModel import Documento
from models.DadosPagamentoModel import DadosPagamento
from models.propostaFiador import DocumentoPropostaFiador
from models.PessoaModel import PessoaJuridica, PessoaFisica

meses = [
    "Janeiro", "Fevereiro", "Março", "Abril",
    "Maio", "Junho", "Julho", "Agosto",
    "Setembro", "Outubro", "Novembro", "Dezembro"
]

def generate_proposal_1(documento):
    try:
        pdf_file = f"proposta1_{documento.nome}_{documento.data_assinatura_contrato}.pdf"
        pdf_file = pdf_file.replace(" ", "")
        pdf_file = pdf_file.replace(":", "")
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

def generate_proposta_fiador(url_list, documento, dadosPagamento, pessoa, fiador, is_pf):
    try:
        pdf_file = f"proposta_fiador_{pessoa.nome}_{documento.data_assinatura_contrato}.pdf"
        pdf_file = pdf_file.replace(" ", "")
        pdf_file = pdf_file.replace(":", "")
        doc = SimpleDocTemplate(pdf_file, pagesize=letter)
        styles = getSampleStyleSheet()
        story = []

        document = return_proposta_fiador_template(documento, dadosPagamento, pessoa, fiador, is_pf)

        for paragraph in document.split('\n'):
            p = Paragraph(paragraph.replace('<b>', '<font name="Helvetica-Bold">').replace('</b>', '</font>'),
                          styles['Normal'])
            story.append(p)
            story.append(Spacer(1, 6))

        # imagem = Image(documento.imagem_io, width=150, height=100)
        # imagem.hAlign = 'LEFT'
        #
        # story.append(imagem)

        doc.build(story)

        url_list.append(save_doc_bucket(pdf_file))

        return url_list
    except Exception as e:
        err_msg = f'It was not possible to send the email. Cause: {traceback.format_exc()}'
        print(err_msg)
        raise e

def generate_proposta_sem_parcela(url_list, documento, dadosPagamento, pessoa, is_pf):
    try:
        pdf_file = f"proposta_sem_parcela_{pessoa.nome}_{documento.data_assinatura_contrato}.pdf"
        pdf_file = pdf_file.replace(" ", "")
        pdf_file = pdf_file.replace(":", "")
        doc = SimpleDocTemplate(pdf_file, pagesize=letter)
        styles = getSampleStyleSheet()
        story = []

        document = return_parcelamento_sem_garantia(documento, dadosPagamento, pessoa, is_pf)

        for paragraph in document.split('\n'):
            p = Paragraph(paragraph.replace('<b>', '<font name="Helvetica-Bold">').replace('</b>', '</font>'),
                          styles['Normal'])
            story.append(p)
            story.append(Spacer(1, 6))

        # imagem = Image(documento.imagem_io, width=150, height=100)
        # imagem.hAlign = 'LEFT'
        #
        # story.append(imagem)

        doc.build(story)

        url_list.append(save_doc_bucket(pdf_file))

        return url_list
    except Exception as e:
        err_msg = f'It was not possible to send the email. Cause: {traceback.format_exc()}'
        print(err_msg)
        raise e

def generate_proposta_pix(url_list, documento, dadosPagamento, pessoa, chave_pix, is_pf):
    try:
        pdf_file = f"proposta_pix_{pessoa.nome}_{documento.data_assinatura_contrato}.pdf"
        pdf_file = pdf_file.replace(" ", "")
        pdf_file = pdf_file.replace(":", "")
        doc = SimpleDocTemplate(pdf_file, pagesize=letter)
        styles = getSampleStyleSheet()
        story = []

        document = return_pix_template(documento, dadosPagamento, pessoa, chave_pix, is_pf)

        for paragraph in document.split('\n'):
            p = Paragraph(paragraph.replace('<b>', '<font name="Helvetica-Bold">').replace('</b>', '</font>'),
                          styles['Normal'])
            story.append(p)
            story.append(Spacer(1, 6))

        # imagem = Image(documento.imagem_io, width=150, height=100)
        # imagem.hAlign = 'LEFT'
        #
        # story.append(imagem)

        doc.build(story)

        url_list.append(save_doc_bucket(pdf_file))

        return url_list
    except Exception as e:
        err_msg = f'It was not possible to send the email. Cause: {traceback.format_exc()}'
        print(err_msg)
        raise e

def generate_proposta_cartao_credito(url_list, documento, dadosPagamento, pessoa, numero_cartao_credito, is_pf):
    try:
        pdf_file = f"proposta_cartao_credito_{pessoa.nome}_{documento.data_assinatura_contrato}.pdf"
        pdf_file = pdf_file.replace(" ", "")
        pdf_file = pdf_file.replace(":", "")
        doc = SimpleDocTemplate(pdf_file, pagesize=letter)
        styles = getSampleStyleSheet()
        story = []

        document = return_propsta_cartao_credito_template(documento, dadosPagamento, pessoa, numero_cartao_credito, is_pf)

        for paragraph in document.split('\n'):
            p = Paragraph(paragraph.replace('<b>', '<font name="Helvetica-Bold">').replace('</b>', '</font>'),
                          styles['Normal'])
            story.append(p)
            story.append(Spacer(1, 6))

        # imagem = Image(documento.imagem_io, width=150, height=100)
        # imagem.hAlign = 'LEFT'
        #
        # story.append(imagem)

        doc.build(story)

        url_list.append(save_doc_bucket(pdf_file))

        return url_list
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
        print(blob.public_url)
        url = blob.public_url
        return url
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
    url_list = []

    rua = data["rua"]
    numero_endereco = data["numero_endereco"]
    bairro = data["bairro"]
    cidade = data["cidade"]
    uf = data["uf"]
    cep = data["cep"]
    valor = data["valor_divida"]
    valor_desconto = data["valor_desconto"]
    vencimento_divida = data["vencimento_divida"]
    qtd_de_parcela = data["qtd_de_parcela"]
    is_pf = data["is_pf"]
    numero_cartao_credito = data["numero_cartao_credito"]

    locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')
    valor_formatado = locale.currency(valor, grouping=True)
    valor_formatado_por_extenso = numero_por_extenso(valor)
    valor_descontado = calcula_valor_descontado(valor, valor_desconto)
    valor_parcela = calculate_valor_parcela(valor_descontado, qtd_de_parcela)
    valor_parcela = locale.currency(valor_parcela, grouping=True)
    valor_formatado_descontado = locale.currency(valor_descontado, grouping=True)
    valor_descontado_por_extenso = numero_por_extenso(valor_descontado)

    endereco = return_complete_address(rua, numero_endereco, bairro, cidade, uf, cep)

    data_assinatura_contrato = datetime.now()
    data_assinatura_formatada = f"{data_assinatura_contrato.day} de {meses[data_assinatura_contrato.month - 1]} de {data_assinatura_contrato.year}"

    # imagem_io = get_Image_from_bucket(url_bucket)

    chave_pix = gerar_chave_pix_aleatoria()

    documento = DocumentoPropostaFiador(data_assinatura_formatada, data_assinatura_contrato, imagem_io="null")
    dadosPagamento = DadosPagamento(valor_formatado, valor_formatado_por_extenso, valor_formatado_descontado, valor_descontado_por_extenso, valor_desconto, qtd_de_parcela, valor_parcela)
    fiador = PessoaFisica("NOME DO FIADOR", "NACIONALIDADE DO FIADOR", "ESTADO CIVIL FIADOR", "CPF DO FIADOR", "ENDEREÇO DO FIADOR")
    if(is_pf):
        nome = data["nome"]
        nacionalidade = data["nacionalidade"]
        estado_civil = data["estado_civil"]
        cpf = data["cpf"]
        pessoaFisica = PessoaFisica(nome, nacionalidade, estado_civil, cpf, endereco)
        url_list = generate_proposta_fiador(url_list, documento, dadosPagamento, pessoaFisica, fiador, is_pf)
        url_list = generate_proposta_sem_parcela(url_list, documento, dadosPagamento, pessoaFisica, is_pf)
        url_list = generate_proposta_pix(url_list, documento, dadosPagamento, pessoaFisica, chave_pix, is_pf)
        url_list = generate_proposta_cartao_credito(url_list, documento, dadosPagamento, pessoaFisica, numero_cartao_credito, is_pf)
    else:
        nome_empresa = data["nome"]
        pj = data["pj"]
        cnpj = data["cnpj"]
        cpf_administrador = data["cpf_administrador"]
        nome_administrador = data["nome_administrador"]
        nacionalidade_administrador = data["nacionalidade_administrador"]
        estado_civil_administrador = data["estado_civil_administrador"]
        pessoaJuridica = PessoaJuridica(nome_empresa, pj, cnpj, endereco, cpf_administrador, nome_administrador, nacionalidade_administrador, estado_civil_administrador)
        url_list = generate_proposta_fiador(url_list, documento, dadosPagamento, pessoaJuridica, fiador, is_pf)
        url_list = generate_proposta_sem_parcela(url_list, documento, dadosPagamento, pessoaJuridica, is_pf)
        url_list = generate_proposta_pix(url_list, documento, dadosPagamento, pessoaJuridica, chave_pix, is_pf)
        url_list = generate_proposta_cartao_credito(url_list, documento, dadosPagamento, pessoaJuridica,
                                                    numero_cartao_credito, is_pf)

    return url_list