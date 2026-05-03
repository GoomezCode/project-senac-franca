from repository.databaseConnection import estoque
class product:
    def __init__(self,nome, categoria, quantidade_atual, preco_unitario, estoque_minimo, ncm, cfop_entrada, cfop_saida):
        global estoque
        
        self.codigo = len(estoque) # int
        self.nome = nome # String
        self.categoria = categoria # String
        self.quantidade_atual = quantidade_atual # float
        self.preco_unitario = preco_unitario # float
        self.estoque_minimo = estoque_minimo # float
        self.ncm = ncm # String
        self.cfop_entrada = cfop_entrada # String
        self.cfop_saida = cfop_saida # String
    
    def cadastrar_produto(product):
        global estoque
        estoque.append({
            "codigo": product.codigo,
            "nome": product.nome,
            "categoria": product.categoria,
            "quantidade_atual": product.quantidade_atual,
            "preco_unitario": product.preco_unitario,
            "estoque_minimo": product.estoque_minimo,
            "ncm": product.ncm,
            "cfop_entrada": product.cfop_entrada,
            "cfop_saida": product.cfop_saida
        })
        
        
        