name = input("Digite o nome do personagem: ")

status = ["forca", "agilidade", "inteligencia", "sorte"]
forca = 0
agilidade = 0
inteligencia = 0
sorte = 0

def verific(opcao, nStatus):
    global forca    
    global agilidade
    global inteligencia
    global sorte
    
    if nStatus == "forca":
        forca = opcao
    if nStatus == "agilidade":
        agilidade = opcao
    

print(f"Informe o status do {name} de 1 a 10")
for i in status:
    op = int(input(f"{i}: "))
    