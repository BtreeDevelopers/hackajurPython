
def return_debt_confession_document(nome, nacionalidade, endereco, estado_civil, cpf, numero_formatado, por_extenso, data_formatada):
    texto = f"""
    <b>INSTRUMENTO PARTICULAR DE CONFISSÃO DE DÍVIDA</b> 



    <b>CREDORA</b>: ALGAR TELECOM S/A, pessoa jurídica de direito privado, inscrita no CNPJ sob o n°. 71.208.516/0001-74, com sede à Rua José Alves Garcia, nº 415, Mezanino, Bairro Brasil, Uberlândia/MG, CEP 38.400-668.;

    <b>DEVEDOR PF</b>: {nome}, {nacionalidade}, {estado_civil}, portador do CPF nº {cpf}, residente e domiciliado no endereço {endereco}. 
    <b>DEVEDOR PJ</b>: Nome empresa, pessoa jurídica de direito privado/público, inscrita no CNPJ, representada pela sócia administradora nome, nacionalidade, estado civil, portador do RG nº e CPF nº, residente e domiciliado no endereço xx

     		Pelo presente instrumento particular e na melhor forma de direito, confessam e assumem como líquida e certa a dívida a seguir descrita:

    <b>CLÁUSULA PRIMEIRA</b>: Ressalvadas quaisquer outras obrigações aqui não incluídas, pelo presente instrumento e na melhor forma de direito, o <b>DEVEDOR</b> reconhece e confessa dever a <b>CREDORA</b> a quantia líquida, certa e exigível no valor de {numero_formatado} ({por_extenso}), cujo dívida segue discriminada abaixo.

     		A dívida, origina-se pela utilização dos serviços e produtos fornecidos pela Credora.

    <b>CLÁUSULA SEGUNDA</b>: Por este instrumento e na melhor forma de direito o  DEVEDOR confessa e reconhece que o débito está em atraso há x dias. 

    <b>CLÁUSULA TERCEIRA</b>: O DEVEDOR poderá realizar a negociação do presente débito, mediante termo de acordo.

    <b>CLÁUSULA QUARTA</b>: A DÍVIDA ora reconhecida e assumida pelo DEVEDOR, como líquida, certa e exigível, no valor acima mencionado, aplica-se o disposto no artigo 784,III, do Código de Processo Civil Brasileiro, haja vista o caráter de título executivo extrajudicial do presente instrumento de confissão de dívida, por ser documento particular.

    <b>CLÁUSULA QUINTA</b>: Não havendo a negociação do débito, poderá a CREDORA imediatamente executar o presente contrato.
    	§1º O DEVEDOR autoriza o desconto da importância constante na cláusula primeira de até de 30% de seu salário, bem como penhora de suas contas poupanças, até o limite do débito, ficando estabelecido para tanto negócio jurídico processual, nos termos do art. 190 do Código de Processo Civil (CPC/2015).

    §2º A execução do presente instrumento, importará ao pagamento do valor integral do débito, sobre o qual incidirá a aplicação de multa de 10%, juros de mora de 1% ao mês e correção monetária e mais custas processuais e honorários advocatícios na base de 20% sobre o valor total do débito.

    <b>CLÁUSULA SEXTA</b>: As partes declaram, para os devidos fins, que nos termos da Resolução TRE/PA nº 5.689/2021 c/c Resolução CNJ nº 345, de 9/10/2020, Lei nº 13.105 ( CPC) e Lei nº 11.419 de 19/12/2006, optam pelo JUÍZO 100% DIGITAL, autorizando citação e comunicação dos atos processuais pelo Whatsapp,  nos termos do art. 190 do Código de Processo Civil (CPC/2015).

    <b>CLÁUSULA SÉTIMA</b>: A eventual tolerância à infringência de qualquer das cláusulas deste instrumento ou o não exercício de qualquer direito nele previsto constituirá em mera liberalidade, não implicando em novação ou transação de qualquer espécie.

    <b>CLÁUSULA OITAVA</b>: Caso haja título protestado, compete EXCLUSIVAMENTE à <b>DEVEDORA</b> solicitar à <b>CREDORA</b> o termo de anuência para a retirada do protesto.

    <b>PARÁGRAFO ÚNICO</b>: Referido termo de anuência somente será enviado após a quitação total do valor estipulado no presente termo.

    <b>CLÁUSULA NONA</b>: Para dirimir qualquer dúvida oriunda deste instrumento fica eleito o Foro de Uberlândia/MG, com exclusão de qualquer outro que seja.

    Isto posto, firmam este instrumento.

    Uberlândia,  {data_formatada}


    """

    return texto