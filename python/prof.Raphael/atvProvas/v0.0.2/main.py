# **Descrição da Task:**

# Refatorar a função `calculaMedia` para calcular média ponderada com pesos fixos: teste 1 com peso 2 e teste 2 com peso 3.

# **Critérios de Aceite:**
# - Manter o nome da função `calculaMedia`
# - Aplicar fórmula: (nota1 * 2 + nota2 * 3) / 5
# - Retornar o valor correto

# **Exemplo de uso:**
# ```python
# Entrada: 7.5 e 10.0
# Saída: 9.0
# ```

# **Prazo:** 1 dia
# **Prioridade:** Média

def calculaMedia(nota1, nota2):
    return round((nota1*2 + nota2*3) / 5, 1)

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

print(f"Media final: {calculaMedia(nota1, nota2)}")