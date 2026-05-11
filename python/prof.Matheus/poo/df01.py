class leitor:
    def __init__(self, nome):
        self.nome = nome
        self.livros_na_mao = []
        
    def pegar_livro(self, nome_do_livro):
        if(len(self.livros_na_mao) >= 3):
            return "Limite atingido! Devolva um livro primeiro."
        for n in self.livros_na_mao:
            if(n.lower() == nome_do_livro.lower()):
                return "Você já está com este título!"
            else: continue
        self.livros_na_mao.append(nome_do_livro)
        return "Empréstimo realizado!"
        
    def devolver_livro(self, nome_do_livro):
        for i,n in enumerate(self.livros_na_mao):
            if(n.lower() == nome_do_livro.lower()):
                self.livros_na_mao.pop(i)
                return "Devolução feita!!"
            else: continue
        return "Você não está com esse livro"


ps1 = leitor("daniel")
ps2 = leitor("gabriel")

#ps3 = leitor("matheus", 5)

print(ps1.pegar_livro("muito legal"))
print(ps1.pegar_livro("muito chato"))
print(ps1.pegar_livro("muito mas muito"))
print(ps1.pegar_livro("muito mas ++ chato"))
print(ps1.devolver_livro("MuITo LeGaL"))
print(ps2.devolver_livro("Opaa"))
print(ps2.pegar_livro("diaaa"))