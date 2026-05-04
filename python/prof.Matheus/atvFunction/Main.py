estoque = [
    {"maca": 10},
    {"banana": 20},
    {"laranja": 15}
]

def adicionar_estoque(estoque, fruta, qntd):
    str(fruta).lower()
    for i in estoque:
        if i.get(fruta) != None:
            i[fruta] += qntd
            return "Adicionado com sucesso!!"
        else:
            continue
    estoque.append({fruta:qntd})
    return "Criado com sucesso!"
    
def vender_fruta(estoque, fruta, qntd):
    for i in estoque:
        if fruta in i:
            qtdFruta = i[fruta]
            if qntd <= qtdFruta:
                i[fruta] -= qntd
                return "venda realizada!!"
            else:return "Quantidade inválida"
        else:continue
    return "Produto não encontrado!!"
            
def relatorio_final(estoque):
    print("------ Relatorio Estoque ------")
    for i in estoque:
        chave = str(list(i)[0]).capitalize()
        valor = i[chave.lower()]
        print(f"{chave}: {valor}")
    print("")

msg0_0 = adicionar_estoque(estoque, "maca", 60)
msg0_1 = adicionar_estoque(estoque, "pera", 80)

msg1_0 = vender_fruta(estoque, "maca", 10)
msg1_1 = vender_fruta(estoque, "melancia", 5)
msg1_2 = vender_fruta(estoque, "laranja", 20)

print(msg0_0)
print(msg0_1)
print("")
print(msg1_0)
print(msg1_1)
print(msg1_2)
print("")

relatorio_final(estoque)