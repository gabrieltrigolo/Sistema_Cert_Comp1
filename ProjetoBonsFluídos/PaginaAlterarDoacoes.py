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
def Alterar():
    categoria = Categoria_combobox.get()
    alterado = Alteracao_entry.get()
    print(categoria + " " + alterado+ " Alterar")

def Voltar():
    print("Voltar")

# Criando a janela principal
tela = tk.Tk()
tela.title("Alterar Doações")
tela.geometry("700x500")

# Criando Frames
Tabela_frame = tk.Frame(tela)
Entrada_frame = tk.Frame(tela)
Botao_frame = tk.Frame(tela)

# Posicionando os frames
Tabela_frame.pack(pady=10)
Entrada_frame.pack(pady=10)
Botao_frame.pack(pady=10)

# Label e Campo de Entrada
lbl_id = tk.Label(Entrada_frame, text="ID:", font=fonte)
lbl_id.grid(row=0, column=0, padx=5, pady=5)
ent_id = tk.Entry(Entrada_frame, font=fonte)
ent_id.grid(row=0, column=1, padx=5, pady=5)
Categoria_label = tk.Label(Entrada_frame, text="Categoria:", font=fonte)
Categoria_label.grid(row=1, column=0, padx=5, pady=5)
Categoria_combobox = ttk.Combobox(Entrada_frame, values=["Nome", "Data", "Validade"], font=fonte, width=37)
Categoria_combobox.current(0)
Categoria_combobox.grid(row=1, column=1, padx=5, pady=5)
Alteracao_label = tk.Label(Entrada_frame, text="Alteração:", font=fonte)
Alteracao_label.grid(row=2, column=0, padx=5, pady=5)
Alteracao_entry = tk.Entry(Entrada_frame, font=fonte)
Alteracao_entry.grid(row=2, column=1, padx=5, pady=5)

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
dados = [(1, "Pedro", 22), (2, "Ana", 25), (3, "João", 30),]
for dado in dados:
    tree.insert("", tk.END, values=dado)

# Posicionando a tabela na janela
tree.pack(expand=True, fill="both")

# Criando botões
Deletar_button = tk.Button(Botao_frame, text="Alterar", command=Alterar, font=fonte, **conf_Button)
Voltar_button = tk.Button(Botao_frame, text="Voltar", command=Voltar, font=fonte, **conf_Button)

# Posicionando os botões
Deletar_button.pack(side=tk.LEFT, padx=10)
Voltar_button.pack(side=tk.LEFT, padx=10)

# Rodando o loop da interface
tela.mainloop()
