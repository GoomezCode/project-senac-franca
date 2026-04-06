
# -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def atv01():
    list = []
    for i in range(3):
        num = input("digite o numero: ")
        list.append(num)
    list.sort()
    print(list)

# -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def atv02():
    salario = input("Digite seu salario: ")
    antesSalario = salario
    porcento = 0.0

    salario = int(salario)
    if(salario <= 280):
        porcento = 0.20
        salario += salario * porcento
    elif(salario <= 700):
        porcento = 0.15
        salario += salario * porcento
    elif(salario < 1500):
        porcento = 0.10
        salario += salario * porcento
    elif(salario >= 1500):
        porcento = 0.05
        salario += salario * porcento

    print(f"""
Salário antes {antesSalario}R$
Aumentado por {porcento}%
Salário depois {salario}R$

Antes: {antesSalario} | Depois: {salario}
""")
    
# -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def atv03():
    ano = input("Digite algum ano: ")
    bissexto = "SIM" if int(ano) % 4 == 0 else "NÂO"

    print(f"""
Ano digitado: {ano}
Ele e bissexto?: {bissexto}
""")
    
# -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

