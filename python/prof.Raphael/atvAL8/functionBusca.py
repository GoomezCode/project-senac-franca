#   -------------------- FUNCTIONS --------------------
def buscaSeq(i, chave):
    for (indice, el) in enumerate(i):
        if el[0] == chave:
            return indice
    return None

def getAllGroup(list):
    todos = []
    verific = todos    

    for i in list:
        todos.append({"posicao": buscaSeq(list, i[0]), "ponto": i[1]})
    newList = []
    for i, t in enumerate(todos, start=1):
        ponto = t["ponto"]
        
        for j, n in enumerate(verific, start=1):
            if i == j:
                continue

            if t["posicao"] == n["posicao"]:
                ponto += n["ponto"]
                verific.remove({"posicao": n["posicao"], "ponto": n["ponto"]})

        newList.append({"posicao": t["posicao"], "ponto": ponto})
    listFinal = []

    for i in newList:
        listFinal.append({"nome": list[i["posicao"]][0], "ponto": i["ponto"]})

    return listFinal

def getGroup(list, nome):
    for i in getAllGroup(list):
        if i["nome"].lower() == nome.lower():
            return [i["nome"], i["ponto"]]
    return None
#   -------------------- FUNCTIONS --------------------


#   -------------------- TESTE --------------------
teste = [
  ["Wolverine", 5],
  ["Deadpool", 3],
  ["Wolverine", 10],
  ["Deadpool", 2],
  ["Aranha", 5],
  ["Fantasma", 13],
  ["Deadpool", 2],
  ["Aranha", 2],
  ["Fantasma", 21],
  ["Aranha", 6],
  ["Wolverine", 30]
]

nome = "Aranha"
if getGroup(teste, nome) != None:
    print(getGroup(teste, nome)[0], " | ", getGroup(teste, nome)[1])
else:    print("Grupo não encontrado!!")

#   -------------------- TESTE --------------------
