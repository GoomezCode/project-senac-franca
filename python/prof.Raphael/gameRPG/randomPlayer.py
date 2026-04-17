import random
def randomName():
    sufixos = [
        "dor", "ion", "ar", "eth", "ius", "or", "an", "us", "ir", "el",
        "on", "as", "en", "um", "is", "orim", "adir", "eron", "ath", "orn",
        "iel", "ael", "uin", "orion", "azar", "ethor", "andar", "urion",
        "alion", "eon", "yra", "ara", "ora", "ira", "era", "una",
        "thor", "dun", "grim", "rak", "gorn", "drak", "vorn", "zun",
        "thar", "nor", "mir", "lir", "var", "dar", "zor", "kar",
        "BR", "GG", "Player", "99", "Bot"
    ]

    adjetivos = [
        "Forte", "Valente", "Indomável", "Implacável", "Brutal",
        "Invencível", "Destemido", "Feroz", "Inquebrável", "Lendário",
        
        "Arcano", "Místico", "Encantado", "Eterno", "Ancestral",
        "Etéreo", "Iluminado", "Profético", "Runico", "Astral",
        
        "Sombrio", "Maldito", "Profano", "Tenebroso", "Cruel",
        "Corrompido", "Sanguinário", "Vazio", "Obscuro", "Perdido",
        
        "Nobre", "Real", "Majestoso", "Glorioso", "Honrado",
        "Sagrado", "Ilustre", "Virtuoso", "Sublime", "Radiante",
        
        "Selvagem", "Verdejante", "Tempestuoso", "Flamejante",
        "Gélido", "Rochoso", "Ventoso", "Solar", "Lunar", "Primordial"
    ]


    prefixos = [
        "Ar", "Bel", "Cor", "Dor", "El", "Fal", "Gal", "Hel",
        "Is", "Jar", "Kel", "Lor", "Mor", "Nor", "Or", "Per",
        "Quel", "Ral", "Sel", "Tor", "Ul", "Val", "Xan", "Yel", "Zor",
        
        "Mal", "Vor", "Zar", "Kra", "Dra", "Gor", "Nar", "Thar",
        "Vel", "Xor", "Zek", "Mor", "Noct", "Teneb", "Umb", "Grim",

        "Ael", "Eri", "Ily", "Olo", "Uru", "Ae", "Io", "Lumi",
        "Nym", "Syl", "Eld", "Fae", "Myth", "Arc", "En",

        "Brak", "Drun", "Gar", "Thok", "Karn", "Rok", "Bar", "Dur",
        "Grak", "Hruk", "Krug", "Mag", "Rag", "Tor", "Vor",
        
        "Al", "Ed", "Fer", "Leo", "Theo", "Val", "Aur", "Reg",
        "Lux", "Cael", "Dom", "Max", "Oct", "Seb"
    ]
    return f"{random.choice(prefixos)}{random.choice(sufixos)} {random.choice(prefixos)}{random.choice(sufixos)}"


# tem que retornar 4 valores aleatorios que somados dão o valor do ponto e retornar o nome

def randomPlayer():
    ponto = 20
    nome = randomName()
    while True:
        num = [random.randint(1, 10) for n in range(4)]
        if sum(num) <= ponto:
            break
    return nome, num[0], num[1], num[2], num[3]