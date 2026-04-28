# **Descrição da Task:**

# Refatorar o código criando uma função dedicada para exibição dos resultados.

# **Critérios de Aceite:**
# - Criar função `exibeMedias(media_testes, media_provas, media_disciplina)`
# - A função deve receber as 3 médias como parâmetros
# - Exibir todas as médias formatadas
# - Manter a lógica de cálculo no programa principal
# - Melhorar organização do código

# **Exemplo da função:**
# ```python
# def exibeMedias(media_testes, media_provas, media_disciplina):
#     print(f"Média dos testes: {media_testes:.1f}")
#     print(f"Média das provas: {media_provas:.1f}")
#     print(f"Média da disciplina: {media_disciplina:.1f}")
# ```

# **Prazo:** 1 dia
# **Prioridade:** Baixa


# ---------------- Functions ----------------
def calculaMedia(nota1, peso1, nota2, peso2):
    return round((nota1 * peso1 + nota2 * peso2) / (peso1 + peso2),1)

def calculaMediafinal(mediaTeste, peso1, mediaProva, peso2):
    return round((mediaTeste * peso1 + mediaProva * peso2) / (peso1 + peso2), 1)

def exibirMedias(mediaTeste, mediaProvas, mediaDisciplinas):
    print(f"Media dos testes: {mediaTeste}")
    print(f"Media das provas: {mediaProvas}")
    print(f"Média da disciplina: {mediaDisciplinas}")
# ---------------- Functions ----------------    

# ---------------- Input ----------------    
teste1 = float(input("Digite a nota do teste 1: "))
teste2 = float(input("Digite a nota do teste 2: ")) 
print("")
nota1 = float(input("Digite a nota da prova 1: "))
nota2 = float(input("Digite a nota da prova 2: "))
print("")
peso1 = int(input("Digite o peso 1: "))
peso2 = int(input("Digite o peso 2: "))
print("")
# ---------------- Input ----------------    

# ---------------- Variaveis ----------------
mediaTeste = calculaMedia(teste1,peso1, teste2,peso2)
mediaProvas = calculaMedia(nota1,peso1, nota2,peso2)
mediaDisciplinas = calculaMediafinal(mediaTeste,peso1, mediaProvas,peso2)
# ---------------- Variaveis ----------------

# ---------------- Views ----------------
exibirMedias(mediaTeste, mediaProvas, mediaDisciplinas)
# ---------------- Views ----------------