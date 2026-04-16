import os
name = input("Digite o nome do personagem: ")
print(f"Informe o status do {name} de 1 a 10")
print("")


status = ["forca", "agilidade", "inteligencia", "sorte"]
statusPerson = []
id = len(statusPerson)
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
    if opcao > distribuir:
        raise ValueError(f"Digite o numero menor que {distribuir}")
    
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
    for i in status:
        forca = i["forca"]
        agilidade = i["agilidade"]
        inteligencia = i["inteligencia"]
        maiorAt = i["maiorAt"]
    
    if forca >= 8 or forca >= maiorAt:
        return "Guerreiro"
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
            if distribuir < 0:
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

statusPerson.append({
    "name": name,
    "forca": forca,
    "agilidade": agilidade,
    "inteligencia": inteligencia,
    "sorte": sorte,
    "maiorAt": maiorAt,
    })

statusPerson[id]["class"] = getClass(statusPerson)
statusPerson[id]["ponto"] = distribuir

def getAllPlayer():
    for i in statusPerson:
        print(f"""
        ------------- Status Personagem -------------
        Nome: {i["name"]}

        forca: {i["forca"]}
        agilidade: {i["agilidade"]}
        inteligencia: {i["inteligencia"]}
        sorte: {i["sorte"]}
        class: {i["class"]}

        pontos: {i["ponto"]}
        ------------- Status Personagem -------------
    """)