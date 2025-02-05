import tkinter as tk


class PaginaDados:
    def __init__(self):
        # Configurações iniciais
        self.fonte = ("Arial", 12)
        self.conf_Button = {
            "width": 5,
            "height": 1,
            "padx": 10,
            "pady": 5
        }

        # Criando Tela
        self.tela = tk.Tk()
        self.tela.title("Dados")
        self.tela.geometry("700x400")

        # Criando Frames
        self.Botao_frame = tk.Frame(self.tela)

        # Colocando frames à tela
        self.Botao_frame.pack(pady=50)

        # Criando botões
        self.criar_botoes()

    def criar_botoes(self):
        # Criando botões (Button)
        Inserir_button = tk.Button(self.Botao_frame, text="Doações", command=self.doacao, font=self.fonte, **self.conf_Button)
        Deletar_button = tk.Button(self.Botao_frame, text="Estoques", command=self.estoque, font=self.fonte, **self.conf_Button)
        AlterarUsuario_button = tk.Button(self.Botao_frame, text="Beneficiários", command=self.beneficiarios, font=self.fonte, **self.conf_Button)
        Voltar_button = tk.Button(self.Botao_frame, text="Voltar", command=self.voltar, font=self.fonte, **self.conf_Button)

        # Colocando elementos à tela
        Inserir_button.pack(pady=20)
        Deletar_button.pack(pady=20)
        AlterarUsuario_button.pack(pady=20)
        Voltar_button.pack(pady=20)

    def doacao(self):
        print("doação")

    def estoque(self):
        print("estoque")

    def beneficiarios(self):
        print("beneficiário")

    def voltar(self):
        print("voltouuu")


