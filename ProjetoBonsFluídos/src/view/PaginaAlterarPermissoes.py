import tkinter as tk
from tkinter import ttk

from src.dao.UsuarioDAO import UsuarioDAO


class PaginaAlterarPermissoes:
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
        self.tela.title("Alterar Permissões")
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
        lbl_id = tk.Label(self.Entrada_frame, text="ID:", font=self.fonte)
        lbl_id.grid(row=0, column=0, padx=5, pady=5)

        self.ent_id = tk.Entry(self.Entrada_frame, font=self.fonte)
        self.ent_id.grid(row=0, column=1, padx=5, pady=5)

        Permissao_label = tk.Label(self.Entrada_frame, text="Permissão:", font=self.fonte)
        Permissao_label.grid(row=1, column=0, padx=5, pady=5)

        self.Permissao_combobox = ttk.Combobox(
            self.Entrada_frame,
            values=["Administrador", "Usuário", "Visitante"],
            font=self.fonte,
            width=37
        )
        self.Permissao_combobox.current(0)
        self.Permissao_combobox.grid(row=1, column=1, padx=5, pady=5)

    def criar_tabela(self):
        columns = ("ID", "Nome", "Email")
        self.tree = ttk.Treeview(self.Tabela_frame, columns=columns, show="headings")

        # Definindo os títulos das colunas
        for col in columns:
            self.tree.heading(col, text=col)

        # Definindo o tamanho das colunas
        self.tree.column("ID", width=50)
        self.tree.column("Nome", width=150)
        self.tree.column("Email", width=200)

        for item in self.tree.get_children():
            self.tree.delete(item)

        dao = UsuarioDAO()
        usuarios = dao.listarTodosUsuarios()
        for usuario in usuarios:
            self.tree.insert("", tk.END, values=usuario)

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

        dao = UsuarioDAO()
        usuarios = dao.listarTodosUsuarios()
        for usuario in usuarios:
            self.tree.insert("", tk.END, values=usuario)

    def alterar(self):
        permissao = self.Permissao_combobox.get()
        id_usuario = self.ent_id.get()

        dao = UsuarioDAO()
        # Teste do metodo buscarPorId
        user_id = self.ent_id.get()  # Substitua pelo ID gerado ao inserir
        usuario = dao.buscarPorId(user_id)

        # Verificar se o usuário existe
        if usuario:
            # Alterando o nome
            usuario.cargo = permissao
            dao.atualizar(user_id, usuario)
            self.atualizar_tabela()
        else:
            print("Usuário não encontrado.")

        print(f"{permissao} {id_usuario} Alterar")

    def voltar(self):
        print("Voltar")


# Executar a aplicação
if __name__ == "__main__":
    app = PaginaAlterarPermissoes()
    tk.mainloop()
