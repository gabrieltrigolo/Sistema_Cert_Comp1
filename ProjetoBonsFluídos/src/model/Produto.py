class Produto:
    def __init__(self, idProduto=None, nome=None, categoria=None, quantidade=0, validade=None, lote=None):
        
        self._idProduto = idProduto
        self._nome = nome
        self._categoria = categoria
        self._quantidade = quantidade
        self._validade = validade
        self._lote = lote

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
    def categoria(self):
        return self._categoria

    @categoria.setter
    def categoria(self, value):
        self._categoria = value

    @property
    def quantidade(self):
        return self._quantidade

    @quantidade.setter
    def quantidade(self, value):
        self._quantidade = value

    @property
    def validade(self):
        return self._validade

    @validade.setter
    def validade(self, value):
        self._validade = value

    @property
    def lote(self):
        return self._lote

    @lote.setter
    def lote(self, value):
        self._lote = value

    def __eq__(self, other):
        if isinstance(other, Produto):
            return self.idProduto == other.idProduto
        return False

    def __hash__(self):
        return hash(self.idProduto)

    def __repr__(self):
        return (
            f"Produto(idProduto={self.idProduto}, nome='{self.nome}', categoria='{self.categoria}', "
            f"quantidade={self.quantidade}, validade='{self.validade}', lote='{self.lote}')"
        )
