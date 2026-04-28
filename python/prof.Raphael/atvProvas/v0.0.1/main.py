# **Descrição da Task:**

# Desenvolver uma função chamada `calculaMedia` que receba 2 valores reais como parâmetros e retorne sua média aritmética.

# **Critérios de Aceite:**
# - A função deve aceitar dois parâmetros do tipo float
# - Deve retornar a média aritmética correta
# - O programa principal deve ler as notas do usuário
# - Exibir o resultado formatado com uma casa decimal

# **Exemplo de uso:**
# ```python
# Entrada: 7.5 e 9.7
# Saída: Média dos testes: 8.6
# ```

# **Prazo:** 2 dias
# **Prioridade:** Alta

def calculaMedia(nota1, nota2):
    return round((nota1 + nota2) / 2, 1)

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

print(f"Media final: {calculaMedia(nota1, nota2)}")