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
def Tela_doacao():
	print("entrou Tela_doacao")
def Tela_estoque():
	print("entrou Tela_estoque")
def Tela_relatorio():
	print("entrou Tela_relatorio")
def Tela_distribuicao():
	print("entrou Tela_distribuicao")
def Tela_sair():
	print("entrou Tela_sair")

#Criando Tela
tela = tk.Tk()

tela.title("Colaborador")
tela.geometry("700x450")

#Criando Frames
Botao_frame = tk.Frame(tela)

#Colocando frames à tela
Botao_frame.pack(pady=50)

#Criando botão (Button)
Doacao_button = tk.Button(Botao_frame, text="Doação", command=Tela_doacao, font=fonte)
Estoque_button = tk.Button(Botao_frame, text="Estoque", command=Tela_estoque, font=fonte)
Relatorio_button = tk.Button(Botao_frame, text="Relatório", command=Tela_relatorio, font=fonte)
Distribuicao_button = tk.Button(Botao_frame, text="Distribuição", command=Tela_distribuicao, font=fonte)
Sair_button = tk.Button(Botao_frame, text="Sair", command=Tela_sair, font=fonte)

#Colocando elementos à tela
Doacao_button.pack(pady=20)
Estoque_button.pack()
Relatorio_button.pack(pady=20)
Distribuicao_button.pack()
Sair_button.pack()

tela.mainloop()