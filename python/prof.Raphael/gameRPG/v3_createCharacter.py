import os
from imgPersonagem import mostrar_classes
# name = input("Digite o nome do personagem: ")


status = ["forca", "agilidade", "inteligencia", "sorte"]
statusPerson = []
id = 0
forca = 0
agilidade = 0
inteligencia = 0
sorte = 0
distribuir = 20
maiorAt = 0

def createPlayer(name,s1,s2,s3,s4):
    global status
    global statusPerson
    global id
    global distribuir
    
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
                if distribuir <= 0:
                    raise AttributeError("Os pontos não fui distribuido corretamente")
                    
            
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
                    raise AttributeError("Os pontos não fui distribuido corretamente")
                break
            except ValueError as e:
                os.system("cls") if os.name == "nt" else os.system("clear")
                print(f"{e} \nDigite numero válido! \nFaça novamente!")
                print("")
            except AttributeError as e:
                os.system("cls") if os.name == "nt" else os.system("clear")
                print(f"{e}")
                return 404
                
    # ------------------------ Function ------------------------
    if s1 == 0: 
        while True:
            try:
                for i in status:
                    print(f"Informe o status do {name} de 1 a 10")
                    print("")
                    
                    if addAtributos(i) == 404:
                        raise ValueError("erro: 404 \nDistribuição incorreta!")
            except ValueError as e:
                distribuir = 20
                os.system("cls") if os.name == "nt" else os.system("clear")
                print(f"{e} \nFaça novamente!")
                print("")
            else:
                break
    else:
        forca = s1
        agilidade = s2
        inteligencia = s3
        sorte = s4
        maiorAt = max([s1,s2,s3,s4])
        distribuir = 20 - sum([s1,s2,s3,s4])

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

    id += 1
    distribuir = 20

    
def getAllPlayer():
    for i in statusPerson:
        print(f"""
{15*"---"}
Nome: {i["name"]}
forca: {i["forca"]}
agilidade: {i["agilidade"]}
inteligencia: {i["inteligencia"]}
sorte: {i["sorte"]}
class: {i["class"]} {mostrar_classes(i["class"])}
pontos: {i["ponto"]}
{15*"---"}
    
    """)