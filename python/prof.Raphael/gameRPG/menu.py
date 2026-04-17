from v3_createCharacter import createPlayer, getAllPlayer, statusPerson
import randomPlayer
import os

def windowCreate():
    os.system("cls") if os.name == "nt" else os.system("clear")
    print(5*"---","create player",5*"---")
    print("Insira 5 para um nick aleatorio")
    print("")
    name = input("Digite seu Nick: ")
    if name == "5":
        os.system("cls") if os.name == "nt" else os.system("clear")
        print(5*"---","create player",5*"---")
        print("")
        createPlayer(randomPlayer.randomName(), 0, 0, 0, 0)
    else:
        os.system("cls") if os.name == "nt" else os.system("clear")
        print(5*"---","create player",5*"---")
        print("")
        createPlayer(name,0, 0, 0, 0)

os.system("cls") if os.name == "nt" else os.system("clear")
while True:
    try:
        print(5*"---","Game RPG",5*"---")

        print("(1) - create player")
        print("(2) - create random player")
        print("(3) - get all player")
        print("(0) - exit")
        print("")
        opc = int(input("Escolha: "))

        print(5*"---","Game RPG",5*"---")

        if opc > 3:
            raise ValueError("Opção Inválida")

        if opc == 1:
            windowCreate()
        if opc == 2:
            os.system("cls") if os.name == "nt" else os.system("clear")
            name, s1,s2,s3,s4 = randomPlayer.randomPlayer()
            createPlayer(name,s1,s2,s3,s4)    
            print(f"O jogador {name} foi criado!!")
            print("")
        if opc == 3:
            if len(statusPerson) > 0:
                os.system("cls") if os.name == "nt" else os.system("clear")
                print("------------- Status Personagem -------------")
                getAllPlayer()
                print("------------- Status Personagem -------------")
                print("")
                print("")
            else:
                os.system("cls") if os.name == "nt" else os.system("clear")    
                print("Não tem player cadastrado...")
                print("")
        if opc == 0:
            os.system("cls") if os.name == "nt" else os.system("clear")
            print("Sistema finalizado....")
            break
    except ValueError as e:
        os.system("cls") if os.name == "nt" else os.system("clear")
        print(f"Erro: {e} \nTente novamente!")
        print("")