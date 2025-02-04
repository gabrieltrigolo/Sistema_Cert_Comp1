import tkinter as tk
from tkinter import ttk

from ProjetoBonsFluídos.src.dao.BeneficiarioDAO import BeneficiarioDAO
from ProjetoBonsFluídos.src.dao.UsuarioDAO import UsuarioDAO

class PaginaAlterarBeneficiario:
    def __init__(self):
        # Configurações iniciais
        self.fonte = ("Arial", 12)
        self.conf_Button = {
            "width": 10,
            "height": 1,
            "padx": 10,
            "pady": 5
        }

        # Criando a janela principal
        self.tela = tk.Tk()
        self.tela.title("Alterar Beneficiario")
        self.tela.geometry("700x500")

        # Criando Frames
        self.Tabela_frame = tk.Frame(self.tela)
        self.Entrada_frame = tk.Frame(self.tela)
        self.Botao_frame = tk.Frame(self.tela)

        # Posicionando os frames
        self.Tabela_frame.pack(pady=10)
        self.Entrada_frame.pack(pady=10)
        self.Botao_frame.pack(pady=10)

        # Criando Label e Campo de Entrada
        self.criar_entrada()

        # Criando a tabela
        self.criar_tabela()

        # Criando botões
        self.criar_botoes()

    def criar_entrada(self):
        lbl_id = tk.Label(self.Entrada_frame, text="CPF ou CNPJ:", font=self.fonte)
        lbl_id.grid(row=0, column=0, padx=5, pady=5)

        self.ent_id = tk.Entry(self.Entrada_frame, font=self.fonte)
        self.ent_id.grid(row=0, column=1, padx=5, pady=5)

        Categoria_label = tk.Label(self.Entrada_frame, text="Categoria:", font=self.fonte)
        Categoria_label.grid(row=1, column=0, padx=5, pady=5)

        self.Categoria_combobox = ttk.Combobox(
            self.Entrada_frame,
            values=["Nome", "Email"],
            font=self.fonte,
            width=37
        )
        self.Categoria_combobox.current(0)
        self.Categoria_combobox.grid(row=1, column=1, padx=5, pady=5)

        Alteracao_label = tk.Label(self.Entrada_frame, text="Alteração:", font=self.fonte)
        Alteracao_label.grid(row=2, column=0, padx=5, pady=5)

        self.Alteracao_entry = tk.Entry(self.Entrada_frame, font=self.fonte)
        self.Alteracao_entry.grid(row=2, column=1, padx=5, pady=5)

    def criar_tabela(self):
        columns = ("CPF ou CNPJ", "Nome", "Email")
        self.tree = ttk.Treeview(self.Tabela_frame, columns=columns, show="headings")

        # Definindo os títulos das colunas
        for col in columns:
            self.tree.heading(col, text=col)

        # Definindo o tamanho das colunas
        self.tree.column("CPF ou CNPJ", width=100)
        self.tree.column("Nome", width=150)
        self.tree.column("Email", width=200)

        self.atualizar_tabela()

        # Posicionando a tabela na janela
        self.tree.pack(expand=True, fill="both")

    def criar_botoes(self):
        Alterar_button = tk.Button(
            self.Botao_frame,
            text="Alterar",
            command=self.alterar,
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

        # Posicionando os botões
        Alterar_button.pack(side=tk.LEFT, padx=10)
        Voltar_button.pack(side=tk.LEFT, padx=10)

    def atualizar_tabela(self):

        for item in self.tree.get_children():
            self.tree.delete(item)

        dao = BeneficiarioDAO()
        beneficiarios = dao.listarTodosBeneficiarios()
        for beneficiario in beneficiarios:
            self.tree.insert("", tk.END, values=beneficiario)

    def alterar(self):
        categoria = self.Categoria_combobox.get()
        alterado = self.Alteracao_entry.get()
        dao = BeneficiarioDAO()
        # Teste do metodo buscarPorId
        beneficiario_id = self.ent_id.get()  # Substitua pelo ID gerado ao inserir
        beneficiario = dao.buscarPorId(beneficiario_id)

        # Verificar se o usuário existe
        if beneficiario:
            if categoria == "Nome":
                # Alterando o nome
                beneficiario.nome = alterado
                dao.atualizar(beneficiario)
            elif categoria == "Email":
                # Alterando o email
                beneficiario.email = alterado
                dao.atualizar(beneficiario)
            print(f"{categoria} {alterado} Alterar")
            self.atualizar_tabela()
        else:
            print("Usuário não encontrado.")
    def voltar(self):
        print("Voltar")
        self.tela.destroy()

