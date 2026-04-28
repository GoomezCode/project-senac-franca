# **Descrição da Task:**

# Adicionar o cálculo da média final da disciplina.

# **Critérios de Aceite:**
# - Calcular média da disciplina usando os mesmos pesos
# - Fórmula: (média_teste * peso1 + média_prova * peso2) / (peso1 + peso2)
# - Exibir a média da disciplina junto com as outras médias

# **Exemplo de saída adicional:**
# ```
# Média da disciplina: 8.5
# ```

# **Prazo:** 1 dia
# **Prioridade:** Média



def calculaMedia(nota1, peso1, nota2, peso2):
    return round((nota1 * peso1 + nota2 * peso2) / (peso1 + peso2),1)

def calculaMediafinal(mediaTeste, peso1, mediaProva, peso2):
    return round((mediaTeste * peso1 + mediaProva * peso2) / (peso1 + peso2))

teste1 = float(input("Digite a nota do teste 1: "))
teste2 = float(input("Digite a nota do teste 2: ")) 
print("")
nota1 = float(input("Digite a nota da prova 1: "))
nota2 = float(input("Digite a nota da prova 2: "))
print("")
peso1 = int(input("Digite o peso 1: "))
peso2 = int(input("Digite o peso 2: "))
print("")

mediaTeste = calculaMedia(teste1,peso1, teste2,peso2)
mediaProvas = calculaMedia(nota1,peso1, nota2,peso2)
mediaDisciplinas = calculaMediafinal(mediaTeste,peso1, mediaProvas,peso2)

print(f"Media dos testes: {mediaTeste}")
print(f"Media das provas: {mediaProvas}")
print(f"Média da disciplina: {mediaDisciplinas}")