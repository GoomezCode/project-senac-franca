import os
import json


file = os.path.join("app/database", "DB_Characters.json")

def readJson():
    with open(file, "r", encoding="UTF-8") as afile:
        return json.load(afile)
    
def createJson(character):
    data = readJson()
    data.append(character)
    with open(file,"w", encoding="UTF-8") as afile:
        json.dump(data,afile,indent=4)

def updateJson(dados):
    for n,i in enumerate(dados):
        i["id"] = (n+1) 
    with open(file,"w", encoding="UTF-8") as afile:
        json.dump(dados,afile,indent=4)
