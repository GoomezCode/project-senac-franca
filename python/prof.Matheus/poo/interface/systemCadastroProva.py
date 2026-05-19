import tkinter as tk
from tkinter import messagebox
class window:
    def __init__(self):
        self.window = tk.Tk()
        self.window.geometry("800x800")
        self.window.resizable(0,0)
        self.window.title("Cadastro e Correção de provas")
        
        
        self.lblTitle = tk.Label(
            text="Cadastro Aluno",
            font=("Arial", 17)
        ).pack()
        
        # ====== Ra aluno ======
        self.lblRaAl = tk.Label(
            text="Coloque seu RA:",
            font=("Arial", 10)
        ).pack()
        self.inputRaAl = tk.Entry(
            self.window,
            font=("Arial", 15),
            width=20
        )
        self.inputRaAl.pack(pady=10)
        # ====== Ra aluno ======
        
        # ====== Nome aluno ======
        self.lblNomeAluno = tk.Label(
            self.window,
            text="Coloque seu Nome:",
            font=("Arial", 10)
        ).pack()
        self.inputNomeAluno = tk.Entry(
            self.window,
            font=("Arial", 15),
            width=20
        )
        self.inputNomeAluno.pack()
        # ====== Nome aluno ======
        
        # ====== Btn aluno ======
        self.btnCadastrarAluno = tk.Button(
            self.window,
            text="Cadastrar aluno",
            font=("Arial", 15),
            command=lambda:self.FbtnCadastrarAluno(self.inputRaAl.get(), self.inputNomeAluno.get())
        ).pack(pady=10)
        # ====== Btn aluno ======
        
        self.lblTitleRespostas = tk.Label(
            self.window,
            text="Cadastra Respostas",
            font=("Arial", 17)
        ).pack(pady=20)
        
        # ====== Ra aluno ======
        self.lblRaRes = tk.Label(
            self.window,
            text="Coloque RA:",
            font=("Arial", 10)
        ).pack()
        self.inputRaRes = tk.Entry(
            self.window,
            font=("Ariel", 15),
            width=20
        )
        self.inputRaRes.pack(pady=10)
        # ====== Ra aluno ======
        
        # ====== Resposta aluno ======
        self.lblResProva = tk.Label(
            self.window,
            text="Respostas da prova:",
            font=("Arial", 10)            
        ).pack()
        self.inputResProva = tk.Entry(
            self.window,
            font=("Arial", 15),
            width=20
        )
        self.inputResProva.pack(pady=10)
        # ====== Resposta aluno ======
        
        self.btnResProva = tk.Button(
            self.window,
            text="Cadastrar Respostas",
            font=("Arial", 15)
        ).pack(pady=15)
        
        self.lblTitleCorrecao = tk.Label(
            self.window,
            text="Corrigir Prova",
            font=("Arial",17)
        ).pack(pady=20)
        
        self.lblRaCor = tk.Label(
            self.window,
            text="Coloque seu Ra:",
            font=("Arial",10)
        ).pack()
        self.inputRaCor = tk.Entry(
            self.window,
            font=("Arial", 15),
            width=20
        )
        self.inputRaCor.pack()
        
        self.btnCorrigirProva = tk.Button(
            self.window,
            text="Corrigir prova",
            font=("Arial", 15)
        ).pack(pady=20)
                
        self.window.mainloop()
        
    def FbtnCadastrarAluno(self, ra, nomeAluno):
        if(ra == ""):
            messagebox.showwarning("Atenção!!","Preencha o campo de RA!")
        elif(nomeAluno == ""):
            messagebox.showwarning("Atenção!!","Preencha o campo de Nome do aluno!")

window()