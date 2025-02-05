import sys
import os

# Adiciona o diretório raiz ao PYTHONPATH
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


import tkinter as tk
from tkinter import messagebox
from src.dao.UsuarioDAO import UsuarioDAO
from src.view.PaginaAdm import PaginaADM
from src.view.PaginaRelatorio import PaginaRelatorio


class PaginaLogin:
    def __init__(self):
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
            "width": 5,
            "height": 1,
            "padx": 10,
            "pady": 5
        }

        # Criando Tela
        self.tela = tk.Tk()
        self.tela.title("Login")
        self.tela.geometry("700x500")

        # Criando Frames
        self.Email_frame = tk.Frame(self.tela)
        self.Senha_frame = tk.Frame(self.tela)
        self.Botao_frame = tk.Frame(self.tela)

        # Colocando frames à tela
        self.Email_frame.pack(pady=50)
        self.Senha_frame.pack()
        self.Botao_frame.pack(pady=24)

        # Criando rótulos (Labels)
        self.criar_rotulos()

        # Criando entradas de texto (Entry)
        self.criar_entries()

        # Criando botões (Button)
        self.criar_botoes()

    def criar_rotulos(self):
        Email_label = tk.Label(self.Email_frame, text="Email: ", font=self.fonte, **self.conf_Label)
        Senha_label = tk.Label(self.Senha_frame, text="Senha: ", font=self.fonte, **self.conf_Label)

        Email_label.pack()
        Senha_label.pack()

    def criar_entries(self):
        self.Email_entry = tk.Entry(self.Email_frame, font=self.fonte, **self.conf_Entry)
        self.Senha_entry = tk.Entry(self.Senha_frame, show="*", font=self.fonte, **self.conf_Entry)

        self.Email_entry.pack()
        self.Senha_entry.pack()

    def criar_botoes(self):
        Entrar_button = tk.Button(self.Botao_frame, text="Entrar", command=self.entrar, font=self.fonte)
        Cadastrar_button = tk.Button(self.Botao_frame, text="Cadastrar", command=self.cadastrar, font=self.fonte)

        Entrar_button.pack(pady=12)
        Cadastrar_button.pack(pady=12)

    def entrar(self):
        email = self.Email_entry.get()
        senha = self.Senha_entry.get()

        try:
            usuario_dao = UsuarioDAO()
            resultado = usuario_dao.verificarLogin(email, senha)

            if resultado["sucesso"]:
                if resultado["tipo"] == "Administrador":
                    tela_adm = PaginaADM()
                    tela_adm.tela.mainloop()
                else:
                    nova_janela = tk.Toplevel()  # Cria uma nova janela em vez de uma nova instância do Tk
                    tela_relatorio = PaginaRelatorio(nova_janela)  # Passa a nova janela como root
            else:
                messagebox.showerror("Erro de Login", "Email ou senha incorretos!")
        except Exception as e:
            messagebox.showerror("Erro", f"Ocorreu um erro: {str(e)}")

    def cadastrar(self):
        from src.view.PaginaInserirUsuario import PaginaInserirUsuario  # Importação aqui para evitar problemas de referência circular
        tela_inserirusuario = PaginaInserirUsuario()
        tela_inserirusuario.tela.mainloop()


# Executar a aplicação
if __name__ == "__main__":
    app = PaginaLogin()
    app.tela.mainloop()
