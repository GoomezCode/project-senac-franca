def desafio01():
    print("")
    print("")
    print(10* ("--"),"Evolução de classe de personagem", 10*("--"))
    print(" ")
    level = int(input("Digite o nivel do personagem: "))
    classe = int(input("escolha a classe de seu personagem | Guerreiro (1) | Mago (2) |: "))
    def condicao():
        if(level <= 10):
            print("Nível insuficiente para evoluir. Continue treinando!")
        if(level <= 20):
            print("Evoluiu para Cavaleiro") if (classe == 1) else print("Evoluiu para Arquimago")
        if(level > 20):
            print("Evoluiu para Paladino") if (classe == 1) else print("Evoluiu para Invocador")

    condicao() if (classe == 1 or classe == 2) else print("Classe inválida.")


def desafio02():
    defeitosVisual = int(input("Tem defeitos visuais?: | Não (0) | Sim (1) |: "))
    peso = float(input("Qual o peso em gramas da peça?: "))
    diametro = float(input("Qual o diametro em milímetros da peça?: "))

    if (defeitosVisual == 0):
        if(peso >= 150 and peso < 160 and diametro >= 20 and diametro < 22):
            print("Aprovação Premium")
        elif(peso >= 140 and peso < 170 and diametro >= 18 and diametro < 24):
            print("Aprovação Padrão")
        else:
            print("Reprocessamento")
    else:print("Peça descartada")
