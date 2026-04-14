import os
import collections

votos = [2,3,5,3,2,4,6,8,2]

os.system("cls") if os.name == "nt" else os.system("clear")
while True:
    num = 0
    try:
        print(5*"----"," Best Player ",5*"----")
        print("Digite 0 para sair!")
        print("")
        num = int(input("Digite o num do jogador (1 - 23): "))
        print("")
        if num == 0: break
        if num > 23 or num < 0:
            raise ValueError
    except ValueError:
        os.system("cls") if os.name == "nt" else os.system("clear")
        print("Erro! \nDigite o numero válido!")
        print("")
    else:
        votos.append(num)
        os.system("cls") if os.name == "nt" else os.system("clear")
        
votos = collections.Counter(votos)
jogadoresVotados = []
porcentual = []
totalPessoa = 0

for i in range(23):
    totalPessoa += votos[i]    
for i in votos:
    jogadoresVotados.append(i)
for i in range(23):    
    vtJogador = votos[i]
    if vtJogador != 0:
        porcentual.append( (vtJogador/totalPessoa) * 100)
    else: continue
    
# melhorJogador.append({"camisa": 2, "votos": 2, "porcetagem": 25})
jogador = []

os.system("cls") if os.name == "nt" else os.system("clear")
print("")
# Os númeos e respectivos votos de todos os jogadores que receberam votos; O percentual de votos de cada um destes jogadores;
for i,n in enumerate(porcentual):
    votosI =  round(totalPessoa*(n/100))
    jogador.append({"camisa": jogadoresVotados[i], "votos": votosI, "porcentual": f"{n:.2F}"})
    print(f"camisa: {jogadoresVotados[i]} | Votos: {votosI} | Porcentual: {n:.2F}%")

melhor = jogador[0]["votos"]
melhorJogador = []
for n,i in enumerate(jogadoresVotados):
    if votos[i] >= melhor:
        melhor = votos[i]
print("")
for i in jogador:
    if i["votos"] == melhor:
        print(f"Melhor Jogador --> Camisa: {i["camisa"]}, Votos: {i["votos"]}, Porcentual: {i["porcentual"]}%")
print("")
print(f"Total de votos: {totalPessoa}")
print("")