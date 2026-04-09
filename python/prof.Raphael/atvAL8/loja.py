# sabe da idade
# sabe a nota de A B C D E
# fara a opinião dos 10 primeiros
notaList =[
    {"nota": "a", "descricao": "otimo"},
    {"nota": "b", "descricao": "bom"},
    {"nota": "c", "descricao": "regular"},
    {"nota": "d", "descricao": "ruim"},
    {"nota": "e", "descricao": "pessimo"}
]
resp= []

for i in range(10):
    while True:
        try:
            print("")
            print("")
            idade = int(input("Sua idade: "))
            nota = str(input("Nota em | A | B | C | D | E: ")).lower()
            vl = False
            for i in notaList:
                if nota == i["nota"]:
                    vl = True
                    break
                else:
                    vl = False
            
            if vl == False:
                raise NameError("Errooooo")
        except ValueError:
            print("Digite um numero!!!")
        except NameError:
            print("Digite um caracter válido!!")
            print("Faça denovo!")
        else:
            resp.append({"resposta": nota, "idade": idade})
            break

qtdA = 0
maiorIdadeA = 0
qtdRespostas = 0
qtdD = 0
mediaIdadeD = 0
maiorIdadeD = 0
qtdE = 0
menorIdadeE = 0

for i in resp:
    qtdRespostas += 1
    if i["resposta"] == "a":
        qtdA += 1
        if i["idade"] > maiorIdadeA:
            maiorIdadeA = i["idade"]
    
    if i["resposta"] == "d":
        qtdD += 1
        mediaIdadeD += i["idade"]
        if i["idade"] > maiorIdadeD:
            maiorIdadeD = i["idade"]

    if i["resposta"] == "e":
        qtdE += 1
        if i["idade"] < menorIdadeE:
            menorIdadeE = i["idade"]

msg = f""" 
Quantidade de resposta A: {qtdA} 
maior idade de pessoas resposta A: {maiorIdadeA} 
Média de idade das pessoas que responderam D: {mediaIdadeD / qtdD if mediaIdadeD > 0 else 0}
maior idade de pessoas resposta D: {maiorIdadeD}
Porcentagem de respostas E: {qtdE/qtdRespostas * 100 if qtdE > 0 else 0}%
menor idade da resposta E: {menorIdadeE}
"""

print(msg)