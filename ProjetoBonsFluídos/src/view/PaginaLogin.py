#Importando biblioteca Tkinter 
import tkinter as tk
from tkinter import messagebox

from PaginaAdm import PaginaADM
from src.dao.UsuarioDAO import UsuarioDAO

#Criando dicionário de fontes e configs
fonte = {
	("Arial", 12)
}
conf_Label = {
	"width":20,
	"height":2,
	"padx":10,
	"pady":10
}
conf_Entry = {
	"width":40
}
conf_Button = {
	"width":5,
	"height":1,
	"padx":10,
	"pady":5
}

#Função quando botão for pressionado
def entrar():
	email = Nome_entry.get()  # Assumindo que Nome_entry é para o email
	senha = Senha_entry.get()

	usuario_dao = UsuarioDAO()
	login_sucesso = usuario_dao.verificarLogin(email, senha)

	if login_sucesso:
		print(f"Bem-vindo, {email}!")
		tela_adm = PaginaADM()
		tela_adm.tela.mainloop()
	else:
		# Caso queira mostrar uma mensagem de erro em uma janela
		messagebox.showerror("Erro de Login", "Email ou senha incorretos!")

#Criando Tela
tela = tk.Tk()

tela.title("Login")
tela.geometry("700x400")

#Criando Frames
Nome_frame = tk.Frame(tela)
Senha_frame = tk.Frame(tela)
Botao_frame = tk.Frame(tela)

#Colocando frames à tela
Nome_frame.pack(pady=50)
Senha_frame.pack()
Botao_frame.pack(pady=50)

#Criando rótulos (Labels)
Nome_label = tk.Label(Nome_frame, text="Nome: ", font=fonte, **conf_Label)
Senha_label = tk.Label(Senha_frame, text="Senha: ", font=fonte, **conf_Label)
#Criando entrada de texto (Entry)
Nome_entry = tk.Entry(Nome_frame, font=fonte, **conf_Entry)
Senha_entry = tk.Entry(Senha_frame, show="*", font=fonte, **conf_Entry)
#Criando botão (Button)
Entrar_button = tk.Button(Botao_frame, text="Entrar", command=entrar, font=fonte)

#Colocando elementos à tela
Nome_label.pack()
Nome_entry.pack()
Senha_label.pack()
Senha_entry.pack()
Entrar_button.pack()

tela.mainloop()