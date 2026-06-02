import tkinter as tk
from tkinter import messagebox

class main:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Login User")
        self.window.resizable(0,0)
        self.window.geometry("500x300")
        
        self.h1 = tk.Label(
            self.window,
            text="Login User",
            font=("Arial", 17)
        ).pack()
        
        self.h3 = tk.Label(
            self.window,
            text="Insira seu Gmail:",
            font=("Arial", 15)
        ).pack(pady=10)
        self.inputName = tk.Entry(
            self.window,
            font=("Arial", 13),
            width=30
        )
        self.inputName.pack()
        
        self.h3 = tk.Label(
            self.window,
            text="Insira seu password:",
            font=("Arial", 15)
        ).pack(pady=10)
        self.inputPassword = tk.Entry(
            self.window,
            font=("Arial", 13),
            width=30
        )
        self.inputPassword.pack()
        
        
        self.btnEnter = tk.Button(
            self.window,
            text="Confirmar",
            font=("Arial", 15),
            width=20,
            command=lambda:self.windowForm(self.inputName.get(), self.inputPassword.get())
        ).pack()
        
        self.window.mainloop()
        
    def windowForm(self, gmail, password):
        if gmail == "": return messagebox.showerror("Error!","Insira algo no campo Gmail!")
        if password == "": return messagebox.showerror("Error!","Insira algo no campo Password!")
        
        self.painelForm = tk.Tk()
        self.painelForm.title("Painel Form")
        self.painelForm.geometry("500x500")
        self.painelForm.resizable(0,0)
        
        self.barraMenu = tk.Menu(self.painelForm)
        self.painelForm.config(menu=self.barraMenu)
        
        self.cascataUser = tk.Menu(self.barraMenu,tearoff=0)
        
        self.barraMenu.add_cascade(
            label="User",
            menu=self.cascataUser
        )
        self.cascataUser.add_command(
            label="Gmail",
            command=lambda:print(gmail)
        )
        self.cascataUser.add_command(
            label="Password",
            command=lambda:print(password)
        )
        
        if gmail == "admin" and password == "123":
            self.cascataAdmin = tk.Menu(self.barraMenu, tearoff=0)
            self.barraMenu.add_cascade(
                label="Admin",
                menu=self.cascataAdmin
            )
            
            self.cascataAdmin.add_command(
            label="Gmail",
            command=lambda:print(gmail)
            )
            self.cascataAdmin.add_command(
                label="Password",
                command=lambda:print(password)
            )
        
        self.painelForm.mainloop()
        
main()