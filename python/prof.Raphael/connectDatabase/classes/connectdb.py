import mysql.connector
from mysql.connector import Error


class connectMysql:
    def __init__(self, host, username, password, bank, port):
        self.host = host
        self.username = username
        self.password = password
        self.bank = bank
        self.port = port
        self.conexao = None
    def connect(self):
        try:
            self.conexao = mysql.connector(
                host = self.host,
                database = self.bank,
                user = self.username,
                password = self.password,
                port = self.port
            )
            if self.conexao.is_connected():
                print("Conexão feita")
                return self.conexao
        except Error as error:
            print(f"Erro ao conectar: {error}")
            return None
        
