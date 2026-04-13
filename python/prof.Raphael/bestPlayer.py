# Uma grande emissora de televisão quer fazer uma enquete entre os seus telespectadores para saber qual o melhor jogador após cada jogo. Para isto, faz-se necessário o desenvolvimento de um programa, que será utilizado pelas telefonistas, para a computação dos votos. Sua equipe foi contratada para desenvolver este programa.
# Para computar cada voto, a telefonista digitará um número, entre 1 e 23, correspondente ao número da camisa do jogador. Um número de jogador igual zero, indica que a votação foi encerrada. Se um número inválido for digitado, o programa deve ignorá-lo, mostrando uma breve mensagem de aviso, e voltando a pedir outro número. Após o final da votação,

# o programa deverá exibir: O total de votos computados; Os númeos e respectivos votos de todos os jogadores que receberam votos; O percentual de votos de cada um destes jogadores; O número do jogador escolhido como o melhor jogador da partida, juntamente com o número de votos e o percentual de votos dados a ele. Observe que os votos inválidos e o zero final não devem ser computados como votos. O resultado aparece ordenado pelo número do jogador.

# O programa deve fazer uso de arrays. O programa deverá executar o cálculo do percentual de cada jogador através de uma função. Esta função receberá dois parâmetros: o número de votos de um jogador e o total de votos. A função calculará o percentual e retornará o valor calculado.

# Exemplo: Enquete: Quem foi o melhor jogador?
# Número do jogador (0=fim): 9 Número do jogador (0=fim): 10 Número do jogador (0=fim): 9 Número do jogador (0=fim): 10 Número do jogador (0=fim): 11 Número do jogador (0=fim): 10 Número do jogador (0=fim): 50 Informe um valor entre 1 e 23 ou 0 para sair! Número do jogador (0=fim): 9 Número do jogador (0=fim): 9 Número do jogador (0=fim): 0

# num deve 1 - 23
# num == 0 Encerre Programa
# fim programa exibir total de votos
# porcentual
# o melhor jogador
import os
import collections
import math

votos = [2,3,5,3,2,4,6,8]

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
melhorJogador = []

# Os númeos e respectivos votos de todos os jogadores que receberam votos; O percentual de votos de cada um destes jogadores;
for i,n in enumerate(porcentual):
    votos = round(totalPessoa*(n/100))
    print(f"camisa: {jogadoresVotados[i]} | Votos: {votos} | Porcentual: {n}")

msg = f"""
Total de votos: {totalPessoa}
"""

print(votos)    
print(jogadoresVotados)    
print(porcentual)


    