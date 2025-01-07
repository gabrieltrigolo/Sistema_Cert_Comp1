class Produto:
    def __init__(self, nome, categoria, quantidade, validade, lote):
        self.__nome = nome
        self.__categoria = categoria
        self.__quantidade = quantidade
        self.__validade = validade
        self.__lote = lote

    def getNome(self):
        return self.__nome

    def setNome(self, nome):
        self.__nome = nome

    def getCategoria(self):
        return self.__categoria

    def setCategoria(self, categoria):
        self.__categoria = categoria

    def getQuantidade(self):
        return self.__quantidade

    def setQuantidade(self, quantidade):
        self.__quantidade = quantidade

    def getValidade(self):
        return self.__validade

    def setValidade(self, validade):
        self.__validade = validade

    def getLote(self):
        return self.__lote

    def setLote(self, lote):
        self.__lote = lote