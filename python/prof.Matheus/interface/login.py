import tkinter as tk
from tkinter import messagebox

# Dados simulados (em memória)
usuarios = {}


def mostrar_login():
    frame_cadastro.pack_forget()
    frame_login.pack(expand=True)


def mostrar_cadastro():
    frame_login.pack_forget()
    frame_cadastro.pack(expand=True)


def fazer_login():
    usuario = entry_login_usuario.get()
    senha = entry_login_senha.get()

    if usuario in usuarios and usuarios[usuario]["senha"] == senha:
        messagebox.showinfo("Sucesso", f"Bem-vindo, {usuario}!")
    else:
        messagebox.showerror("Erro", "Usuário ou senha inválidos!")


def registrar():
    nome = entry_nome.get()
    data = entry_data.get()
    email = entry_email.get()
    senha = entry_senha.get()

    if not (nome and data and email and senha):
        messagebox.showwarning("Erro", "Preencha todos os campos!")
        return

    if nome in usuarios:
        messagebox.showerror("Erro", "Usuário já existe!")
        return

    usuarios[nome] = {
        "data": data,
        "email": email,
        "senha": senha
    }

    messagebox.showinfo("Sucesso", "Cadastro realizado!")
    limpar_campos()
    mostrar_login()


def limpar_campos():
    entry_nome.delete(0, tk.END)
    entry_data.delete(0, tk.END)
    entry_email.delete(0, tk.END)
    entry_senha.delete(0, tk.END)


# Janela principal
janela = tk.Tk()
janela.title("Sistema Login + Cadastro")
janela.geometry("350x300")
janela.resizable(False, False)

# ================= LOGIN =================
frame_login = tk.Frame(janela)

tk.Label(frame_login, text="Login", font=("Arial", 16)).pack(pady=10)

tk.Label(frame_login, text="Usuário:").pack()
entry_login_usuario = tk.Entry(frame_login)
entry_login_usuario.pack()

tk.Label(frame_login, text="Senha:").pack()
entry_login_senha = tk.Entry(frame_login, show="*")
entry_login_senha.pack()

tk.Button(frame_login, text="Entrar", command=fazer_login).pack(pady=10)
tk.Button(frame_login, text="Criar conta", command=mostrar_cadastro).pack()

# ================= CADASTRO =================
frame_cadastro = tk.Frame(janela)

tk.Label(frame_cadastro, text="Cadastro", font=("Arial", 16)).pack(pady=10)

tk.Label(frame_cadastro, text="Nome:").pack()
entry_nome = tk.Entry(frame_cadastro)
entry_nome.pack()

tk.Label(frame_cadastro, text="Data Nascimento:").pack()
entry_data = tk.Entry(frame_cadastro)
entry_data.pack()

tk.Label(frame_cadastro, text="Email:").pack()
entry_email = tk.Entry(frame_cadastro)
entry_email.pack()

tk.Label(frame_cadastro, text="Senha:").pack()
entry_senha = tk.Entry(frame_cadastro, show="*")
entry_senha.pack()

tk.Button(frame_cadastro, text="Registrar", command=registrar).pack(pady=10)
tk.Button(frame_cadastro, text="Voltar ao login", command=mostrar_login).pack()

# Iniciar com login
frame_login.pack(expand=True)

janela.mainloop()