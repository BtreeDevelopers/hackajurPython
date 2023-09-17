class PessoaFisica:
    def __init__(self, nome, nacionalidade, estado_civil, cpf, endereco):
        self.nome = nome
        self.nacionalidade = nacionalidade
        self.estado_civil = estado_civil
        self.cpf = cpf
        self.endereco = endereco

class PessoaJuridica:
    def __init__(self, nome, pj, cnpj, endereco, cpf_administrador, nome_administrador, nacionalidade_administrador, estado_civil_administrador):
        self.nome = nome
        self.cnpj = cnpj
        self.pj = pj
        self.endereco = endereco
        self.cpf_administrador = cpf_administrador
        self.nome_administrador = nome_administrador
        self.nacionalidade_administrador = nacionalidade_administrador
        self.estado_civil_administrador = estado_civil_administrador