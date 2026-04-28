# **Descrição da Task:**

# Adaptar o sistema de média ponderada para processar os dados de uma turma de **sete alunos**.

# **Critérios de Aceite:**
# - Os pesos são iguais para todos os alunos
# - Os pesos devem ser lidos **apenas uma vez** no início do programa
# - Para cada aluno, ler:
#   - Nota do teste 1
#   - Nota do teste 2
#   - Nota da prova 1
#   - Nota da prova 2
# - Calcular para cada aluno:
#   - Média dos testes (ponderada)
#   - Média das provas (ponderada)
#   - Média da disciplina
# - Exibir as médias de cada aluno

# **Estrutura sugerida:**
# ```python
# # Ler pesos uma vez
# peso1 = float(input("Digite o peso 1: "))
# peso2 = float(input("Digite o peso 2: "))

# # Função para calcular média ponderada
# def calculaMedia(nota1, peso1, nota2, peso2):
#     return (nota1 * peso1 + nota2 * peso2) / (peso1 + peso2)

# # Loop para 7 alunos
# for aluno in range(1, 8):
#     print(f"\n--- Aluno {aluno} ---")
#     # Ler notas do aluno
#     # Calcular e exibir médias
# ```

# **Exemplo de saída:**
# ```
# --- Aluno 1 ---
# Média dos testes: 8.2
# Média das provas: 8.8
# Média da disciplina: 8.5

# --- Aluno 2 ---
# ...
# ```

# **Prazo:** 3 dias
# **Prioridade:** Alta

alunos = []

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
print(f"\n--- Colocar peso das provas ---")
peso1 = int(input("Digite o peso 1: "))
peso2 = int(input("Digite o peso 2: "))
print("")

for aluno in range(1, 8):
    print(f"\n--- Aluno {aluno} ---")   
    teste1 = float(input("Digite a nota do teste 1: "))
    teste2 = float(input("Digite a nota do teste 2: ")) 
    print("")
    nota1 = float(input("Digite a nota da prova 1: "))
    nota2 = float(input("Digite a nota da prova 2: "))
    
    mediaTeste = calculaMedia(teste1,peso1, teste2,peso2)
    mediaProvas = calculaMedia(nota1,peso1, nota2,peso2)
    mediaDisciplinas = calculaMediafinal(mediaTeste,peso1, mediaProvas,peso2)
    
    alunos.append({"mediaTeste": mediaTeste, "mediaProvas": mediaProvas, "mediaDisciplinas": mediaDisciplinas})    
# ---------------- Input ----------------    


# ---------------- Views ----------------
# exibirMedias(mediaTeste, mediaProvas, mediaDisciplinas)
for i, n in enumerate(alunos, start=1):
    print(f"--- Aluno {i} ---")
    print(f"Media dos testes: {n["mediaTeste"]}")
    print(f"Media das provas: {n["mediaProvas"]}")
    print(f"Média da disciplina: {n["mediaDisciplinas"]}")
    print("")
# ---------------- Views ----------------