import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime

from src.dao.RelatorioDAO import RelatorioDAO


class PaginaRelatorio:
    def __init__(self, root):
        self.root = root
        self.root.title("Relatórios de Estoque")
        # Definir o tamanho da janela
        largura_janela = 700
        altura_janela = 500
        # Obter o tamanho da tela
        largura_tela = self.root.winfo_screenwidth()
        altura_tela = self.root.winfo_screenheight()
        # Calcular a posição x e y para centralizar a janela
        pos_x = (largura_tela - largura_janela) // 2
        pos_y = (altura_tela - altura_janela) // 2
        # Definir a geometria da janela
        self.root.geometry(f"{largura_janela}x{altura_janela}+{pos_x}+{pos_y}")
        self.dao = RelatorioDAO()

        # Abas para cada relatório
        self.tab_control = ttk.Notebook(root)

        self.tab_distribuicoes = ttk.Frame(self.tab_control)
        self.tab_doacoes_por_doador = ttk.Frame(self.tab_control)
        self.tab_beneficiarios = ttk.Frame(self.tab_control)

        self.tab_control.add(self.tab_distribuicoes, text='Distribuições por Mês')
        self.tab_control.add(self.tab_doacoes_por_doador, text='Doações por Doador')
        self.tab_control.add(self.tab_beneficiarios, text='Top Beneficiários')

        self.tab_control.pack(expand=1, fill='both')

        self.criar_distribuicoes_por_mes()
        self.criar_doacoes_por_doador()
        self.criar_top_beneficiarios()

        # Botão de Voltar
        tk.Button(root, text="Voltar", command=root.destroy).pack(pady=10)

    def criar_distribuicoes_por_mes(self):
        tk.Label(self.tab_distribuicoes, text="Distribuições realizadas em um mês e ano específicos",
                 font=("Arial", 12, "bold")).pack(pady=5)

        tk.Label(self.tab_distribuicoes, text="Mês (1-12):").pack(pady=2)
        self.mes_entry = tk.Entry(self.tab_distribuicoes)
        self.mes_entry.pack(pady=2)

        tk.Label(self.tab_distribuicoes, text="Ano:").pack(pady=2)
        self.ano_entry = tk.Entry(self.tab_distribuicoes)
        self.ano_entry.pack(pady=2)

        tk.Button(self.tab_distribuicoes, text="Buscar", command=self.buscar_distribuicoes).pack(pady=5)

        self.tree_distribuicoes = ttk.Treeview(self.tab_distribuicoes,
                                               columns=("Data", "Beneficiário", "Produto", "Quantidade"),
                                               show="headings")
        for col in self.tree_distribuicoes["columns"]:
            self.tree_distribuicoes.heading(col, text=col)
        self.tree_distribuicoes.pack(fill='both', expand=True, pady=5)

    def buscar_distribuicoes(self):
        mes = self.mes_entry.get()
        ano = self.ano_entry.get()

        if not (mes.isdigit() and ano.isdigit()):
            messagebox.showerror("Erro", "Mês e Ano devem ser números.")
            return

        try:
            resultados = self.dao.distribuicoes_por_mes(int(mes), int(ano))
            self.tree_distribuicoes.delete(*self.tree_distribuicoes.get_children())
            for row in resultados:
                self.tree_distribuicoes.insert("", "end", values=(
                row["data_distribuicao"], row["beneficiario"], row["produto"], row["quantidade"]))
        except Exception as e:
            messagebox.showerror("Erro", str(e))

    def criar_doacoes_por_doador(self):
        tk.Label(self.tab_doacoes_por_doador, text="Total de doações feitas por cada doador",
                 font=("Arial", 12, "bold")).pack(pady=5)

        tk.Button(self.tab_doacoes_por_doador, text="Buscar Doações por Doador",
                  command=self.buscar_doacoes_por_doador).pack(pady=5)

        self.tree_doacoes_por_doador = ttk.Treeview(self.tab_doacoes_por_doador, columns=("Doador", "Total Doações"),
                                                    show="headings")
        for col in self.tree_doacoes_por_doador["columns"]:
            self.tree_doacoes_por_doador.heading(col, text=col)
        self.tree_doacoes_por_doador.pack(fill='both', expand=True, pady=5)

    def buscar_doacoes_por_doador(self):
        try:
            resultados = self.dao.doacoes_por_doador()
            self.tree_doacoes_por_doador.delete(*self.tree_doacoes_por_doador.get_children())
            for row in resultados:
                self.tree_doacoes_por_doador.insert("", "end", values=(row["doador"], row["total_doacoes"]))
        except Exception as e:
            messagebox.showerror("Erro", str(e))

    def criar_top_beneficiarios(self):
        tk.Label(self.tab_beneficiarios, text="Top 10 beneficiários que mais receberam produtos",
                 font=("Arial", 12, "bold")).pack(pady=5)

        tk.Button(self.tab_beneficiarios, text="Buscar Top Beneficiários", command=self.buscar_beneficiarios).pack(
            pady=5)

        self.tree_beneficiarios = ttk.Treeview(self.tab_beneficiarios, columns=("Beneficiário", "Total Recebido"),
                                               show="headings")
        for col in self.tree_beneficiarios["columns"]:
            self.tree_beneficiarios.heading(col, text=col)
        self.tree_beneficiarios.pack(fill='both', expand=True, pady=5)

    def buscar_beneficiarios(self):
        try:
            resultados = self.dao.beneficiarios_mais_produtos()
            self.tree_beneficiarios.delete(*self.tree_beneficiarios.get_children())
            for row in resultados:
                self.tree_beneficiarios.insert("", "end", values=(row["beneficiario"], row["total_recebido"]))
        except Exception as e:
            messagebox.showerror("Erro", str(e))


