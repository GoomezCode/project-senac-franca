import os
import json


file = os.path.join("gameRPG_API/app/database", "DB_Characters.json")

def readJson():
    with open(file, "r", encoding="UTF-8") as afile:
        return json.load(afile)
    
def createJson(character):
    data = readJson()
    data.append(character)
    with open(file,"w", encoding="UTF-8") as afile:
        json.dump(data,afile,indent=4)
