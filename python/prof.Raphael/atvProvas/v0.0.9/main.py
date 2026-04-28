# **Descrição da Task:**

# Alterar o programa do desafio anterior para que, após processar todos os alunos da turma, também exiba a **média aritmética dos alunos que obtiveram média menor que 3.0** na disciplina.

# **Critérios de Aceite:**
# - Considerar apenas a média na disciplina de cada aluno
# - Calcular a média aritmética dos alunos com média < 3.0
# - Exibir o resultado com **uma casa decimal**
# - Se **nenhum aluno** tiver média menor que 3.0, exibir mensagem indicando: "Nenhum aluno ficou com média abaixo de 3.0"

# **Exemplo de cálculo:**
# ```
# Médias na disciplina dos 7 alunos:
# 8.0, 10.0, 2.8, 1.2, 9.3, 2.4, 5.5

# Alunos com média < 3.0: 2.8, 1.2, 2.4
# Média aritmética = (2.8 + 1.2 + 2.4) / 3 = 2.133... → 2.1

# Saída: "Média dos alunos com nota < 3.0: 2.1"
# ```

# **Estrutura sugerida:**
# ```python
# # Lista para armazenar médias dos alunos em recuperação
# medias_recuperacao = []

# # Durante o loop dos alunos
# if media_disciplina < 3.0:
#     medias_recuperacao.append(media_disciplina)

# # Após o loop
# if medias_recuperacao:
#     media_recuperacao = sum(medias_recuperacao) / len(medias_recuperacao)
#     print(f"Média dos alunos com nota < 3.0: {media_recuperacao:.1f}")
# else:
#     print("Nenhum aluno ficou com média abaixo de 3.0")
# ```

# **Exemplo de saída completa:**
# ```
# --- Aluno 1 ---
# Média dos testes: 8.2
# Média das provas: 8.8
# Média da disciplina: 8.5

# --- Aluno 2 ---
# Média dos testes: 5.5
# Média das provas: 6.0
# Média da disciplina: 5.8

# --- Aluno 3 ---
# Média dos testes: 3.0
# Média das provas: 2.5
# Média da disciplina: 2.7

# --- Aluno 4 ---
# Média dos testes: 4.0
# Média das provas: 4.5
# Média da disciplina: 4.3

# --- Aluno 5 ---
# Média dos testes: 2.5
# Média das provas: 3.0
# Média da disciplina: 2.8

# --- Aluno 6 ---
# Média dos testes: 9.0
# Média das provas: 9.5
# Média da disciplina: 9.3

# --- Aluno 7 ---
# Média dos testes: 2.0
# Média das provas: 2.5
# Média da disciplina: 2.3

# ========================================
# 📊 ESTATÍSTICA DA TURMA
# ========================================
# Média dos alunos com nota < 3.0: 2.6
# ```

# **Prazo:** 2 dias
# **Prioridade:** Média

alunos = []
medias_recuperacao = []

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

for aluno in range(1, 2):
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
    
print(f"""
========================================
📊 ESTATÍSTICA DA TURMA
========================================
      """)
for i in alunos:    
    if i["mediaDisciplinas"] < 3.0:
        medias_recuperacao.append(i)

if medias_recuperacao:
    media_recuperacao = sum(medias_recuperacao) / len(medias_recuperacao)
    print(f"Média dos alunos com nota < 3.0: {media_recuperacao:.1f}")
else:
    print("Nenhum aluno ficou com média abaixo de 3.0")
print("")
# ---------------- Views ----------------