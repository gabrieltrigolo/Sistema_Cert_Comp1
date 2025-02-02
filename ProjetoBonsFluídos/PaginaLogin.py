#Importando biblioteca Tkinter 
import tkinter as tk

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
	__nome = Nome_entry.get()
	__senha = Senha_entry.get()
	print(__nome+" entrou")

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