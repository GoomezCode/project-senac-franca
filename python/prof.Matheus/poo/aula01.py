import json
from fpdf import FPDF

clients = []
arquivo = open("client.json", "r")
clients = json.load(arquivo)
arquivo.close()


class client():
    def __init__(self, nome, nascimento,email,cpf):
        id = len(clients)+1
        self.nome = nome
        self.nascimento = nascimento
        self.email = email
        self.cpf = cpf
        
        arquivo = open("client.json", "w")
        clients.append({"id":id,"nome": nome, "nascimento":nascimento, "email":email, "cpf":cpf})
        json.dump(clients, arquivo)
        arquivo.close()
        
    
    def printInfoClient(idClient):
        client = clients[idClient]
        msg = f"""
        Id = {client["id"]}
        Nome = {client["nome"]}
        nascimento = {client["nascimento"]}
        email = {client["email"]}
        cpf = {client["cpf"]}
        """
        return msg

    
def createRelatorio():
    pdf = FPDF()
    
    pdf.add_page()
    pdf.set_font("Arial", "B", 16)
    for i in range(len(clients)):
        pdf.multi_cell(0, 8, txt=client.printInfoClient(i))
    pdf.output("teste.pdf")
        
    
# ps1 = client(            
#         "fulano",
#         "10/09/2008",
#         "daniel@gmail.com",
#         "000.000.000-00"    
# )
# ps2 = client(            
#         "betano",
#         "4/02/2012",
#         "gabriel@gmail.com",
#         "000.000.000-00"    
# )


createRelatorio()
# print("\n", clients)


