verific = [
    {"posicao": 0, "ponto": 5},
    {"posicao": 1, "ponto": 3},
    {"posicao": 0, "ponto": 10},
    {"posicao": 1, "ponto": 2},
    {"posicao": 4, "ponto": 13}
]

verific.remove( {"posicao": 1, "ponto": 2} )

for i in verific:
    print(i["posicao"]," | ",i["ponto"])



