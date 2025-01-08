class Produto:
    def __init__(self, idProduto=None, nome=None, descricao=None, quantidade=0, dataRecebimento=None):
        
        self._idProduto = idProduto
        self._nome = nome
        self._descricao = descricao
        self._quantidade = quantidade
        self._dataRecebimento = dataRecebimento

    @property
    def idProduto(self):
        return self._idProduto

    @idProduto.setter
    def idProduto(self, value):
        self._idProduto = value

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, value):
        self._nome = value

    @property
    def descricao(self):
        return self._descricao

    @descricao.setter
    def descricao(self, value):
        self._descricao = value

    @property
    def quantidade(self):
        return self._quantidade

    @quantidade.setter
    def quantidade(self, value):
        self._quantidade = value

    @property
    def dataRecebimento(self):
        return self._dataRecebimento

    @dataRecebimento.setter
    def dataRecebimento(self, value):
        self._dataRecebimento = value

    def __eq__(self, other):
        if isinstance(other, Produto):
            return self.idProduto == other.idProduto
        return False

    def __hash__(self):
        return hash(self.idProduto)

    def __repr__(self):
        return (
            f"Produto(idProduto={self.idProduto}, nome='{self.nome}', descricao='{self.descricao}', "
            f"quantidade={self.quantidade}, dataRecebimento='{self.dataRecebimento}')"
        )
