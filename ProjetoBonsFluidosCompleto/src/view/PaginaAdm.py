#Importando biblioteca Tkinter
import tkinter as tk

from src.view.PaginaBeneficiario import PaginaBeneficiario
from src.view.PaginaDistribuicao import PaginaDistribuicao
from src.view.PaginaDoacoes import PaginaDoacoes
from src.view.PaginaInserirDoacoes import PaginaInserirDoacoes
from src.view.PaginaRelatorio import PaginaRelatorio
from src.view.PaginaUsuario import PaginaUsuario


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
		# Definir o tamanho da janela
		largura_janela = 700
		altura_janela = 450
		# Obter o tamanho da tela
		largura_tela = self.tela.winfo_screenwidth()
		altura_tela = self.tela.winfo_screenheight()
		# Calcular a posição x e y para centralizar a janela
		pos_x = (largura_tela - largura_janela) // 2
		pos_y = (altura_tela - altura_janela) // 2
		# Definir a geometria da janela
		self.tela.geometry(f"{largura_janela}x{altura_janela}+{pos_x}+{pos_y}")

		# Criando Frame
		self.Botao_frame = tk.Frame(self.tela)
		self.Botao_frame.pack(pady=50)

		# Criando botões
		self.criar_botoes()

	def criar_botoes(self):
		# Lista de tuplas com (texto, comando)
		botoes = [
			("Usuários", self.Tela_usuarios),
			("Beneficiarios", self.Tela_beneficiarios),
			("Doações", self.Tela_doacoes),
			("Distribuição", self.Tela_distribuicao),
			("Relatórios", self.Tela_relatorios),
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
		self.tela.withdraw()  # Oculta a tela ADM
		self.tela_inserirusuario = PaginaUsuario(self.tela)

	def Tela_beneficiarios(self):
		self.tela.withdraw()  # Oculta a tela ADM
		self.tela_beneficiario = PaginaBeneficiario(self.tela)

	def Tela_doacoes(self):
		self.tela.withdraw()  # Oculta a tela ADM
		self.tela_doacoes = PaginaDoacoes(self.tela)

	def Tela_distribuicao(self):
		self.tela.withdraw()  # Oculta a tela ADM
		self.tela_distribuicao = PaginaDistribuicao(self.tela)

	def Tela_relatorios(self):
		nova_janela = tk.Toplevel()  # Cria uma nova janela em vez de uma nova instância do Tk
		tela_relatorio = PaginaRelatorio(nova_janela)  # Passa a nova janela como root

	def Tela_sair(self):
		self.tela.destroy()

