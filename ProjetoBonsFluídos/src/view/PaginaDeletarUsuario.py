import tkinter as tk
from tkinter import ttk

from src.dao.UsuarioDAO import UsuarioDAO


class PaginaDeletarUsuario:
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
        self.tela.title("Deletar Usuário")
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

    def atualizar_tabela(self):

        for item in self.tree.get_children():
            self.tree.delete(item)

        dao = UsuarioDAO()
        usuarios = dao.listarTodosUsuarios()
        for usuario in usuarios:
            self.tree.insert("", tk.END, values=usuario)


    def criar_botoes(self):
        Deletar_button = tk.Button(self.Botao_frame, text="Deletar", command=self.deletar, font=self.fonte,
                                   **self.conf_Button)
        Voltar_button = tk.Button(self.Botao_frame, text="Voltar", command=self.voltar, font=self.fonte,
                                  **self.conf_Button)

        # Posicionando os botões
        Deletar_button.pack(side=tk.LEFT, padx=10)
        Voltar_button.pack(side=tk.LEFT, padx=10)

    def deletar(self):
        print("Deletar")
        id = self.ent_id.get()
        dao = UsuarioDAO()
        dao.deletar(id)
        self.atualizar_tabela()

    def voltar(self):
        print("Voltar")
        self.tela.destroy()

# Executar a aplicação
if __name__ == "__main__":
    app = PaginaDeletarUsuario()
    tk.mainloop()
