from app import app
from flask import request, jsonify
from app.service import randomPlayer
from app.service import serviceJson


def getClass(i):
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
    jsonMsg = {
        "error":"default",
        "dica":"default"
    }    
    
    point = 20
    name = request.args.get("name", default=randomPlayer.randomName()) # caso o parametro name não seja adicionado ira criar um nome aleatorio para o user
    force = request.args.get("force", default=0)
    agility = request.args.get("agility", default=0)
    inteligence = request.args.get("inteligence", default=0)
    luck = request.args.get("luck", default=0)
    
    if not force and not agility and not inteligence and not luck:
        # caso n use nenhum parametro ira criar um player aleatorio 
        n,f,a,i,l = randomPlayer.randomPlayer()
        name = n
        force = f
        agility = a
        inteligence = i
        luck = l
        
    
    if not force:
        jsonMsg["error"] = "Parametro está errado!"
        jsonMsg["dica"]="use '/api/createPlayer?force=' "
        return jsonify(jsonMsg)
    if not agility:
        jsonMsg["error"] = "Parametro está errado!"
        jsonMsg["dica"]="use '/api/createPlayer?agility=' "
        return jsonify(jsonMsg)
    if not inteligence:
        jsonMsg["error"] = "Parametro está errado!"
        jsonMsg["dica"]="use '/api/createPlayer?inteligence=' "
        return jsonify(jsonMsg)
    if not luck:
        jsonMsg["error"] = "Parametro está errado!"
        jsonMsg["dica"]="use '/api/createPlayer?luck=' "
        return jsonify(jsonMsg)

    point = point - (int(force) + int(agility) + int(inteligence) + int(luck))

    character = {
        "name":name,
        "force": force,
        "agility": agility,
        "inteligence":inteligence,
        "luck":luck,
        "point": point
    }
    character["class"]= getClass(character)
    
    serviceJson.createJson(character)
    return jsonify(character)



@app.route("/api/searchCharacter", methods={"GET"})
def searchCharacter():  
    dados = serviceJson.readJson()
    
    name = request.args.get("name")
    classe = request.args.get("class")

    
    if name and classe: # faz a filtragem pelo os dois parametros
        dadosFilter = []
        for i in dados: 
            if i["name"].lower() == name.lower() and i["class"].lower() == classe.lower():
                dadosFilter.append(i)

        return jsonify(dadosFilter)
    
    if name:
        dadosNam = []
        for i in dados:# filtra pelo nome especifico
            if i["name"].lower() == name.lower():
                dadosNam.append(i)

        return jsonify(dadosNam)
    
    if classe: # filtra apenas para os user com a class especifica
        dadosClass = []
        for i in dados:
            if i["class"].lower() == classe.lower():
                dadosClass.append(i)

        return jsonify(dadosClass)

# Caso não use nenhum tipo de filter ira aparecer todos os users
    return jsonify(dados)