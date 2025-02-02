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
def Notificacao():
	print("Notificação")
def Voltar():
	print(" voltouuu")

#Criando Tela
tela = tk.Tk()

tela.title("Configurações")
tela.geometry("700x400")

#Criando Frames
Botao_frame = tk.Frame(tela)

#Colocando frames à tela
Botao_frame.pack(pady=50)

#Criando botão (Button)
Notificacao_button = tk.Button(Botao_frame, text="Notificação", command=Notificacao, font=fonte)
Voltar_button = tk.Button(Botao_frame, text="Voltar", command=Voltar, font=fonte)

#Colocando elementos à tela
Notificacao_button.pack(pady=20)
Voltar_button.pack(pady=20)

tela.mainloop()