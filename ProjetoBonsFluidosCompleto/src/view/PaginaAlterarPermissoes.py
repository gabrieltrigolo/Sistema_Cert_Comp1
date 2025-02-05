import tkinter as tk
from tkinter import ttk, messagebox
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
        # Definir o tamanho da janela
        largura_janela = 700
        altura_janela = 500
        # Obter o tamanho da tela
        largura_tela = self.tela.winfo_screenwidth()
        altura_tela = self.tela.winfo_screenheight()
        # Calcular a posição x e y para centralizar a janela
        pos_x = (largura_tela - largura_janela) // 2
        pos_y = (altura_tela - altura_janela) // 2
        # Definir a geometria da janela
        self.tela.geometry(f"{largura_janela}x{altura_janela}+{pos_x}+{pos_y}")

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
        columns = ("ID", "Nome", "Email", "Cargo")
        self.tree = ttk.Treeview(self.Tabela_frame, columns=columns, show="headings")

        # Definindo os títulos das colunas
        for col in columns:
            self.tree.heading(col, text=col)

        # Definindo o tamanho das colunas
        self.tree.column("ID", width=50)
        self.tree.column("Nome", width=150)
        self.tree.column("Email", width=200)
        self.tree.column("Email", width=150)

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

        # Verifica se o ID foi preenchido
        if not id_usuario.strip():
            messagebox.showerror("Erro", "Por favor, insira um ID válido.")
            return

        dao = UsuarioDAO()
        usuario = dao.buscarPorId(id_usuario)

        if usuario:
            usuario.cargo = permissao
            dao.atualizar(id_usuario, usuario)
            self.atualizar_tabela()
            messagebox.showinfo("Sucesso", f"Permissão do usuário {usuario.nome} alterada para {permissao}!")
        else:
            messagebox.showerror("Erro", "Usuário não encontrado.")

    def voltar(self):
        confirmacao = messagebox.askyesno("Confirmar", "Tem certeza que deseja voltar?")
        if confirmacao:
            self.tela.destroy()


