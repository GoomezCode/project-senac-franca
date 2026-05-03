from service.exceptions import unitPrice

def menuCadastrarProduto():
    while(True):
        try:
            print(5*"---","Cadastrar Produto",5*"---")
            print("")
            nome = input("Nome: ")
            categoria = input("Categoria: ")
            qdtAtual = float(input("Quantidade atual: "))
            if qdtAtual < 0: raise unitPrice
            precoUnitario = float(input("Preço unitario: "))
            estoqueMinimo = float(input("Estoque minimo: "))
            ncm = input("Ncm: ")
            cfopEntrada = input("Cfop Entrada: ")
            cfopSaida = input("Cfop saida: ")
        except unitPrice as e:
            print(e)
            break
    
        

menuCadastrarProduto()