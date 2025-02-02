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
def Configurar():
    print("Configurar")

def Voltar():
    print("Voltar")

def toggle_habilitar():
    if habilitar_var.get():
        print("Habilitado")
    else:
        print("Desabilitado")

# Criando a janela principal
tela = tk.Tk()
tela.title("Notificação")
tela.geometry("500x300")

# Criando Frame
Entrada_frame = tk.Frame(tela)
Botao_frame = tk.Frame(tela)

# Posicionando os frames
Entrada_frame.pack(pady=10)
Botao_frame.pack(pady=10)

# Labels e Campos de Entrada
lbl_categoria = tk.Label(Entrada_frame, text="Categoria:", font=fonte)
lbl_categoria.grid(row=0, column=0, padx=5, pady=5)
ent_categoria = ttk.Combobox(Entrada_frame, values=["Administrador", "Usuário", "Visitante"], font=fonte, width=20)
ent_categoria.current(0)
ent_categoria.grid(row=0, column=1, padx=5, pady=5)

lbl_estoque = tk.Label(Entrada_frame, text="Quantidade de Estoque:", font=fonte)
lbl_estoque.grid(row=1, column=0, padx=5, pady=5)

# Criando Entry que aceita apenas números
def validar_entrada(P):
    return P.isdigit() or P == ""

vcmd = (tela.register(validar_entrada), "%P")
ent_estoque = tk.Entry(Entrada_frame, font=fonte, validate="key", validatecommand=vcmd)
ent_estoque.grid(row=1, column=1, padx=5, pady=5)

# Criando Checkbutton
habilitar_var = tk.BooleanVar()
check_habilitar = tk.Checkbutton(Entrada_frame, text="Habilitar", font=fonte, variable=habilitar_var, command=toggle_habilitar)
check_habilitar.grid(row=2, column=0, columnspan=2, pady=10)

# Criando botões
Configurar_button = tk.Button(Botao_frame, text="Configurar", command=Configurar, font=fonte, **conf_Button)
Voltar_button = tk.Button(Botao_frame, text="Voltar", command=Voltar, font=fonte, **conf_Button)

# Posicionando os botões
Configurar_button.pack(side=tk.LEFT, padx=10)
Voltar_button.pack(side=tk.LEFT, padx=10)

# Rodando o loop da interface
tela.mainloop()
