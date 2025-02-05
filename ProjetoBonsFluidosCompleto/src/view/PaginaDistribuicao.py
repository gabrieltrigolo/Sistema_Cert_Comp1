# Importando biblioteca Tkinter
import tkinter as tk
from tkinter import ttk, messagebox

from src.dao.DistribuicaoDAO import DistribuicaoDAO
from src.view.PaginaInserirDistribuicao import PaginaInserirDistribuicao
from src.view.PaginaDeletarDistribuicao import PaginaDeletarDistribuicao


class PaginaDistribuicao:
    def __init__(self, master):
        # Configurações iniciais
        self.fonte = ("Arial", 12)

        # Criando a janela principal
        self.master = master
        self.tela = tk.Tk()
        self.tela.title("Beneficiário")
        self.tela.geometry("700x400")

        # Criando Frame para a tabela
        self.Tabela_frame = tk.Frame(self.tela)
        self.Tabela_frame.pack(pady=10)

        # Adicionando título para a tabela
        self.titulo_tabela = tk.Label(self.Tabela_frame, text="Tabela de Distribuições", font=("Arial", 14))
        self.titulo_tabela.pack(pady=5)

        # Criando a tabela
        self.criar_tabela()

        # Criando Frame para os botões
        self.Botao_frame = tk.Frame(self.tela)
        self.Botao_frame.pack(side=tk.BOTTOM, pady=20)

        # Criando botões
        self.criar_botoes()

    def criar_tabela(self):
        columns = ("Distribuição ID", "Nome Beneficiario", "Quantidade", "Data")
        self.tree = ttk.Treeview(self.Tabela_frame, columns=columns, show="headings")

        # Definindo os títulos das colunas
        for col in columns:
            self.tree.heading(col, text=col)

        # Definindo o tamanho das colunas
        self.tree.column("Distribuição ID", width=150)
        self.tree.column("Nome Beneficiario", width=200)
        self.tree.column("Quantidade", width=200)
        self.tree.column("Data", width=200)

        self.atualizar_tabela()

        # Posicionando a tabela na janela
        self.tree.pack(expand=True, fill="both")

    def atualizar_tabela(self):
        for item in self.tree.get_children():
            self.tree.delete(item)

        dao = DistribuicaoDAO()
        distribuicoes = dao.buscarTodasDistribuicoes()
        for distribuicao in distribuicoes:
            campos_filtrados = (
                distribuicao[0],  # Distribuição ID
                distribuicao[1],  # Beneficiario NOME
                distribuicao[7],  # Quantidade
                distribuicao[6]  # Data
            )
            self.tree.insert("", tk.END, values=campos_filtrados)

    def criar_botoes(self):
        # Lista de tuplas com (texto, comando)
        botoes = [
            ("Inserir Distribuição", self.Inserir_distribuicao),
            ("Deletar Distribuição", self.Deletar_distribuicao),
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

    def Inserir_distribuicao(self):
        print("entrou Inserir Usuários")
        tela_inserirdistribuicao = PaginaInserirDistribuicao()
        tela_inserirdistribuicao.tela.mainloop()

    def Deletar_distribuicao(self):
        print("entrou Inserir Usuários")
        tela_deletardistribuicao = PaginaDeletarDistribuicao()
        tela_deletardistribuicao.tela.mainloop()

    def Voltar(self):
        self.tela.destroy()
        self.master.deiconify()  # Reexibe a tela ADM


