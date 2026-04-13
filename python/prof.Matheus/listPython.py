listas = [] # aceita numeros repitidos
sets = [] # não recebe numeros repitidos
tuplas = ()
dicionarios = {}

vogais = "aeiou"
pl = input("Digite uma palavra: ")
qntdVogal = 0
for i in pl:
    if i in vogais:
        qntdVogal +=1
    
    
print(qntdVogal)
