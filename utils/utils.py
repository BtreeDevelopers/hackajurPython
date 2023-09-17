import locale
import re
import smtplib
import email.message
import os
import random
import string

def send_email(payload, useremail, subject):

    msg = email.message.Message()
    msg['Subject'] = subject
    msg['From'] = os.getenv('EMAIL')
    msg['To'] = useremail
    password = os.getenv('EMAIL_PASSWORD')
    msg.add_header('Content-Type', 'text/html')
    msg.set_payload(payload)

    s = smtplib.SMTP('smtp.gmail.com: 587')
    s.starttls()
    # Login Credentials for sending the mail
    s.login(msg['From'], password)
    s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))

def cep_with_mask(cep):
    masked_cep = re.sub(r'^(\d{5})-?(\d{3})$', r'\1-\2', cep)
    return masked_cep

def cpf_with_mask(cpf):
    cpf_regex = re.compile(r'(\d{3})(\d{3})(\d{3})(\d{2})')
    return cpf_regex.sub(r'\1.\2.\3-\4', cpf)

def cnpj_with_mask(cnpj):
    cnpj_regex = re.compile(r'(\d{2})(\d{3})(\d{3})(\d{4})(\d{2})')
    return cnpj_regex.sub(r'\1.\2.\3/\4-\5', cnpj)

def formatted_number_value(valor):
    locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')
    return locale.currency(valor, grouping=True)

def calcula_valor_descontado(valor, desconto):
    return valor - ((valor*desconto)/100)

def calculate_valor_parcela(valor, qtd_parcela):
    return valor/qtd_parcela

def return_str_pessoa(pessoa, is_pf):
    if(is_pf):
        return f"""
            <b>DEVEDOR PF</b>: {pessoa.nome}, {pessoa.nacionalidade}, {pessoa.estado_civil}, portador do CPF nº {pessoa.cpf}, residente e domiciliado no endereço {pessoa.endereco}.
        """
    else:
        return f"""
            <b>DEVEDOR PJ</b>: {pessoa.nome}, pessoa jurídica de direito {pessoa.pj}, inscrita no {pessoa.cnpj}, representada pela sócio administrador {pessoa.nome_administrador}, {pessoa.nacionalidade_administrador}, {pessoa.estado_civil_administrador}, portador do CPF nº {pessoa.cpf_administrador} , residente e domiciliado no endereço {pessoa.endereco}.
        """

def gerar_chave_pix_aleatoria(tamanho=20):
    caracteres = string.ascii_letters + string.digits  # letras maiúsculas, minúsculas e dígitos
    chave_pix = ''.join(random.choice(caracteres) for _ in range(tamanho))
    return chave_pix