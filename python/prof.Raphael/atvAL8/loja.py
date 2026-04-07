import processLoja
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

for i in range(2):
    idade = int(input("Sua idade: "))
    nota = input("Nota em | A | B | C | D | E: ").lower

    # resp.append({"resposta": nota, "idade": idade})

msg = f""" 
Quantidade de resposta A : 
maior idade de pessoas resposta A: 
Média de idade das pessoas que responderam D: (qtd)
maior idade de pessoas resposta D: (idade)
Porcentagem de respostas E: (porcento)%
menor idade da resposta E: (idade)

"""

print(msg)



    




