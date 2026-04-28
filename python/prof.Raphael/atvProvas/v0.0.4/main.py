# **Descrição da Task:**

# Expandir o programa para calcular médias de testes E provas, mantendo os mesmos pesos.

# **Critérios de Aceite:**
# - Ler notas do teste 1 e 2
# - Ler notas da prova 1 e 2
# - Ler pesos (mesmos para testes e provas)
# - Calcular e exibir média dos testes
# - Calcular e exibir média das provas
# - Manter a função `calculaMedia` existente

# **Exemplo de execução:**
# ```
# Digite a nota do teste 1: 10
# Digite a nota do teste 2: 7
# Digite a nota da prova 1: 7
# Digite a nota da prova 2: 10
# Digite o peso 1: 2
# Digite o peso 2: 3

# Saída:
# Média dos testes: 8.2
# Média das provas: 8.8
# ```

# **Prazo:** 2 dias
# **Prioridade:** Alta



def calculaMedia(nota1, peso1, nota2, peso2):
    return round((nota1 * peso1 + nota2 * peso2) / (peso1 + peso2),1)

teste1 = float(input("Digite a nota do teste 1: "))
teste2 = float(input("Digite a nota do teste 2: ")) 
print("")
nota1 = float(input("Digite a nota da prova 1: "))
nota2 = float(input("Digite a nota da prova 2: "))
print("")
peso1 = int(input("Digite o peso 1: "))
peso2 = int(input("Digite o peso 2: "))
print("")
print(f"Media dos testes: {calculaMedia(teste1,peso1, teste2,peso2)}")
print(f"Media das provas: {calculaMedia(nota1,peso1, nota2,peso2)}")