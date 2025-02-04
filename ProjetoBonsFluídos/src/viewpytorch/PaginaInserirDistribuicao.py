import tkinter as tk
from tkinter import ttk
from datetime import date

from src.dao.BeneficiarioDAO import BeneficiarioDAO
from src.dao.DistribuicaoDAO import DistribuicaoDAO
from src.dao.ProdutoDAO import ProdutoDAO
from src.dao.UsuarioDAO import UsuarioDAO
from src.model.Beneficiario import Beneficiario


class PaginaInserirDistribuicao:
    def __init__(self):
        # Configurações iniciais
        self.fonte = ("Arial", 12)
        self.conf_Label = {
            "width": 20,
            "height": 0,
            "padx": 5,
            "pady": 5
        }
        self.conf_Entry = {
            "width": 10,
            "justify": "center"
        }
        self.conf_Button = {
            "width": 10,
            "height": 1,
            "padx": 10,
            "pady": 5
        }

        # Criando Tela
        self.tela = tk.Tk()
        self.tela.title("Inserir Distribuicao")
        self.tela.geometry("1000x500")

        # Criando Frames
        self.Tabela_frame = tk.Frame(self.tela)
        self.Entrada_frame = tk.Frame(self.tela)
        self.Campos_frame = tk.Frame(self.tela)
        self.Botao_frame = tk.Frame(self.tela)

        # Posicionando os frames
        self.Tabela_frame.pack(pady=10, fill=tk.BOTH, expand=True)
        self.Entrada_frame.pack(pady=10)
        self.Campos_frame.pack(pady=10)
        self.Botao_frame.pack(pady=20)

        # Criando sub-frames para as tabelas
        self.Tabela1_frame = tk.Frame(self.Tabela_frame)
        self.Tabela2_frame = tk.Frame(self.Tabela_frame)
        self.Tabela1_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=5)
        self.Tabela2_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=5)

        # Criando rótulos (Labels)
        self.criar_rotulos()

        # Criando entradas de texto (Entry)
        self.criar_entries()

        # Criando as tabelas com scrollbars
        self.criar_tabela_usuarios()
        self.criar_tabela_beneficiarios()

        # Criando botões
        self.criar_botoes()

    def criar_rotulos(self):
        tk.Label(self.Campos_frame, text="Quantidade:", font=self.fonte, **self.conf_Label).grid(row=0, column=0)
        tk.Label(self.Campos_frame, text="ID Beneficiário:", font=self.fonte, **self.conf_Label).grid(row=0, column=1)

    def criar_entries(self):
        # Entrada de quantidade e ID lado a lado
        self.Quantidade_entry = tk.Entry(self.Campos_frame, font=self.fonte, **self.conf_Entry)
        self.Quantidade_entry.grid(row=1, column=0, padx=5)

        self.ID_entry = tk.Entry(self.Campos_frame, font=self.fonte, **self.conf_Entry)
        self.ID_entry.grid(row=1, column=1, padx=5)

        # Combobox para produtos
        Produto_label = tk.Label(self.Entrada_frame, text="Produto:", font=self.fonte)
        Produto_label.grid(row=1, column=0, padx=5, pady=5)

        self.Produto_combobox = ttk.Combobox(
            self.Entrada_frame,
            values=["Absorvente"],
            font=self.fonte,
            width=16
        )
        self.Produto_combobox.current(0)
        self.Produto_combobox.grid(row=1, column=1, padx=5, pady=5)

    def criar_tabela_usuarios(self):
        # Container para tabela e scrollbars
        container = tk.Frame(self.Tabela1_frame)
        container.pack(fill=tk.BOTH, expand=True)

        # Título
        tk.Label(container, text="Lista de Produtos", font=("Arial", 14, "bold"),
                 bg="#f0f0f0").grid(row=0, column=0, columnspan=2, sticky="ew")

        # Tabela
        columns = ("Nome", "Descrição", "Quantidade", "Data")
        self.tree_produtos = ttk.Treeview(container, columns=columns, show="headings")

        # Scrollbars
        yscroll = ttk.Scrollbar(container, orient="vertical", command=self.tree_produtos.yview)
        xscroll = ttk.Scrollbar(container, orient="horizontal", command=self.tree_produtos.xview)
        self.tree_produtos.configure(yscrollcommand=yscroll.set, xscrollcommand=xscroll.set)

        # Layout
        self.tree_produtos.grid(row=1, column=0, sticky="nsew")
        yscroll.grid(row=1, column=1, sticky="ns")
        xscroll.grid(row=2, column=0, sticky="ew")

        # Configurar colunas
        for col in columns:
            self.tree_produtos.heading(col, text=col)
            self.tree_produtos.column(col, width=100)

        # Popular dados
        dao = ProdutoDAO()
        produtos = dao.listarTodosProdutos()
        for produto in produtos:
            self.tree_produtos.insert("", tk.END, values=produto)

        # Configurar peso da grid
        container.grid_rowconfigure(1, weight=1)
        container.grid_columnconfigure(0, weight=1)

    def criar_tabela_beneficiarios(self):
        # Container para tabela e scrollbars
        container = tk.Frame(self.Tabela2_frame)
        container.pack(fill=tk.BOTH, expand=True)

        # Título
        tk.Label(container, text="Lista de Beneficiários", font=("Arial", 14, "bold"),
                 bg="#f0f0f0").grid(row=0, column=0, columnspan=2, sticky="ew")

        # Tabela
        columns = ("CPF/CNPJ", "Nome", "Email", "ID")
        self.tree_beneficiarios = ttk.Treeview(container, columns=columns, show="headings")

        # Scrollbars
        yscroll = ttk.Scrollbar(container, orient="vertical", command=self.tree_beneficiarios.yview)
        xscroll = ttk.Scrollbar(container, orient="horizontal", command=self.tree_beneficiarios.xview)
        self.tree_beneficiarios.configure(yscrollcommand=yscroll.set, xscrollcommand=xscroll.set)

        # Layout
        self.tree_beneficiarios.grid(row=1, column=0, sticky="nsew")
        yscroll.grid(row=1, column=1, sticky="ns")
        xscroll.grid(row=2, column=0, sticky="ew")

        # Configurar colunas
        for col in columns:
            self.tree_beneficiarios.heading(col, text=col)
            self.tree_beneficiarios.column(col, width=100)

        # Popular dados
        dao = BeneficiarioDAO()
        beneficiarios = dao.listarTodosBeneficiarios()
        for benef in beneficiarios:
            self.tree_beneficiarios.insert("", tk.END, values=benef)

        # Configurar peso da grid
        container.grid_rowconfigure(1, weight=1)
        container.grid_columnconfigure(0, weight=1)

    def atualizar_tabela(self):

        for item in self.tree_beneficiarios.get_children():
            self.tree_beneficiarios.delete(item)

        dao = BeneficiarioDAO()
        beneficiarios = dao.listarTodosBeneficiarios()
        for benef in beneficiarios:
            self.tree_beneficiarios.insert("", tk.END, values=benef)

        for item in self.tree_produtos.get_children():
            self.tree_produtos.delete(item)

        # Popular dados
        dao = ProdutoDAO()
        produtos = dao.listarTodosProdutos()
        for produto in produtos:
            self.tree_produtos.insert("", tk.END, values=produto)

    def criar_botoes(self):
        Inserir_button = tk.Button(
            self.Botao_frame,
            text="Inserir",
            command=self.inserir,
            font=self.fonte,
            **self.conf_Button
        )

        Voltar_button = tk.Button(
            self.Botao_frame,
            text="Voltar",
            command=self.voltar,
            font=self.fonte,
            **self.conf_Button
        )

        Inserir_button.pack(side=tk.LEFT, padx=10)
        Voltar_button.pack(side=tk.RIGHT, padx=10)

    def inserir(self):
        nome = self.Produto_combobox.get()
        quantidade = int(self.Quantidade_entry.get())
        id = self.ID_entry.get()
        dao = DistribuicaoDAO()
        dao.inserirEspecial(nome, id, quantidade, date.today())
        self.atualizar_tabela()

    def voltar(self):
        self.tela.destroy()


# Executar a aplicação
if __name__ == "__main__":
    app = PaginaInserirDistribuicao()
    tk.mainloop()