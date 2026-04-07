import processConcurso

def valNota(nota, i):
    while(True):
        if int(nota) > 10 or int(nota) < 0:
            print("")
            print("Nota Inválida Tente denovo!")
            print("apenas notas de 0 a 10")
            print("")
            nota = input(f"{i} - Digite a nota: ")
        else:
            return nota

pessoa = []
for i in range(5):
    i+=1
    nome = input(f"{i} - Digite o nome: ")
    nota = input(f"{i} - Digite a nota: ")
    print("")
    nota = valNota(nota, i)

    ps = {"nome":nome, "nota": nota}
    pessoa.append(ps)

notaMax = pessoa[0]["nota"]
pessoaGanha = pessoa[0]["nome"]
for i in pessoa:
    if i["nota"] > notaMax:
        notaMax = i["nota"]
        pessoaGanha = i["nome"]

print(f"O vencedor é: {pessoaGanha} com a nota: {notaMax}")



