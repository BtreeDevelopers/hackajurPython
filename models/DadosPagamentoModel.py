class DadosPagamento:
    def __init__(self, valor_formatado,  valor_formatado_por_extenso, valor_formatado_descontado, valor_descontado_por_extenso, valor_desconto, qtd_de_parcela, valor_parcela_formatado):
        self.valor_formatado = valor_formatado
        self.valor_formatado_por_extenso = valor_formatado_por_extenso
        self.valor_formatado_descontado = valor_formatado_descontado
        self.valor_descontado_por_extenso = valor_descontado_por_extenso
        self.valor_desconto = valor_desconto
        self.qtd_de_parcela = qtd_de_parcela
        self.valor_parcela_formatado = valor_parcela_formatado