# Importando biblioteca Tkinter
import tkinter as tk
from tkinter import ttk, messagebox

from src.dao.DoacaoDAO import DoacaoDAO  # Atualizar para o DAO correto
from src.view.PaginaDeletarDoacao import PaginaDeletarDoacao
from src.view.PaginaInserirDoacoes import PaginaInserirDoacoes  # Atualizar para a página correta

class PaginaDoacoes:
    def __init__(self):
        # Configurações iniciais
        self.fonte = ("Arial", 12)

        # Criando a janela principal
        self.tela = tk.Tk()
        self.tela.title("Gerenciar Doações")
        self.tela.geometry("900x400")

        # Criando Frame para a tabela
        self.Tabela_frame = tk.Frame(self.tela)
        self.Tabela_frame.pack(pady=10)

        # Adicionando título para a tabela
        self.titulo_tabela = tk.Label(self.Tabela_frame, text="Tabela de Doações", font=("Arial", 14))
        self.titulo_tabela.pack(pady=5)

        # Criando a tabela
        self.criar_tabela()

        # Criando Frame para os botões
        self.Botao_frame = tk.Frame(self.tela)
        self.Botao_frame.pack(side=tk.BOTTOM, pady=20)

        # Criando botões
        self.criar_botoes()

    def criar_tabela(self):
        columns = ("Doação ID", "Nome do Produto", "Doador", "Quantidade", "Data da Doação")
        self.tree = ttk.Treeview(self.Tabela_frame, columns=columns, show="headings")

        # Definindo os títulos das colunas
        for col in columns:
            self.tree.heading(col, text=col)

        # Definindo o tamanho das colunas
        self.tree.column("Doação ID", width=150)
        self.tree.column("Nome do Produto", width=150)
        self.tree.column("Doador", width=200)
        self.tree.column("Quantidade", width=150)
        self.tree.column("Data da Doação", width=150)

        self.atualizar_tabela()

        # Posicionando a tabela na janela
        self.tree.pack(expand=True, fill="both")

    def atualizar_tabela(self):
        for item in self.tree.get_children():
            self.tree.delete(item)

        dao = DoacaoDAO()  # Usar o DAO correto para buscar doações
        doacoes = dao.listarTodasDoacoes()
        for doacao in doacoes:
            campos_filtrados = (
                doacao[0],  # Doação ID
                doacao[6],  # Produto ID
                doacao[4],  # Doador
                doacao[3],  # Quantidade
                doacao[2]   # Data da Doação
            )
            self.tree.insert("", tk.END, values=campos_filtrados)

    def criar_botoes(self):
        # Lista de tuplas com (texto, comando)
        botoes = [
            ("Inserir Doação", self.Inserir_doacao),
            ("Deletar Doação", self.Deletar_doacao),
            ("Voltar", self.Voltar)
        ]

        # Criando e posicionando os botões lado a lado
        for texto, comando in botoes:
            botao = tk.Button(
                self.Botao_frame,
                text=texto,
                command=comando,
                font=self.fonte,
                padx=10,
                pady=5
            )
            botao.pack(side=tk.LEFT, padx=10)  # Posiciona os botões lado a lado

    def Inserir_doacao(self):
        tela_inserir_doacao = PaginaInserirDoacoes()  # Atualizar para a página correta de inserção de doações
        tela_inserir_doacao.tela.mainloop()

    def Deletar_doacao(self):
        tela_deletar_doacao = PaginaDeletarDoacao()  # Atualizar para a página correta de deleção de doações
        tela_deletar_doacao.tela.mainloop()

    def Voltar(self):
        self.tela.destroy()


