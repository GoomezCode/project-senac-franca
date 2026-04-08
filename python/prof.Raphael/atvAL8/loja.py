# sabe da idade
# sabe a nota de A B C D E
# fara a opinião dos 10 primeiros

notaList =[
    {"a": "otimo"},
    {"b": "bom"},
    {"c": "regular"},
    {"d": "ruim"},
    {"e": "pessimo"}
]
resp= []
for i in range(2):
    idade = int(input("Sua idade: "))
    nota = input("Nota em | A | B | C | D | E: ").lower
    resp.append({"resposta": nota, "idade": idade})
qtdA = 0
maiorIdadeA = 0

qtdRespostas = 0

qtdD = 0
mediaIdadeD = 0
maiorIdadeD = 0


qtdE = 0
menorIdadeE = 0
if i in resp:
    qtdRespostas += 1
    if i["resposta"] == "a":
        qtdA += 1
        if i["idade"] > maiorIdadeA:
            maiorIdadeA = i["idade"]
    elif i["resposta"] == "d":
        qtdD += 1
        mediaIdadeD += i["idade"]
        if i["idade"] > maiorIdadeD:
            maiorIdadeD = i["idade"]
    elif i["resposta"] == "e":
        qtdE += 1
        if i["idade"] < menorIdadeE:
            menorIdadeE = i["idade"]

porcentagemE = qtdE/qtdRespostas * 100 
mediaIdadeD = mediaIdadeD / qtdD



msg = f""" 
Quantidade de resposta A: {qtdA} 
maior idade de pessoas resposta A: {maiorIdadeA} 
Média de idade das pessoas que responderam D: {mediaIdadeD}
maior idade de pessoas resposta D: {maiorIdadeD}
Porcentagem de respostas E: {porcentagemE}%
menor idade da resposta E: {menorIdadeE}
"""
print(msg)



    




