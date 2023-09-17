from utils.utils import return_str_pessoa

def return_pix_template(documento, dadosPagamento, pessoa, chave_pix, is_pf):
    devedor = return_str_pessoa(pessoa, is_pf)
    return f"""
        <b>INSTRUMENTO PARTICULAR DE CONFISSÃO DE DÍVIDA E ACORDO</b>

        CREDORA: ALGAR TELECOM S/A, pessoa jurídica de direito privado, inscrita no CNPJ sob o n°. 71.208.516/0001-74, com sede à Rua José Alves Garcia, nº 415, Mezanino, Bairro Brasil, Uberlândia/MG, CEP 38.400-668.
        
        {devedor}
        
            As partes identificadas acima firmam o presente instrumento particular de confissão de dívida, que se regerá pelas condições e cláusulas abaixo
        
        <b>CLÁUSULA PRIMEIRA</b> – DO VALOR
        
        1.1 - Ressalvadas quaisquer outras obrigações aqui não incluídas, pelo presente instrumento e na melhor forma de direito, o (a) DEVEDOR (A) confessa dever ao CREDOR a quantia líquida, certa e exigível no valor de {dadosPagamento.valor_formatado} ({dadosPagamento.valor_formatado_por_extenso}).
        
        1.2 - O valor aqui pactuado decorre de dívida oriunda de prestação de serviço telefônico, referente ao contrato x , y e z a qual não fora (m) quitada (s) à época oportuna pelo DEVEDOR.
        
        <b>CLÁUSULA SEGUNDA</b> – DO PAGAMENTO
        
        2.1 – Reconhecendo como boa a origem da dívida, o DEVEDOR, comprometem-se a pagar na seguinte conformidade:
        
        2.1.1 – no valor de {dadosPagamento.valor_formatado_descontado} ({dadosPagamento.valor_descontado_por_extenso}) a serem pagos pelo DEVEDOR, através de PIX disponibilizado , com expiração de 24 horas.
        
        Parágrafo Primeiro : Fica autorizado desde já, em caso de inadimplência a execução do presente instrumento, ao pagamento do valor integral do débito, sobre o qual incidirá a aplicação de multa de 10%, juros de mora de 1% ao mês e correção monetária e mais custas processuais e honorários advocatícios na base de 20% sobre o valor total do débito. Os valores monetários serão corrigidos de acordo com a tabela da Corregedoria do Egrégio Tribunal de Justiça de Minas Gerais.
        
         Parágrafo Segundo : Fica autorizado desde já, em caso de inadimplência, o desconto dos valores devidos diretamente no salário da <b>DEVEDORA</b>, até o importe de 30%, bem como penhora de suas contas poupanças, até o limite do débito, ficando estabelecido para tanto negócio jurídico processual, nos termos do art. 190 do Código de Processo Civil (CPC/2015).
        
        <b>CLÁUSULA TERCEIRA</b> – DA EXIGIBILIDADE DA DÍVIDA
        
        3.1 - A DÍVIDA ora reconhecida e assumida pelo <b>DEVEDOR</b> como líquida, certa e exigível, no valor acima mencionado, aplica-se o disposto no artigo 784, III, do Código de Processo Civil Brasileiro, haja vista o caráter de título executivo extrajudicial do presente instrumento de confissão de dívida.
        
        Parágrafo único: A eventual tolerância à infringência de qualquer das cláusulas deste instrumento ou o não exercício de qualquer direito nele previsto constituirá mera liberalidade do CREDOR, não implicando em novação ou transação de qualquer espécie.
        
        <b>CLÁUSULA QUARTA</b> - DO TÍTULO PROTESTADO
        
        4.1- Caso haja título protestado, compete EXCLUSIVAMENTE à <b>DEVEDORA</b> solicitar à <b>CREDORA</b> o termo de anuência para a retirada do protesto.
        
        Parágrafo único: Referido termo de anuência somente será enviado após a quitação total do valor estipulado no presente termo.
        
        <b>CLÁUSULA QUINTA</b> – DA ADESÃO AO JUIZO 100% DIGITAL
        
        As partes declaram, para os devidos fins, que nos termos da Resolução TRE/PA nº 5.689/2021 c/c Resolução CNJ nº 345, de 9/10/2020, Lei nº 13.105 ( CPC) e Lei nº 11.419 de 19/12/2006, optam pelo <b>JUÍZO 100% DIGITAL</b>, autorizando citação e comunicação dos atos processuais pelo WhatsApp,  nos termos do art. 190 do Código de Processo Civil (CPC/2015).
        
        <b>CLÁUSULA SEXTA</b>–   DA VALIDADE DA ASSINATURA
        
        6.1 As partes envolvidas neste instrumento afirmam e declaram que esse poderá ser assinado por qualquer modalidade de assinatura eletrônica prevista em lei, dispensada a assinatura de testemunhas por sua integridade ter sido conferida pelo provedor da assinatura  com fundamento no Artigo 10, parágrafo 2º da MP 2200-2/2001 c/c art.784 § 4º do CPC.
        6.2 As Partes renunciam ao direito de recusar ou contestar a validade das assinaturas eletrônicas, na medida máxima permitida pela legislação aplicável.
        
        <b>CLÁUSULA SÉTIMA</b> –  DO FORO
        
        Para dirimir qualquer dúvida oriunda deste instrumento fica eleito o Foro da Comarca de {chave_pix}, com exclusão de qualquer outro por mais privilegiado que seja.
        
        Uberlândia e {documento.data_assinatura_formatada}.
        
        Assinatura.

    """