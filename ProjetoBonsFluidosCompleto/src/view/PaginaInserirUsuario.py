import tkinter as tk
from tkinter import ttk, messagebox
from src.dao.UsuarioDAO import UsuarioDAO
from src.model.Usuario import Usuario

class PaginaInserirUsuario:
    def __init__(self, master):
        # Configurações iniciais
        self.fonte = ("Arial", 12)
        self.conf_Label = {
            "width": 20,
            "height": 2,
            "padx": 10,
            "pady": 10
        }
        self.conf_Entry = {
            "width": 40
        }
        self.conf_Button = {
            "width": 10,
            "height": 1,
            "padx": 10,
            "pady": 5
        }

        # Criando Tela
        self.master = master  # Referência à janela principal
        self.tela = tk.Toplevel()
        self.tela.title("Inserir Usuário")
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
        self.tela.grab_set()  # Modal: bloqueia interação externa
        self.tela.focus_force()  # Foca na janela atual

        # Criando Frames
        self.Nome_frame = tk.Frame(self.tela)
        self.Email_frame = tk.Frame(self.tela)
        self.Senha_frame = tk.Frame(self.tela)
        self.Permissao_frame = tk.Frame(self.tela)
        self.Botao_frame = tk.Frame(self.tela)

        # Colocando frames à tela
        self.Nome_frame.pack(pady=10)
        self.Email_frame.pack()
        self.Senha_frame.pack()
        self.Permissao_frame.pack()
        self.Botao_frame.pack(pady=20)

        # Criando rótulos (Labels)
        self.criar_rotulos()

        # Criando entradas de texto (Entry)
        self.criar_entries()

        # Criando botões
        self.criar_botoes()

    def criar_rotulos(self):
        tk.Label(self.Nome_frame, text="Nome:", font=self.fonte, **self.conf_Label).pack()
        tk.Label(self.Email_frame, text="Email:", font=self.fonte, **self.conf_Label).pack()
        tk.Label(self.Senha_frame, text="Senha:", font=self.fonte, **self.conf_Label).pack()
        tk.Label(self.Permissao_frame, text="Permissão:", font=self.fonte, **self.conf_Label).pack()

    def criar_entries(self):
        self.Nome_entry = tk.Entry(self.Nome_frame, font=self.fonte, **self.conf_Entry)
        self.Nome_entry.pack()

        self.Email_entry = tk.Entry(self.Email_frame, font=self.fonte, **self.conf_Entry)
        self.Email_entry.pack()

        self.Senha_entry = tk.Entry(self.Senha_frame, show="*", font=self.fonte, **self.conf_Entry)
        self.Senha_entry.pack()

        self.Permissao_combobox = ttk.Combobox(
            self.Permissao_frame,
            values=["Administrador", "Usuário", "Visitante"],
            font=self.fonte,
            width=37
        )
        self.Permissao_combobox.current(0)
        self.Permissao_combobox.pack()

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
        nome = self.Nome_entry.get()
        email = self.Email_entry.get()
        senha = self.Senha_entry.get()
        permissao = self.Permissao_combobox.get()

        # Verificação de campos vazios
        if not nome or not email or not senha:
            messagebox.showerror("Erro", "Por favor, preencha todos os campos.")
            return
        try:
            # Criação do objeto Usuario e inserção no banco de dados
            user_novo1 = Usuario(None, nome, email, senha, permissao)
            dao = UsuarioDAO()
            dao.inserir(user_novo1)
            messagebox.showinfo("Sucesso", "Usuário inserido com sucesso!")
        except Exception as e:
            # Exibição de erro caso algo dê errado
            messagebox.showerror("Erro", f"Falha ao inserir o usuário: {str(e)}")

    def voltar(self):
        self.tela.destroy()  # Fecha a tela de cadastro
        self.master.deiconify()  # Reexibe a tela de login

