from collections import Counter

def buscaSeq(i, chave):
    for (indice, el) in enumerate(i):
        if el[0] == chave:
            return indice
    return None

def testeFunction():
    lAlunos = [["Mickey", 8.7], ["Pateta", 6.5], ["Minnie", 9.9], ["Pato Donald", 7.2]]
    nome = "Pateta"
    indice = buscaSeq(lAlunos, nome)
    if indice != None:
        print(f"Aluno: {nome}\tNota: {lAlunos[indice][1]}")
    else:
        print("Aluno não encontrado")

teste = [
  ["Wolverine", 5],
  ["Deadpool", 3],
  ["Wolverine", 5],
  ["Deadpool", 2],
  ["Fantasma", 13],
  ["Deadpool", 2],
  ["Fantasma", 21]
]
todos = []
qntPosicao = []
list = teste
for i in list:
    todos.append({"posicao": buscaSeq(list, i[0]), "ponto": i[1]})

# print(posicoes)
# print(valores)
# print(todos)
newList = []
for i, t in enumerate(todos, start=1):
    qntPosicao.append(t["posicao"])
    # print(i, " - ",t["posicao"], " -- quantidade: ")



# Wolverine - 0  =  5
# Deadpool - 1  =  3
# Wolverine - 0  =  5
# Deadpool - 1  =  2
# Fantasma - 4  =  13
# Deadpool - 1  =  2
# Fantasma - 4  =  13