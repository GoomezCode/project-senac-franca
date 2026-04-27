def calcular_bonus(salario_base):
    if salario_base < 2500:
        salario_base += 300
    return salario_base

def descontar_sindicato(salario_com_bonus):
    return salario_com_bonus - (salario_com_bonus * 0.03)

salarioAtual = float(input("Digite seu salário atual: "))
salarioFinal = descontar_sindicato(calcular_bonus(salarioAtual))
print(f"Você recebera: R${salarioFinal:.2F}")