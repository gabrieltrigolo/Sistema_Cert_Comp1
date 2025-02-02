import tkinter as tk
from tkinter import ttk

# Criando dicionário de fontes e configs
fonte = ("Arial", 12)
conf_Label = {
    "width": 20,
    "height": 2,
    "padx": 10,
    "pady": 10
}
conf_Entry = {
    "width": 40
}
conf_Button = {
    "width": 10,
    "height": 1,
    "padx": 10,
    "pady": 5
}

# Função quando botão for pressionado
def inserir():
    nome = Nome_entry.get()
    data_nasc = Data_entry.get()
    cpf = CPF_entry.get()
    permissao = Permissao_combobox.get()
    print(f"Usuário Inserido: {nome}, {data_nasc}, {cpf}, Permissão: {permissao}")

def voltar():
    tela.destroy()

# Criando Tela
tela = tk.Tk()
tela.title("Inserir Usuário")
tela.geometry("700x400")

# Criando Frames
Nome_frame = tk.Frame(tela)
Data_frame = tk.Frame(tela)
CPF_frame = tk.Frame(tela)
Permissao_frame = tk.Frame(tela)
Botao_frame = tk.Frame(tela)

# Colocando frames à tela
Nome_frame.pack(pady=10)
Data_frame.pack()
CPF_frame.pack()
Permissao_frame.pack()
Botao_frame.pack(pady=20)

# Criando rótulos (Labels)
Nome_label = tk.Label(Nome_frame, text="Nome:", font=fonte, **conf_Label)
Data_label = tk.Label(Data_frame, text="Data de Nascimento:", font=fonte, **conf_Label)
CPF_label = tk.Label(CPF_frame, text="CPF:", font=fonte, **conf_Label)
Permissao_label = tk.Label(Permissao_frame, text="Permissão:", font=fonte, **conf_Label)

# Criando entrada de texto (Entry)
Nome_entry = tk.Entry(Nome_frame, font=fonte, **conf_Entry)
Data_entry = tk.Entry(Data_frame, font=fonte, **conf_Entry)
CPF_entry = tk.Entry(CPF_frame, font=fonte, **conf_Entry)
Permissao_combobox = ttk.Combobox(Permissao_frame, values=["Administrador", "Usuário", "Visitante"], font=fonte, width=37)
Permissao_combobox.current(0)

# Criando botões
Inserir_button = tk.Button(Botao_frame, text="Inserir", command=inserir, font=fonte, **conf_Button)
Voltar_button = tk.Button(Botao_frame, text="Voltar", command=voltar, font=fonte, **conf_Button)

# Colocando elementos à tela
Nome_label.pack()
Nome_entry.pack()
Data_label.pack()
Data_entry.pack()
CPF_label.pack()
CPF_entry.pack()
Permissao_label.pack()
Permissao_combobox.pack()
Inserir_button.pack(side=tk.LEFT, padx=10)
Voltar_button.pack(side=tk.RIGHT, padx=10)

# Executar o loop principal
tela.mainloop()
