import tkinter as tk
from tkinter import ttk, messagebox
from src.dao.DoacaoDAO import DoacaoDAO  # Importar o DAO correto


class PaginaDeletarDoacao:
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
        self.tela.title("Deletar Doação")
        # Definir o tamanho da janela
        largura_janela = 900
        altura_janela = 500
        # Obter o tamanho da tela
        largura_tela = self.tela.winfo_screenwidth()
        altura_tela = self.tela.winfo_screenheight()
        # Calcular a posição x e y para centralizar a janela
        pos_x = (largura_tela - largura_janela) // 2
        pos_y = (altura_tela - altura_janela) // 2
        # Definir a geometria da janela
        self.tela.geometry(f"{largura_janela}x{altura_janela}+{pos_x}+{pos_y}")

        # Criando Frames
        self.Tabela_frame = tk.Frame(self.tela)
        self.Entrada_frame = tk.Frame(self.tela)
        self.Botao_frame = tk.Frame(self.tela)

        # Posicionando os frames
        self.Tabela_frame.pack(pady=10)
        self.Entrada_frame.pack(pady=10)
        self.Botao_frame.pack(pady=10)

        # Criando Label e Campo de Entrada
        self.criar_entrada()

        # Criando a tabela
        self.criar_tabela()

        # Criando botões
        self.criar_botoes()

    def criar_entrada(self):
        lbl_id = tk.Label(self.Entrada_frame, text="ID da Doação:", font=self.fonte)
        lbl_id.grid(row=0, column=0, padx=5, pady=5)

        self.ent_id = tk.Entry(self.Entrada_frame, font=self.fonte)
        self.ent_id.grid(row=0, column=1, padx=5, pady=5)

    def criar_tabela(self):
        columns = ("Doação ID", "Nome do Produto", "Doador", "Quantidade", "Data da Doação")
        self.tree = ttk.Treeview(self.Tabela_frame, columns=columns, show="headings")

        # Definindo os títulos das colunas
        for col in columns:
            self.tree.heading(col, text=col)

        # Definindo o tamanho das colunas
        self.tree.column("Doação ID", width=150)
        self.tree.column("Nome do Produto", width=150)
        self.tree.column("Doador", width=200)
        self.tree.column("Quantidade", width=150)
        self.tree.column("Data da Doação", width=150)

        self.atualizar_tabela()

        # Posicionando a tabela na janela
        self.tree.pack(expand=True, fill="both")

    def atualizar_tabela(self):
        for item in self.tree.get_children():
            self.tree.delete(item)

        dao = DoacaoDAO()  # Usar o DAO correto para buscar doações
        doacoes = dao.listarTodasDoacoes()
        for doacao in doacoes:
            campos_filtrados = (
                doacao[0],  # Doação ID
                doacao[5],  # Produto ID
                doacao[4],  # Doador
                doacao[3],  # Quantidade
                doacao[2]  # Data da Doação
            )
            self.tree.insert("", tk.END, values=campos_filtrados)

    def criar_botoes(self):
        Deletar_button = tk.Button(self.Botao_frame, text="Deletar", command=self.deletar, font=self.fonte,
                                   **self.conf_Button)
        Voltar_button = tk.Button(self.Botao_frame, text="Voltar", command=self.voltar, font=self.fonte,
                                  **self.conf_Button)

        # Posicionando os botões
        Deletar_button.pack(side=tk.LEFT, padx=10)
        Voltar_button.pack(side=tk.LEFT, padx=10)

    def deletar(self):
        id = self.ent_id.get().strip()

        if not id.isdigit():
            messagebox.showerror("Erro", "Por favor, insira um ID válido (somente números).")
            return

        dao = DoacaoDAO()

        try:
            doacao = dao.buscarPorId(id)  # Nova função para verificar existência
            if not doacao:
                messagebox.showerror("Erro", "Doação não encontrada!")
                return

            confirmacao = messagebox.askyesno("Confirmar", f"Tem certeza que deseja deletar a doação ID {id}?")
            if confirmacao:
                dao.deletarDoacaoPorId(id)
                self.atualizar_tabela()
                messagebox.showinfo("Sucesso", "Doação deletada com sucesso!")

        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao deletar a doação: {e}")

    def voltar(self):
        self.tela.destroy()
