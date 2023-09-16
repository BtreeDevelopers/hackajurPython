class Documento:
    # Método construtor (inicializador)
    def __init__(self, nome, nacionalidade, endereco, estado_civil, cpf, numero_formatado, por_extenso, data_assinatura_formatada, data_assinatura_contrato, imagem_io):
        self.nome = nome
        self.nacionalidade = nacionalidade
        self.endereco = endereco
        self.estado_civil = estado_civil
        self.cpf = cpf
        self.numero_formatado = numero_formatado
        self.por_extenso = por_extenso
        self.data_assinatura_formatada = data_assinatura_formatada
        self.data_assinatura_contrato = data_assinatura_contrato
        self.imagem_io = imagem_io