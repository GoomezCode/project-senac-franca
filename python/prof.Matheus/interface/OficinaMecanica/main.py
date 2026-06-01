import tkinter as tk
from tkinter import messagebox

dataBase = [] # {"101": "Trocar o Óleo"}



class window_main:
    def __init__(self):
        self.janela = tk.Tk()
        self.janela.geometry("400x250")
        self.janela.title("Sistem O.S")
        self.janela.resizable(0,0)
        
        titulo = tk.Label(
            self.janela,
            text="Sistema O.S.",
            font=("Arial", 20)
        ).pack(pady=20)
        
        
        
        btnCadastro = tk.Button(
            self.janela,
            text="Criar Nova O.S",
            font=("Arial", 15),
            command=lambda:windowCadastro()
        ).pack(pady=10)
        
        btnConsultar = tk.Button(
            self.janela,
            text="Consultar O.S",
            font=("Arial", 15),
            command=lambda:windowConsulta()
        ).pack(pady=10)
        
        self.janela.mainloop()


class windowCadastro:
    def __init__(self):
        self.janela = tk.Tk()
        self.janela.grab_set()
        self.janela.geometry("580x300")
        self.janela.resizable(0,0)
        self.janela.title("Criar Nova O.S")
        
        self.titulo = tk.Label(
            self.janela,
            text="Criar Nova O.S",
            font=("Arial", 20)
        ).pack()
        
        
        self.txtNumOs = tk.Label(
            self.janela,
            text="digitar o Número da O.S. (Ex: 101):",
            font=("Arial", 15)
        ).pack()
        self.numOs = tk.Entry(
            self.janela,
            font=("Arial", 15),
            width=10
        )
        self.numOs.pack()
        
        
        self.txtDescOS = tk.Label(
            self.janela,
            text="\ndigitar a Descrição do Serviço\n(Ex: Trocar o óleo e alinhar as rodas):",
            font=("Arial", 15)
        ).pack()
        self.descOS = tk.Entry(
            self.janela,
            font=("Arial", 15),
            width=40
        )
        self.descOS.pack()

        
        self.btnConfirm = tk.Button(
            self.janela,
            text="Confirmar",
            font=("Arial", 17),
            command=lambda:self.actionBtn(self.numOs.get(), self.descOS.get())
        ).pack()
        
        self.janela.mainloop()
        
    def actionBtn(self, numOS, descOS):
        if(numOS==""):
            messagebox.showerror("ERROR", "O Campo Numero O.S está vazio!!")
        elif(descOS==""):
            messagebox.showerror("ERROR", "O Campo Descrição O.S está vazio!!")
        else:
            dataBase.append({numOS:descOS})
            messagebox.showinfo("Sucesso", "O.S cadastrada!")
            
class windowConsulta:
    def __init__(self):
        self.janela = tk.Tk()
        self.janela.grab_set()
        self.janela.geometry("580x300")
        self.janela.resizable(0,0)
        self.janela.title("Consultar O.S")
        
        self.titulo = tk.Label(
            self.janela,
            text="Consultar O.S",
            font=("Arial", 20)
        ).pack()
        
        self.txtNumOs = tk.Label(
            self.janela,
            text="digitar o Número da O.S. (Ex: 101):",
            font=("Arial", 15)
        ).pack()
        self.numOs = tk.Entry(
            self.janela,
            font=("Arial", 15),
            width=10
        )
        self.numOs.pack()
        
        
        self.btnBuscar = tk.Button(
            self.janela,
            text="Buscar",
            font=("Arial", 17),
            command=lambda:self.actionBtn(self.numOs.get())
        ).pack()
                
        self.janela.mainloop()
    def actionBtn(self, numOS):
        if numOS=="":
            messagebox.showerror("Error", "O Campo está vazio!")
        else:
            for i in dataBase:
                messagebox.showinfo("Sucesso!",i[numOS])
window_main()