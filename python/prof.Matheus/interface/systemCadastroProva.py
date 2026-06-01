import tkinter as tk
from tkinter import messagebox





# Classe principal da aplicação
class window:
    def __init__(self):
        # ================== CONFIGURAÇÃO DA JANELA ==================
        self.window = tk.Tk()
        self.window.geometry("800x800")   # Define tamanho da janela
        self.window.resizable(0,0)        # Bloqueia redimensionamento
        self.window.title("Cadastro e Correção de provas")  # Título

        # ================== TÍTULO PRINCIPAL ==================
        self.lblTitle = tk.Label(
            text="Cadastro Aluno",
            font=("Arial", 17)
        ).pack()

        # ================== CAMPO RA DO ALUNO ==================
        self.lblRaAl = tk.Label(
            text="Coloque seu RA:",
            font=("Arial", 10)
        ).pack()

        # Entrada para RA
        self.inputRaAl = tk.Entry(
            self.window,
            font=("Arial", 15),
            width=20
        )
        self.inputRaAl.pack(pady=10)

        # ================== CAMPO NOME DO ALUNO ==================
        self.lblNomeAluno = tk.Label(
            self.window,
            text="Coloque seu Nome:",
            font=("Arial", 10)
        ).pack()

        # Entrada para Nome
        self.inputNomeAluno = tk.Entry(
            self.window,
            font=("Arial", 15),
            width=20
        )
        self.inputNomeAluno.pack()

        # ================== BOTÃO CADASTRAR ALUNO ==================
        self.btnCadastrarAluno = tk.Button(
            self.window,
            text="Cadastrar aluno",
            font=("Arial", 15),

            # Quando clicar, chama a função passando valores digitados
            command=lambda:self.FbtnCadastrarAluno(
                self.inputRaAl.get(),
                self.inputNomeAluno.get()
            )
        ).pack(pady=10)

        # ================== SEÇÃO: CADASTRAR RESPOSTAS ==================
        self.lblTitleRespostas = tk.Label(
            self.window,
            text="Cadastra Respostas",
            font=("Arial", 17)
        ).pack(pady=20)

        # ====== RA para respostas ======
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

        # ====== CAMPO RESPOSTAS DA PROVA ======
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

        # Botão cadastrar respostas (sem função atribuída ainda)
        self.btnResProva = tk.Button(
            self.window,
            text="Cadastrar Respostas",
            font=("Arial", 15),
            command=lambda:self.FbtnCadastrarResposta()
        ).pack(pady=15)

        # ================== SEÇÃO: CORREÇÃO DE PROVA ==================
        self.lblTitleCorrecao = tk.Label(
            self.window,
            text="Corrigir Prova",
            font=("Arial",17)
        ).pack(pady=20)

        # ====== RA para correção ======
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

        # Botão corrigir prova (sem lógica ainda)
        self.btnCorrigirProva = tk.Button(
            self.window,
            text="Corrigir prova",
            font=("Arial", 15)
        ).pack(pady=20)

        # Executa a aplicação (loop da interface)
        self.window.mainloop()


    # ================== FUNÇÃO CADASTRAR ALUNO ==================
    def FbtnCadastrarAluno(self, ra, nomeAluno):
        if(ra == ""):
            messagebox.showwarning("Atenção!!","Preencha o campo de RA!")
        elif(nomeAluno == ""):
            messagebox.showwarning("Atenção!!","Preencha o campo de Nome do aluno!")
            
    def FbtnCadastrarResposta(self):
        janela = tk.Tk()
        janela.geometry("800X800")
        janela.resizable(0,0)
        
        btn = tk.Button(
            janela,
            font=("Arial",17),
            text="Fechar"
        ).pack()
        
        
        
        
        janela.mainloop()
        

# ================== INICIAR SISTEMA ==================
window()