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