import service.exceptions
# def CodigoDuplicado()
# def validadeField()
# def validadeFormatNCM()
# def validadeFormatCFOP()

def validadeField(qtdInit, precoUnitario, estoqueMinimo, ncm, cfop):
    if qtdInit <= 0: return ("A quantidade inicial não pode ser negativa")
    
    