## ------------------ Functions ------------------
def calcCelsius(celsius):
    return (celsius * 1.8) + 32

def calcPar(num):
    return "Par" if num % 2 == 0 else "Impar"

def analisar_estoque(estoque):
    for i,p in enumerate(estoque, start=1):
        if p >= 5:
            print(f"Produto {i}: Estoque OK!")
        else:
            print(f"Produto {i}: Estoque BAIXO (Repor)!")
            
def filtrar_produtos_caros(precos):
    produtos_selecionados = []
    for i in precos:
        if i > 100:
            produtos_selecionados.append(i)
    return produtos_selecionados

def puxarNome():
    return "Daniel"
## ------------------ Functions ------------------


nome = puxarNome()


produtos = [700,40,22,675,110,32,328,899,110,32,328,40,22,675]
print(filtrar_produtos_caros(produtos))