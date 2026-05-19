import tkinter as tk
from tkinter import messagebox

class window:
    def __init__(self):
        self.listaNomes = []
        self.janela = tk.Tk()
        self.janela.title("My first window")
        self.janela.geometry("700x700")
        self.janela.resizable(0,0)
        # self.janela.resizable(400,400)
        
        self.lbltext = tk.Label(
            self.janela,
            text="provide your name: ",
            font=("Arial",14),
            fg="red"
        )
        self.lbltext.pack()
        
        self.inputName = tk.Entry(
            self.janela,
            background="black",
            fg="white",
            font=("Arial", 14),
            width=30
        )
        self.inputName.pack()
        
        self.btnTeste = tk.Button(
            self.janela,
            text="Apenas teste",
            font=("Arial", 17),
            bg="blue",
            border=None,
            command=lambda:self.salvarNome(self.inputName.get())
        )
        self.btnTeste.pack()
        
        self.btnRemover = tk.Button(
            text="Remover",
            font=("Arial", 15),
            fg="White",
            bg="Red",
            command=lambda:self.deletarNome(self.inputName.get())
        ).pack(pady=10)
        
        self.janela.mainloop()
    def salvarNome(self,nome):        
        self.listaNomes.append(nome)
        messagebox.showinfo("Sucesso!","Cadastrado!!")
    def deletarNome(self,nome):
        self.listaNomes.remove(nome)
        



class windowCalc():
    def __init__(self):
        self.window = tk.Tk()
        self.window.geometry("400x400")
        self.window.title("Calculadora basica")
        self.window.resizable(0,0)
        
        self.lblTitle = tk.Label(
            self.window,
            text="Calculadora muitooo basica",
            fg="Black",
            font=("Arial", 15)
        ).pack()
        
        
        self.inputNumber1 = tk.Entry(
            self.window,
            font=("Arial", 17),
            bg="Gray",
            width=20
        )
        self.inputNumber1.pack(padx=10)
        
        
        self.inputNumber2 = tk.Entry(
            self.window,
            font=("Arial", 17),
            bg="Gray",
            width=20
        )
        self.inputNumber2.pack(pady=10)
        
        self.btnCalcular = tk.Button(
            self.window,
            text="Calcular....",
            font=("Arial", 15),
            width=30,
            command=lambda:self.calcular(self.inputNumber1.get(), self.inputNumber2.get())
        ).pack(pady=10)
        
        self.window.mainloop()
    def calcular(self, num1, num2):
        operacao = "soma"
        soma = int(num1)+int(num2)
        self.lblresutado = tk.Label(
            text=f"{num1} + {num2} = {soma}",
            font=("Arial", 20),
            fg="Green"
        )
        self.lblresutado.pack(pady=20)
        
window()