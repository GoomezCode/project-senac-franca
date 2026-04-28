# **Descrição da Task:**

# Alterar a função `calculaMedia` para receber os pesos como parâmetros adicionais.

# **Critérios de Aceite:**
# - Função deve receber: nota1, peso1, nota2, peso2
# - Programa principal deve ler os pesos do usuário
# - Calcular média ponderada com os pesos informados
# - Fórmula: (nota1 * peso1 + nota2 * peso2) / (peso1 + peso2)

# **Exemplo de uso:**
# ```python
# Entrada: 7.5, peso 2, 10.0, peso 3
# Saída: 9.0
# ```

# **Prazo:** 1 dia
# **Prioridade:** Alta



def calculaMedia(nota1, peso1, nota2, peso2):
    return round((nota1 * peso1 + nota2 * peso2) / (peso1 + peso2),1)

nota1 = float(input("Digite a primeira nota: "))
peso1 = int(input("Digite seu peso: "))
nota2 = float(input("Digite a segunda nota: "))
peso2 = int(input("Digite seu peso: "))

print(f"Media final: {calculaMedia(nota1,peso1, nota2,peso2)}")