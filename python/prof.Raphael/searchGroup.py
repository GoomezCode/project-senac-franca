import os
#   -------------------- FUNCTIONS --------------------
def buscaSeq(i, chave):
    for (indice, el) in enumerate(i):
        if el[0].lower() == chave:
            return indice
    return None

def getAllGroup(list):
    grupos = [] 
    for elemento in list:
        nome   = elemento[0]  
        pontos = elemento[1]
        indice = buscaSeq(grupos, nome) 

        if indice is not None:
            grupos[indice][1] += pontos
        else:
            grupos.append([nome, pontos])
    return grupos

def getGroup(list, nome):
    for i in getAllGroup(list):
        if i[0].lower() == nome.lower():
            return [i[0], i[1]]
    return None
#   -------------------- FUNCTIONS --------------------


def verifOption(nums, option):
    t = False
    for i in nums:
        if option == i:
            t = True
            break
    return t
grupos = [
    ["Wolverine", 5],
    ["deadpool", 3],
    ["wolverine", 10],
    ["Deadpool", 2],
    ["aranha", 5],
    ["fantasma", 13],
    ["deadpool", 2],
    ["aranha", 2],
    ["fantasma", 21],
    ["aranha", 6],
    ["wolverine", 30],
    ["fantasma", 80]
  ]
os.system("cls") if os.name == "nt" else os.system("clear")
option = 2000
while True:
    try:
        nums = [1, 2, 3, 4]
        print("----- Gincana Escolar -----")
        print(" (1) addGroup")
        print(" (2) getAllGroups")
        print(" (3) getGroup")
        print(" (0) exit")
        option = int(input("Digite a opção desejada: "))
        t = False
        for i in nums:
            if option == i:
                t = True
            break
        if not t and option != 0:
            os.system("cls") if os.name == "nt" else os.system("clear")
            print("Opção inválida!! \nPor favor, digite uma opção válida.")
            print("")
    except (ValueError, NameError):
        os.system("cls") if os.name == "nt" else os.system("clear")
        print("Entrada inválida!! \nPor favor, digite um número.")
        print("")
    
    try:
        if option == 1:
            os.system("cls") if os.name == "nt" else os.system("clear")
            print("----- Add Group -----")
            nome = input("Digite o nome do grupo: ").lower()
            ponto = int(input("Digite o ponto do grupo: "))
            grupos.append([nome, ponto])
            os.system("cls") if os.name == "nt" else os.system("clear")
            print(f"Grupo '{nome}' adicionado com {ponto} pontos!")
            print("")
    except ValueError:
        os.system("cls") if os.name == "nt" else os.system("clear")
        print("Entrada inválida!! \nPor favor, tente novamente.")
        print("")

    if option == 2:
        os.system("cls") if os.name == "nt" else os.system("clear")
        print("----- All Groups -----")
        
        for i in getAllGroup(grupos):
            print("Nome: ",i[0], " | ", "Pontos: ", i[1])

        print("----------------------")
        print("")

    if option == 3:
        os.system("cls") if os.name == "nt" else os.system("clear")
        print("----- Get Group -----")
        nome = input("Digite o nome do grupo: ")
        if getGroup(grupos, nome) != None:
            print("")
            print(getGroup(grupos, nome)[0], " | ", getGroup(grupos, nome)[1])
        else:
            print("")
            print("Grupo não encontrado!!")
        print("----------------------")
        print("")

    if option == 0:
        os.system("cls") if os.name == "nt" else os.system("clear")
        print("Saindo do programa...")
        break   