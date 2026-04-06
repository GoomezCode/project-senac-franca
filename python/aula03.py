def atv01(inicial, final):
    msg = ""
    for inicial in range(final):
        msg += f"{inicial+1} - "
    print(msg)

def atv02(num):
    for i in range(11):
        print(f"{num} X {i} = {num * i}")

def atv03():
    par = 0;
    impar = 0;

    for i in range(4):
        num = int(input(f"{i+1} - Digite o valor: "))
        if num % 2 == 0:
            par += 1
        else:
            impar += 1

    print(f"Teve {par} pares | {impar} impares")

def atv04():
    maiorNum = None
    for i in range(5):
        numero = int(input("Informe o valor: "))
        if maiorNum == None or numero > maiorNum:
            maiorNum = numero

def atv05():
    inicial = int(input("Numero inicial: "))
    final = int(input("Numero final: "))

    for i in range(inicial,final):
        if i % 5 == 0:
            print(i)

def atv06():
    val = int(input("Informe o num: "))
    num = [1,2]
    for i in range(val):
        ensimo = num[i] + num[i+1]
        num.append(ensimo)

def atv07():
    anterior = 0;
    atual = 1;
    for i in range(10):
        proximo = anterior + atual
        anterior = atual
        atual = proximo
        print(proximo)