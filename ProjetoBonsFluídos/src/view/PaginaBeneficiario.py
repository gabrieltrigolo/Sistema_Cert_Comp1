# Importando biblioteca Tkinter
import tkinter as tk

import PaginaAlterarBeneficiario
import PaginaDeletarBeneficiario
import PaginaInserirBeneficiario


class PaginaBeneficiario:
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
        self.tela.title("Beneficiário")
        self.tela.geometry("700x400")

        # Criando Frame
        self.Botao_frame = tk.Frame(self.tela)
        self.Botao_frame.pack(pady=50)

        # Criando botões
        self.criar_botoes()

    def criar_botoes(self):
        # Lista de tuplas com (texto, comando)
        botoes = [
            ("Inserir Beneficiarios", self.Inserir_beneficiario),
            ("Deletar Beneficiarios", self.Deletar_beneficiario),
            ("Alterar Beneficiarios", self.Alterar_beneficiario),
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

    def Inserir_beneficiario(self):
        print("entrou Inserir Usuários")
        tela_inserirbeneficiario = PaginaInserirBeneficiario.PaginaInserirBeneficiario()
        tela_inserirbeneficiario.tela.mainloop()

    def Deletar_beneficiario(self):
        print("deletou Usuários")
        tela_deletarbeneficiario = PaginaDeletarBeneficiario()
        tela_deletarbeneficiario.tela.mainloop()

    def Alterar_beneficiario(self):
        print("alterou Usuário")
        tela_atualizarbeneficiario = PaginaAlterarBeneficiario()
        tela_atualizarbeneficiario.tela.mainloop()

    def Voltar(self):
        print("voltou")
