import random
def senhaUser(senha):
    # senha = input("Digite sua senha: ")
    while senha != "Sen@c2026":
        print("Senha Incorreta!, tente novamente")
        print("")
        senha = input("Digite sua senha: ")
        if senha == "Sen@c2026":
            print("")
            print("Acesso Permitido!")

# senha = input("Digite sua senha: ")
# senhaUser(senha)

def gameAdivinha(numUser):
    num = random.randint(1, 70)
    while True:
        if numUser < num:
            print("O número digítado é menor")
            print("")
            numUser = int(input("Digite o numero: "))

        elif numUser > num:
            print("O número digítado é maior")
            print("")
            numUser = int(input("Digite o numero: "))
        else:
            break
    print("Seu palpite está correto!!")

# numUser = int(input("Digite o numero: "))
# gameAdivinha(numUser)