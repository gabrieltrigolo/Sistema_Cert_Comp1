import tkinter as tk
from tkinter import ttk

# Criando dicionário de fontes e configs
fonte = ("Arial", 12)
conf_Button = {
    "width": 10,
    "height": 1,
    "padx": 10,
    "pady": 5
}

# Função quando botão for pressionado
def Voltar():
    print("Voltar")

# Criando a janela principal
tela = tk.Tk()
tela.title("Histórico")
tela.geometry("700x500")

# Criando Frames
Tabela_frame = tk.Frame(tela)
Botao_frame = tk.Frame(tela)

# Posicionando os frames
Tabela_frame.pack(pady=10)
Botao_frame.pack(pady=10)

# Criando a tabela
columns = ("ID", "Nome", "Idade")
tree = ttk.Treeview(Tabela_frame, columns=columns, show="headings")

# Definindo os títulos das colunas
tree.heading("ID", text="ID")
tree.heading("Nome", text="Nome")
tree.heading("Idade", text="Idade")

# Definindo o tamanho das colunas
tree.column("ID", width=50)
tree.column("Nome", width=150)
tree.column("Idade", width=50)

# Adicionando dados à tabela
dados = [(1, "Pedro", 22), (2, "Ana", 25), (3, "João", 30)]
for dado in dados:
    tree.insert("", tk.END, values=dado)

# Posicionando a tabela na janela
tree.pack(expand=True, fill="both")

# Criando botões
Voltar_button = tk.Button(Botao_frame, text="Voltar", command=Voltar, font=fonte, **conf_Button)

# Posicionando os botões
Voltar_button.pack(side=tk.LEFT, padx=10)

# Rodando o loop da interface
tela.mainloop()
