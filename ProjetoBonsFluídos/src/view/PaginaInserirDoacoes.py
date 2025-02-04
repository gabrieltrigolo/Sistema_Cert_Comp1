import tkinter as tk
from tkinter import ttk
from tkcalendar import DateEntry
from datetime import date
from ProjetoBonsFluídos.src.dao.DoacaoDAO import DoacaoDAO
from ProjetoBonsFluídos.src.model.Produto import Produto
from ProjetoBonsFluídos.src.model.Doacao import Doacao


class PaginaInserirDoacoes:
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
        self.tela.title("Inserir Doações")
        self.tela.geometry("700x500")

        # Criando Frames
        self.Entrada_frame = tk.Frame(self.tela)
        self.Botao_frame = tk.Frame(self.tela)

        # Posicionando os frames
        self.Entrada_frame.pack(pady=10)
        self.Botao_frame.pack(pady=10)

        # Labels e Campos de Entrada
        self.criar_campos()

        # Criando botões
        self.criar_botoes()

    def criar_campos(self):
        lbl_nome = tk.Label(self.Entrada_frame, text="Nome:", font=self.fonte)
        lbl_nome.grid(row=0, column=0, padx=5, pady=5)

        self.ent_nome = tk.Entry(self.Entrada_frame, font=self.fonte)
        self.ent_nome.grid(row=0, column=1, padx=5, pady=5)

        lbl_desc = tk.Label(self.Entrada_frame, text="Descrição:", font=self.fonte)
        lbl_desc.grid(row=1, column=0, padx=5, pady=5)

        self.ent_desc = tk.Entry(self.Entrada_frame, font=self.fonte)
        self.ent_desc.grid(row=1, column=1, padx=5, pady=5)

        lbl_quantidade = tk.Label(self.Entrada_frame, text="Quantidade:", font=self.fonte)
        lbl_quantidade.grid(row=2, column=0, padx=5, pady=5)

        self.ent_quantidade = tk.Entry(self.Entrada_frame, font=self.fonte)
        self.ent_quantidade.grid(row=2, column=1, padx=5, pady=5)

        lbl_doador = tk.Label(self.Entrada_frame, text="Doador:", font=self.fonte)
        lbl_doador.grid(row=3, column=0, padx=5, pady=5)

        self.ent_doador = tk.Entry(self.Entrada_frame, font=self.fonte)
        self.ent_doador.grid(row=3, column=1, padx=5, pady=5)

    def criar_botoes(self):
        Inserir_button = tk.Button(self.Botao_frame, text="Inserir", command=self.inserir_dados, font=self.fonte,
                                   **self.conf_Button)
        Voltar_button = tk.Button(self.Botao_frame, text="Voltar", command=self.voltar_para_menu_principal,
                                  font=self.fonte, **self.conf_Button)

        # Posicionando os botões
        Inserir_button.pack(side=tk.LEFT, padx=10)
        Voltar_button.pack(side=tk.LEFT, padx=10)

    def inserir_dados(self):
        data = date.today()
        nome = self.ent_nome.get()
        quantidade = self.ent_quantidade.get()
        descricao = self.ent_desc.get()
        doador = self.ent_doador.get()

        produto = Produto(None, nome, descricao, quantidade, data)
        dao = DoacaoDAO()
        doacao = Doacao(idDoacao=None, produto=produto,
                         dataDoacao=data,
                         quantidade=quantidade,
                         responsavel=doador)
        dao.inserir(doacao)
        print(f"Nome: {nome}, Data: {data}, Quantidade: {quantidade}")


    def voltar_para_menu_principal(self):
        print("Voltar")
        self.tela.destroy()

# Executar a aplicação
if __name__ == "__main__":
    app = PaginaInserirDoacoes()
    tk.mainloop()
