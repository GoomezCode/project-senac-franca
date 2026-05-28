from app import app
from flask import request, jsonify
from app.service import randomPlayer
from app.service import serviceJson


def getClass(i):
    """
    Determina a classe do personagem com base nos atributos.

    Parâmetros:
        i (dict): Dicionário contendo os atributos do personagem:
            - force (int)
            - agility (int)
            - inteligence (int)
            - luck (int)

    Regras:
        - Se força >= 8 OU for o maior atributo -> "Guerreiro"
        - Se agilidade >= 8 OU for o maior atributo -> "Arqueiro"
        - Se inteligência >= 8 OU for o maior atributo -> "Mago"
        - Caso contrário -> "Aventureiro"

    Retorno:
        str: Nome da classe do personagem
    """
    forca = int(i["force"])
    agilidade = int(i["agility"])
    inteligencia = int(i["inteligence"])
    luck = int(i["luck"])

    maiorAt = max([forca, agilidade, inteligencia, luck])

    if forca >= 8 or forca >= maiorAt:
        return "Guerreiro"
    elif agilidade >= 8 or agilidade >= maiorAt:
        return "Arqueiro"
    elif inteligencia >= 8 or inteligencia >= maiorAt:
        return "Mago"
    else:
        return "Aventureiro"


@app.route("/api/createPlayer", methods={"GET"})
def createPlayer():
    """
    Cria um novo personagem.

    Endpoint:
        GET /api/createPlayer

    Parâmetros opcionais (via query string):
        - name (str): Nome do personagem
        - force (int): Força
        - agility (int): Agilidade
        - inteligence (int): Inteligência
        - luck (int): Sorte

    Comportamento:
        - Caso nenhum atributo seja enviado:
            → Um personagem aleatório é gerado automaticamente
        - Caso algum atributo esteja faltando:
            → Retorna erro informando o parâmetro faltante
        - Total de pontos base = 20
            → Pontos restantes = 20 - soma dos atributos

    Retorno:
        JSON com:
            - name
            - force
            - agility
            - inteligence
            - luck
            - point (pontos restantes)
            - class (definida automaticamente)

    Exemplo de uso:
        /api/createPlayer?name=Goku&force=8&agility=5&inteligence=4&luck=3
    """

    jsonMsg = {
        "error": "default",
        "dica": "default"
    }

    point = 20
    id = len(serviceJson.readJson())+1

    # Captura parâmetros da URL
    name = request.args.get("name", default=randomPlayer.randomName())
    force = request.args.get("force", default=0)
    agility = request.args.get("agility", default=0)
    inteligence = request.args.get("inteligence", default=0)
    luck = request.args.get("luck", default=0)

    # Se nenhum atributo for informado → gera automático
    if not force and not agility and not inteligence and not luck:
        n, f, a, i, l = randomPlayer.randomPlayer()
        name = n
        force = f
        agility = a
        inteligence = i
        luck = l

    # Validação de parâmetros obrigatórios
    if not force:
        jsonMsg["error"] = "Parametro está errado!"
        jsonMsg["dica"] = "use '/api/createPlayer?force=' "
        return jsonify(jsonMsg)

    if not agility:
        jsonMsg["error"] = "Parametro está errado!"
        jsonMsg["dica"] = "use '/api/createPlayer?agility=' "
        return jsonify(jsonMsg)

    if not inteligence:
        jsonMsg["error"] = "Parametro está errado!"
        jsonMsg["dica"] = "use '/api/createPlayer?inteligence=' "
        return jsonify(jsonMsg)

    if not luck:
        jsonMsg["error"] = "Parametro está errado!"
        jsonMsg["dica"] = "use '/api/createPlayer?luck=' "
        return jsonify(jsonMsg)

    # Cálculo de pontos restantes
    point = point - (int(force) + int(agility) + int(inteligence) + int(luck))

    # Estrutura do personagem
    character = {
        "id": id,
        "name": name,
        "force": force,
        "agility": agility,
        "inteligence": inteligence,
        "luck": luck,
        "point": point
    }
    # Define a classe automaticamente
    character["class"] = getClass(character)

    # Salva no JSON
    serviceJson.createJson(character)

    return jsonify(character)


@app.route("/api/searchCharacter", methods={"GET"})
def searchCharacter():
    """
    Busca personagens armazenados no JSON.

    Endpoint:
        GET /api/searchCharacter

    Parâmetros opcionais:
        - name (str): Nome do personagem
        - class (str): Classe do personagem

    Regras de filtragem:
        - Se name e class forem enviados:
            → Filtra pelos dois
        - Se apenas name:
            → Filtra por nome
        - Se apenas class:
            → Filtra por classe
        - Se nenhum:
            → Retorna todos personagens

    Comparação:
        - Case insensitive (ignora maiúsculas/minúsculas)

    Retorno:
        Lista JSON de personagens

    Exemplos:
        /api/searchCharacter
        /api/searchCharacter?name=Goku
        /api/searchCharacter?class=Mago
        /api/searchCharacter?name=Goku&class=Guerreiro
    """

    # Lê todos os personagens
    dados = serviceJson.readJson()

    # Parâmetros de filtro
    name = request.args.get("name")
    classe = request.args.get("class")

    # Filtrar por nome E classe
    if name and classe:
        dadosFilter = []
        for i in dados:
            if i["name"].lower() == name.lower() and i["class"].lower() == classe.lower():
                dadosFilter.append(i)
        return jsonify(dadosFilter)

    # Filtrar apenas por nome
    if name:
        dadosNam = []
        for i in dados:
            if i["name"].lower() == name.lower():
                dadosNam.append(i)
        return jsonify(dadosNam)

    # Filtrar apenas por classe
    if classe:
        dadosClass = []
        for i in dados:
            if i["class"].lower() == classe.lower():
                dadosClass.append(i)
        return jsonify(dadosClass)

    # Retorna todos
    return jsonify(dados)

@app.route("/api/deleteCharacter", methods=["GET"])
def deleteCharacter():
    dados = serviceJson.readJson()
    id = request.args.get("id")
    
    if not id:
        return jsonify({
            "Erro": "Coloque um ID!",
            "Dica": "Use '/api/deleteCharacter?id=' "
        })
        
    for n,i in enumerate(dados):
        if int(i["id"]) == int(id):
            dados.pop(n)
            serviceJson.updateJson(dados)
            return f"Character {i["name"]} foi deletado com sucesso!!"
    
    return jsonify({
        "Erro": "User nao encontrado!",
        "dica": "Coloque um id existente!"
    })