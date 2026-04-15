import os
name = input("Digite o nome do personagem: ")
print(f"Informe o status do {name} de 1 a 10")
print("")


status = ["forca", "agilidade", "inteligencia", "sorte"]
forca = 0
agilidade = 0
inteligencia = 0
sorte = 0
distribuir = 20
maiorAt = 0

# ------------------------ Function ------------------------
def vOpcao(opcao, nStatus):
    global forca    
    global agilidade
    global inteligencia
    global sorte
    global distribuir
    
    if nStatus == "forca":
        forca = opcao
        distribuir -= opcao
    if nStatus == "agilidade":
        agilidade = opcao
        distribuir -= opcao
    if nStatus == "inteligencia":
        inteligencia = opcao
        distribuir -= opcao
    if nStatus == "sorte":
        sorte = opcao
        distribuir -= opcao

def getClass(status):
    forca = status[1]["forca"]
    agilidade = status[2]["agilidade"]
    inteligencia = status[3]["inteligencia"]
    maiorAt = status[5]["maiorAt"]
    
    if forca >= 8 or forca >= maiorAt:
        return "Gurreiro"
    elif agilidade >= 8 or agilidade >= maiorAt:
        return "Arqueiro"
    elif inteligencia >= 8 or inteligencia >= maiorAt:
        return "Mago"
    else:
        return "Aventureiro"

def addAtributos(i):
    global distribuir
    global maiorAt

    while True: 
        try:
            if distribuir == 0:
                distribuir = 20
                raise ValueError("Os pontos não fui distribuido corretamente")
        
            print(f"Pontos: {distribuir}")
            print("")
            op = int(input(f"{i}: "))
            
            if op > 10 or op <= 0:
                os.system("cls") if os.name == "nt" else os.system("clear")
                print(f"Digite numero válido! \nTente novamente!")
                print("")
                continue
                # raise ValueError("Numero Não está entre 1 e 10")
            if op < 10 or op <= 0:
                if op > maiorAt:
                    maiorAt = op
            vOpcao(op, i)
            os.system("cls") if os.name == "nt" else os.system("clear")
            
            if distribuir < 0:
                distribuir = 20
                raise ValueError("Os pontos não fui distribuido corretamente")
            break
        except ValueError as e:
            os.system("cls") if os.name == "nt" else os.system("clear")
            print(f"{e} \nDigite numero válido! \nFaça novamente!")
            print("")
# ------------------------ Function ------------------------



while True:
    try:
        for i in status:
            addAtributos(i)
    except ValueError as e:
        distribuir = 20
        os.system("cls") if os.name == "nt" else os.system("clear")
        print(f"{e} \nDigite numero válido! \nFaça novamente!")
        print("")
    else:
        break


statusPerson = [
    {"name": name}, # 0
    {"forca": forca}, # 1
    {"agilidade": agilidade}, # 2
    {"inteligencia": inteligencia}, # 3
    {"sorte": sorte}, # 4
    {"maiorAt": maiorAt} # 5
]
statusPerson.append({"class": getClass(statusPerson)}) # 6
statusPerson.append({"Ponto": distribuir}) # 7

print(statusPerson)