import os

def windowCreate():
    os.system("cls") if os.name == "nt" else os.system("clear")
    print(5*"---","create player",5*"---")
    
    print("Insira 5 para um nick aleatorio")
    print("")
    # Adicione a função criar personagem
    
    print(5*"---","create player",5*"---")


os.system("cls") if os.name == "nt" else os.system("clear")
print(5*"---","Game RPG",5*"---")

print("(1) - create player")
print("(2) - create random player")
print("(3) - get all player")
print("(0) - exit")
print("")
opc = int(input("Escolha: "))

print(5*"---","Game RPG",5*"---")

if opc == 1:
    windowCreate()