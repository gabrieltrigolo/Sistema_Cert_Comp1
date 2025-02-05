#Importando biblioteca Tkinter
import tkinter as tk

from PaginaUsuario import PaginaUsuario


class PaginaADM:
	def __init__(self):
		# Configurações iniciais
		self.fonte = ("Arial", 12)
		self.conf_Button = {
			"width": 5,
			"height": 1,
			"padx": 10,
			"pady": 5
		}

		# Criando a janela principal
		self.tela = tk.Tk()
		self.tela.title("Adm")
		self.tela.geometry("700x450")

		# Criando Frame
		self.Botao_frame = tk.Frame(self.tela)
		self.Botao_frame.pack(pady=50)

		# Criando botões
		self.criar_botoes()

	def criar_botoes(self):
		# Lista de tuplas com (texto, comando)
		botoes = [
			("Usuários", self.Tela_usuarios),
			("Dados", self.Tela_dados),
			("Relatório", self.Tela_relatorio),
			("Histórico", self.Tela_historico),
			("Configurações", self.Tela_configuracoes),
			("Sair", self.Tela_sair)
		]

		# Criando e posicionando os botões
		for i, (texto, comando) in enumerate(botoes):
			botao = tk.Button(
				self.Botao_frame,
				text=texto,
				command=comando,
				font=self.fonte
			)
			# Adiciona pady=20 para botões alternados
			botao.pack(pady=20 if i % 2 == 0 else 0)

	def Tela_usuarios(self):
		tela_usuario = PaginaUsuario()
		tela_usuario.tela.mainloop()

	def Tela_dados(self):
		print("entrou Tela_Dados")

	def Tela_relatorio(self):
		print("entrou Tela_relatorio")

	def Tela_historico(self):
		print("entrou Tela_historico")

	def Tela_configuracoes(self):
		print("entrou Tela_configuracoes")

	def Tela_sair(self):
		print("entrou Tela_sair")

# Executar a aplicação
if __name__ == "__main__":
    app = PaginaADM()
    tk.mainloop()