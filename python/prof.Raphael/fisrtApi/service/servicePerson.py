import json
import os

_pathCaminho = os.path.join("database/database.json")

dados = []
    
def createPerson(person):
        dados.append(person)
        with open(_pathCaminho, "w", encoding="utf-8") as f:
                json.dump(dados, f, indent=4,ensure_ascii=False)
                
pessoa1 = {"nome":"daniel"}
pessoa2 = {"nome":"daniel1"}
pessoa3 = {"nome":"danie2"}
pessoa4 = {"nome":"danie3"}

createPerson(pessoa1)
createPerson(pessoa2)
createPerson(pessoa3)
createPerson(pessoa4)
