# Importando bibliotecas
import tkinter as tk
from tkinter import ttk
from src.dao.UsuarioDAO import UsuarioDAO
from src.view.PaginaInserirUsuario import PaginaInserirUsuario
from src.view.PaginaDeletarUsuario import PaginaDeletarUsuario
from src.view.PaginaAlterarUsuario import PaginaAlterarUsuario
from src.view.PaginaAlterarPermissoes import PaginaAlterarPermissoes

class PaginaUsuario:
    def __init__(self, master):
        # Configurações iniciais
        self.fonte = ("Arial", 12)

        # Criando a janela principal
        self.master = master
        self.tela = tk.Tk()
        self.tela.title("Usuário")
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
        self.Tabela_frame.pack(expand=True, fill="both", padx=10, pady=10)

        self.Botao_frame = tk.Frame(self.tela)
        self.Botao_frame.pack(side=tk.BOTTOM, pady=20, fill=tk.X)

        # Criando componentes
        self.criar_titulo_tabela()
        self.criar_tabela()
        self.criar_botoes()

    def criar_titulo_tabela(self):
        lbl_titulo = tk.Label(
            self.Tabela_frame,
            text="Lista de Usuários",
            font=("Arial", 14, "bold"),
            anchor="center"
        )
        lbl_titulo.pack(fill=tk.X, pady=(0, 10))

    def criar_tabela(self):
        columns = ("ID", "Nome", "Email", "Cargo")
        self.tree = ttk.Treeview(self.Tabela_frame, columns=columns, show="headings")

        # Configurando cabeçalhos
        for col in columns:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=100 if col == "ID" else 200)

        # Limpando e populando dados
        self.tree.delete(*self.tree.get_children())
        for usuario in UsuarioDAO().listarTodosUsuarios():
            self.tree.insert("", tk.END, values=usuario)

        # Adicionando scrollbar
        scrollbar = ttk.Scrollbar(self.Tabela_frame, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscrollcommand=scrollbar.set)
        scrollbar.pack(side="right", fill="y")
        self.tree.pack(expand=True, fill="both")

    def criar_botoes(self):
        # Lista de botões
        botoes = [
            ("Inserir", self.Inserir_usuario),
            ("Deletar", self.Deletar_usuario),
            ("Alterar", self.Alterar_usuario),
            ("Permissões", self.Alterar_permissoes),
            ("Voltar", self.Voltar)
        ]

        # Adicionando botões na parte inferior
        for col, (texto, comando) in enumerate(botoes):
            btn = tk.Button(
                self.Botao_frame,
                text=texto,
                command=comando,
                font=self.fonte,
                width=12,
                pady=8
            )
            btn.grid(row=0, column=col, padx=5, sticky="ew")
            self.Botao_frame.grid_columnconfigure(col, weight=1)

    # Mantidos os métodos originais
    def Inserir_usuario(self):
        self.tela.withdraw()  # Oculta a tela de login
        self.tela_inserirusuario = PaginaInserirUsuario(self.tela)

    def Deletar_usuario(self):
        tela_deletarusuario = PaginaDeletarUsuario()
        tela_deletarusuario.tela.mainloop()

    def Alterar_usuario(self):
        tela_alterarusuario = PaginaAlterarUsuario()
        tela_alterarusuario.tela.mainloop()

    def Alterar_permissoes(self):
        tela_permissao = PaginaAlterarPermissoes()
        tela_permissao.tela.mainloop()

    def Voltar(self):
        self.tela.destroy()
        self.master.deiconify()  # Reexibe a tela ADM
