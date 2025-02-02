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
def Tela_usuarios():
	print("entrou Tela_Usuarios")
def Tela_dados():
	print("entrou Tela_Dados")
def Tela_relatorio():
	print("entrou Tela_relatorio")
def Tela_historico():
	print("entrou Tela_historico")
def Tela_configuracoes():
	print("entrou Tela_configuracoes")
def Tela_sair():
	print("entrou Tela_sair")

#Criando Tela
tela = tk.Tk()

tela.title("Adm")
tela.geometry("700x450")

#Criando Frames
Botao_frame = tk.Frame(tela)

#Colocando frames à tela
Botao_frame.pack(pady=50)

#Criando botão (Button)
Usuarios_button = tk.Button(Botao_frame, text="Usurários", command=Tela_usuarios, font=fonte)
Dados_button = tk.Button(Botao_frame, text="Dados", command=Tela_dados, font=fonte)
Relatorio_button = tk.Button(Botao_frame, text="Relatório", command=Tela_relatorio, font=fonte)
Historico_button = tk.Button(Botao_frame, text="Histórico", command=Tela_historico, font=fonte)
Configuracoes_button = tk.Button(Botao_frame, text="Configurações", command=Tela_configuracoes, font=fonte)
Sair_button = tk.Button(Botao_frame, text="Sair", command=Tela_sair, font=fonte)

#Colocando elementos à tela
Usuarios_button.pack(pady=20)
Dados_button.pack()
Relatorio_button.pack(pady=20)
Historico_button.pack()
Configuracoes_button.pack(pady=20)
Sair_button.pack()

tela.mainloop()