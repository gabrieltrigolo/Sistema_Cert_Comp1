# Importando biblioteca Tkinter
import tkinter as tk


class PaginaUsuario:
    def __init__(self):
        # Configurações iniciais
        self.fonte = ("Arial", 12)
        self.conf_Button = {
            "width": 5,
            "height": 1,
            "padx": 10,
            "pady": 5
        }

        # Criando a janela principal
        self.tela = tk.Tk()
        self.tela.title("Usuário")
        self.tela.geometry("700x400")

        # Criando Frame
        self.Botao_frame = tk.Frame(self.tela)
        self.Botao_frame.pack(pady=50)

        # Criando botões
        self.criar_botoes()

    def criar_botoes(self):
        # Lista de tuplas com (texto, comando)
        botoes = [
            ("Inserir Usuários", self.Inserir_usuario),
            ("Deletar Usuários", self.Deletar_usuario),
            ("Alterar Usuários", self.Alterar_usuario),
            ("Alterar Permissões", self.Alterar_permissoes),
            ("Voltar", self.Voltar)
        ]

        # Criando e posicionando os botões
        for i, (texto, comando) in enumerate(botoes):
            botao = tk.Button(
                self.Botao_frame,
                text=texto,
                command=comando,
                font=self.fonte
            )
            # Adiciona pady=20 para botões alternados
            botao.pack(pady=20 if i % 2 == 0 else 0)

    def Inserir_usuario(self):
        print("entrou Inserir Usuários")

    def Deletar_usuario(self):
        print("deletou Usuários")

    def Alterar_usuario(self):
        print("alterou Usuário")

    def Alterar_permissoes(self):
        print("alterou Permissões")

    def Voltar(self):
        print("voltou")



