import tkinter as tk
from tkinter import ttk

#Criando dicionário de fontes e configs
fonte = {
	("Arial", 12)
}
conf_Button = {
	"width":5,
	"height":1,
	"padx":10,
	"pady":5
}

#Função quando botão for pressionado
def Inserir():
    print("Inserir")
def Deletar():
    print("Deletar")
def Alterar():
    print("Alterar")
def Voltar():
    print("Voltar")

# Criando a janela principal
tela = tk.Tk()
tela.title("Doações Adm")
tela.geometry("700x500")

#Criando Frames
Tabela_frame = tk.Frame(tela)
Botao_frame = tk.Frame(tela)

#Colocando frames à tela
Tabela_frame.pack(pady=20)
Botao_frame.pack()

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

#Criando botão (Button)
Inserir_button = tk.Button(Botao_frame, text="Inserir", command=Inserir, font=fonte)
Deletar_button = tk.Button(Botao_frame, text="Deletar", command=Deletar, font=fonte)
Alterar_button = tk.Button(Botao_frame, text="Alterar", command=Alterar, font=fonte)
Voltar_button = tk.Button(Botao_frame, text="Voltar", command=Voltar, font=fonte)

#Colocando elementos à tela
Inserir_button.pack()
Deletar_button.pack(pady=20)
Alterar_button.pack()
Voltar_button.pack(pady=20)

# Rodando o loop da interface
tela.mainloop()
