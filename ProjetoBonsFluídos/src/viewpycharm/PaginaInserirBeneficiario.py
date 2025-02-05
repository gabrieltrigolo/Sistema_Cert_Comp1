import tkinter as tk
from tkinter import ttk, messagebox

from src.dao.BeneficiarioDAO import BeneficiarioDAO
from src.model.Beneficiario import Beneficiario


class PaginaInserirBeneficiario:
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
        self.tela.title("Inserir Beneficiário")
        self.tela.geometry("700x500")

        # Criando Frames
        self.Nome_frame = tk.Frame(self.tela)
        self.Email_frame = tk.Frame(self.tela)
        self.CPFCNPJ_frame = tk.Frame(self.tela)
        self.Botao_frame = tk.Frame(self.tela)

        # Colocando frames à tela
        self.Nome_frame.pack(pady=10)
        self.Email_frame.pack()
        self.CPFCNPJ_frame.pack()
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
        tk.Label(self.CPFCNPJ_frame, text="CPF ou CNPJ:", font=self.fonte, **self.conf_Label).pack()

    def criar_entries(self):
        self.Nome_entry = tk.Entry(self.Nome_frame, font=self.fonte, **self.conf_Entry)
        self.Nome_entry.pack()

        self.Email_entry = tk.Entry(self.Email_frame, font=self.fonte, **self.conf_Entry)
        self.Email_entry.pack()

        self.CPFCNPJ_entry = tk.Entry(self.CPFCNPJ_frame, font=self.fonte, **self.conf_Entry)
        self.CPFCNPJ_entry.pack()

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
        cpfcnpj = self.CPFCNPJ_entry.get()

        if not nome or not email or not cpfcnpj:
            messagebox.showerror("Erro", "Todos os campos devem ser preenchidos!")
            return

        beneficiario = Beneficiario(None, nome, email, cpfcnpj)
        dao = BeneficiarioDAO()

        try:
            dao.inserir(beneficiario)
            messagebox.showinfo("Sucesso", "Beneficiário inserido com sucesso!")
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao inserir beneficiário: {e}")

    def voltar(self):
        self.tela.destroy()


