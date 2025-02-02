import tkinter as tk
from tkinter import ttk
from tkcalendar import DateEntry # type: ignore

# Criando dicionário de fontes e configs
fonte = ("Arial", 12)
conf_Button = {
    "width": 10,
    "height": 1,
    "padx": 10,
    "pady": 5
}

# Função quando botão for pressionado
def Inserir():
    data = date_data.get()
    print(data)

def Voltar():
    print("Voltar")

# Criando a janela principal
tela = tk.Tk()
tela.title("Inserir Doações")
tela.geometry("700x500")

# Criando Frame
Entrada_frame = tk.Frame(tela)
Botao_frame = tk.Frame(tela)

# Posicionando os frames
Entrada_frame.pack(pady=10)
Botao_frame.pack(pady=10)

# Labels e Campos de Entrada
lbl_nome = tk.Label(Entrada_frame, text="Nome:", font=fonte)
lbl_nome.grid(row=0, column=0, padx=5, pady=5)
ent_nome = tk.Entry(Entrada_frame, font=fonte)
ent_nome.grid(row=0, column=1, padx=5, pady=5)

lbl_data = tk.Label(Entrada_frame, text="Data:", font=fonte)
lbl_data.grid(row=1, column=0, padx=5, pady=5)
date_data = DateEntry(Entrada_frame, font=fonte, width=12, background='darkblue', foreground='white', borderwidth=2)
date_data.grid(row=1, column=1, padx=5, pady=5)

lbl_quantidade = tk.Label(Entrada_frame, text="Quantidade:", font=fonte)
lbl_quantidade.grid(row=2, column=0, padx=5, pady=5)
ent_quantidade = tk.Entry(Entrada_frame, font=fonte)
ent_quantidade.grid(row=2, column=1, padx=5, pady=5)

lbl_item = tk.Label(Entrada_frame, text="Item:", font=fonte)
lbl_item.grid(row=3, column=0, padx=5, pady=5)
combo_item = ttk.Combobox(Entrada_frame, font=fonte, values=["Item 1", "Item 2", "Item 3"])
combo_item.grid(row=3, column=1, padx=5, pady=5)

lbl_validade = tk.Label(Entrada_frame, text="Validade:", font=fonte)
lbl_validade.grid(row=4, column=0, padx=5, pady=5)
date_validade = DateEntry(Entrada_frame, font=fonte, width=12, background='darkblue', foreground='white', borderwidth=2)
date_validade.grid(row=4, column=1, padx=5, pady=5)

lbl_lote = tk.Label(Entrada_frame, text="Lote:", font=fonte)
lbl_lote.grid(row=5, column=0, padx=5, pady=5)
ent_lote = tk.Entry(Entrada_frame, font=fonte)
ent_lote.grid(row=5, column=1, padx=5, pady=5)

# Criando botões
Inserir_button = tk.Button(Botao_frame, text="Inserir", command=Inserir, font=fonte, **conf_Button)
Voltar_button = tk.Button(Botao_frame, text="Voltar", command=Voltar, font=fonte, **conf_Button)

# Posicionando os botões
Inserir_button.pack(side=tk.LEFT, padx=10)
Voltar_button.pack(side=tk.LEFT, padx=10)

# Rodando o loop da interface
tela.mainloop()
