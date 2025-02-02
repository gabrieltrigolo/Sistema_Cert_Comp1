#Importando biblioteca Tkinter 
import tkinter as tk

#Criando dicionário de fontes e configs
fonte = {
	("Arial", 12)
}
conf_Button = {
	"width":5,
	"height":1,
	"padx":10,
	"pady":5
}

#Função quando botão for pressionado
def Inserir_usuario():
	print(" entrou")
def Deletar_usuario():
	print(" deletou")
def Alterar_usuario():
	print(" alterou usuario")
def Alterar_permissoes():
	print(" alterou permissoes")
def Voltar():
	print(" voltouuu")

#Criando Tela
tela = tk.Tk()

tela.title("Usuário")
tela.geometry("700x400")

#Criando Frames
Botao_frame = tk.Frame(tela)

#Colocando frames à tela
Botao_frame.pack(pady=50)

#Criando botão (Button)
Inserir_button = tk.Button(Botao_frame, text="Inserir Usurários", command=Inserir_usuario, font=fonte)
Deletar_button = tk.Button(Botao_frame, text="Deletar Usurários", command=Deletar_usuario, font=fonte)
AlterarUsuario_button = tk.Button(Botao_frame, text="Alterar Usurários", command=Alterar_usuario, font=fonte)
AlterarPermissoes_button = tk.Button(Botao_frame, text="Alterar Permissoes", command=Alterar_permissoes, font=fonte)
Voltar_button = tk.Button(Botao_frame, text="Voltar", command=Voltar, font=fonte)

#Colocando elementos à tela
Inserir_button.pack(pady=20)
Deletar_button.pack()
AlterarUsuario_button.pack(pady=20)
AlterarPermissoes_button.pack()
Voltar_button.pack(pady=20)

tela.mainloop()