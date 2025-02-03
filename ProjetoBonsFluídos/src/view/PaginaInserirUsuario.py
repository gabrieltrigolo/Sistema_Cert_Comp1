import tkinter as tk
from tkinter import ttk


class PaginaInserirUsuario:
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
            "width": 10,
            "height": 1,
            "padx": 10,
            "pady": 5
        }

        # Criando Tela
        self.tela = tk.Tk()
        self.tela.title("Inserir Usuário")
        self.tela.geometry("700x400")

        # Criando Frames
        self.Nome_frame = tk.Frame(self.tela)
        self.Data_frame = tk.Frame(self.tela)
        self.CPF_frame = tk.Frame(self.tela)
        self.Permissao_frame = tk.Frame(self.tela)
        self.Botao_frame = tk.Frame(self.tela)

        # Colocando frames à tela
        self.Nome_frame.pack(pady=10)
        self.Data_frame.pack()
        self.CPF_frame.pack()
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
        tk.Label(self.Data_frame, text="Data de Nascimento:", font=self.fonte, **self.conf_Label).pack()
        tk.Label(self.CPF_frame, text="CPF:", font=self.fonte, **self.conf_Label).pack()
        tk.Label(self.Permissao_frame, text="Permissão:", font=self.fonte, **self.conf_Label).pack()

    def criar_entries(self):
        self.Nome_entry = tk.Entry(self.Nome_frame, font=self.fonte, **self.conf_Entry)
        self.Nome_entry.pack()

        self.Data_entry = tk.Entry(self.Data_frame, font=self.fonte, **self.conf_Entry)
        self.Data_entry.pack()

        self.CPF_entry = tk.Entry(self.CPF_frame, font=self.fonte, **self.conf_Entry)
        self.CPF_entry.pack()

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
        data_nasc = self.Data_entry.get()
        cpf = self.CPF_entry.get()
        permissao = self.Permissao_combobox.get()

        print(f"Usuário Inserido: {nome}, {data_nasc}, {cpf}, Permissão: {permissao}")

    def voltar(self):
        self.tela.destroy()


