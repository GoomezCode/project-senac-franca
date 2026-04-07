import process
import os

def windowIndex():
    process.clearTerminal()
    while(True):
        print(5*"-------"," Welcome PetShop ",5*"-------")
        print("(1) - Cadastrar pessoa")
        print("(2) - Cadastrar pet")
        print("(3) - Encerrar programa")
        print("")
        escolha = int(input("Faça sua escolha: "))

        if escolha == 1:
            windowPerson()
        elif escolha == 2:
            windowPet()
        else:
            process.clearTerminal()
            process.stopProcess()


def windowPerson():
    process.clearTerminal()
    while(True):
        print(5*"-------"," Cadastro da pessoa ",5*"-------")
        nome = input("Digite Nome: ")
        telefone = input("Digite Telefone: ")
        endereco = input("Digite Endereço: ")

        print("")
        print("(1) - Cadastrar pet")
        print("(2) - voltar menu")
        print("(3) - Encerrar programa")
        print("")
        escolha = int(input("Faça sua escolha: "))

        if escolha == 1:
            windowPet()
        elif escolha == 2:
            windowIndex()
        else:
            process.clearTerminal()
            process.stopProcess()

def windowPet():
    process.clearTerminal()
    while(True):
        print(5*"-------"," Cadastro do Pet ",5*"-------")
        nome = input("Digite nome Pet: ")
        idade = int(input("Digite idade Pet: "))
        raca = input("Digite raça Pet: ")

        print("")
        print("(1) - Cadastrar pessoa")
        print("(2) - voltar menu")
        print("(3) - Encerrar programa")
        print("")
        escolha = int(input("Faça sua escolha: "))

        if escolha == 1:
            windowPerson()
        elif escolha == 2:
            windowIndex()
        else:
            process.clearTerminal()
            process.stopProcess()

windowIndex()