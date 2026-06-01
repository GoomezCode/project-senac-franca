import tkinter as tk
from tkinter import messagebox

class main:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Menu")
        self.window.resizable(0,0)
        self.window.geometry("500x500")
        
        self.barraMenu = tk.Menu(self.window)
        self.window.config(menu=self.barraMenu)
        
        self.cascataArquivo = tk.Menu(self.barraMenu, tearoff=0)
     
        self.barraMenu.add_cascade(
            label="Arquivo",
            menu=self.cascataArquivo
        )
        
        self.cascataArquivo.add_command(
            label="Add",
            command=lambda:print("Add arquivo")
        )

        
        
        self.window.mainloop()


main()