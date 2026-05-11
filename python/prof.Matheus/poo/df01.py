class livro:
    def __init__(self, titulo):
        self.titulo = titulo
        self.disponivel = True
        
class leitor:
    def __init__(self, nome):
        self.nome = nome
        self.livros_na_mao = []
        
    def pegar_livro(self, livro_objeto):
        
        if(len(self.livros_na_mao) >= 3):
            return "Limite atingido! Devolva um livro primeiro."
        for i in range(len(self.livros_na_mao)):
            if(self.livros_na_mao[i].titulo in livro_objeto.titulo):
                return "Você já está com este título!"
        if(livro_objeto.disponivel):
            self.livros_na_mao.append(livro_objeto)
            livro_objeto.disponivel = False
            return "Empréstimo realizado!"    
        else:
            return "O livro está indisponivel"
        
    def devolver_livro(self, livro_objeto):
        for i in range(len(self.livros_na_mao)):
            if(self.livros_na_mao[i].titulo.lower() == livro_objeto.titulo.lower()):
                self.livros_na_mao.remove(livro_objeto.titulo)
                return "Devolução feita!!"
            else: continue    
        return "Você não está com esse livro"
        


# ps1 = leitor("daniel")
# ps2 = leitor("gabriel")

# lv1 = livro("teste")
# lv2 = livro("opa")
# lv3 = livro("eita")
# lv4 = livro("fiaa")

# print(ps1.pegar_livro(lv1))

lv1 = livro("dia")
lv2 = livro("noite")

ps1 = leitor("daniel")
ps2 = leitor("gabriel")

print(ps1.pegar_livro(lv1))
print(ps2.pegar_livro(lv1))

#ps3 = leitor("matheus", 5)