class invoice:
    def __init__(self, numero_nf, tipo, data_emissao, fornecedor_cliente, cnpj_cpf, produtos, valor_total):
        self.numero_nf = numero_nf # String - único
        self.tipo = tipo # String -- entrada/saida
        self.data_emissao = data_emissao # datetime
        self.fornecedor_cliente = fornecedor_cliente # String
        self.cnpj_cpf = cnpj_cpf # String
        self.produtos = produtos # List
        self.valor_total = valor_total # float