# Importando biblioteca Tkinter
import tkinter as tk

from src.view.PaginaInserirDistribuicao import PaginaInserirDistribuicao
from src.view.PaginaDeletarDistribuicao import PaginaDeletarDistribuicao


class PaginaDistribuicao:
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
            ("Inserir Distribuição", self.Inserir_distribuicao),
            ("Deletar Distribuição", self.Deletar_distribuicao),
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

    def Inserir_distribuicao(self):
        print("entrou Inserir Usuários")
        tela_inserirdistribuicao = PaginaInserirDistribuicao()
        tela_inserirdistribuicao.tela.mainloop()
    
    def Deletar_distribuicao(self):
        print("entrou Inserir Usuários")
        tela_deletardistribuicao = PaginaDeletarDistribuicao()
        tela_deletardistribuicao.tela.mainloop()

    def Voltar(self):
        print("voltou")

# Executar a aplicação
if __name__ == "__main__":
    app = PaginaDistribuicao()
    tk.mainloop()