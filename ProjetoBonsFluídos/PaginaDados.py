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
def Doacao():
	print(" doação")
def Estoque():
	print("estoque")
def Beneficiarios():
	print("beneficiario")
def Voltar():
	print(" voltouuu")

#Criando Tela
tela = tk.Tk()

tela.title("Dados")
tela.geometry("700x400")

#Criando Frames
Botao_frame = tk.Frame(tela)

#Colocando frames à tela
Botao_frame.pack(pady=50)

#Criando botão (Button)
Inserir_button = tk.Button(Botao_frame, text="Doações", command=Doacao, font=fonte)
Deletar_button = tk.Button(Botao_frame, text="Estoques", command=Estoque, font=fonte)
AlterarUsuario_button = tk.Button(Botao_frame, text="Beneficiários", command=Beneficiarios, font=fonte)
Voltar_button = tk.Button(Botao_frame, text="Voltar", command=Voltar, font=fonte)

#Colocando elementos à tela
Inserir_button.pack(pady=20)
Deletar_button.pack(pady=20)
AlterarUsuario_button.pack(pady=20)
Voltar_button.pack(pady=20)

tela.mainloop()