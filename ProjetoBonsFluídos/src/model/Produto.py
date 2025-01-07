class Produto:
    def __init__(self, produto_id=None, nome=None, preco_unitario=0.0, quantidade=0, categoria=None, preco_custo=0.0):
        
        self._produto_id = produto_id
        self._nome = nome
        self._preco_unitario = preco_unitario
        self._quantidade = quantidade
        self._categoria = categoria
        self._preco_custo = preco_custo

    @property
    def produto_id(self):
        return self._produto_id

    @produto_id.setter
    def produto_id(self, value):
        self._produto_id = value

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, value):
        self._nome = value

    @property
    def preco_unitario(self):
        return self._preco_unitario

    @preco_unitario.setter
    def preco_unitario(self, value):
        self._preco_unitario = value

    @property
    def quantidade(self):
        return self._quantidade

    @quantidade.setter
    def quantidade(self, value):
        self._quantidade = value

    @property
    def categoria(self):
        return self._categoria

    @categoria.setter
    def categoria(self, value):
        self._categoria = value

    @property
    def preco_custo(self):
        return self._preco_custo

    @preco_custo.setter
    def preco_custo(self, value):
        self._preco_custo = value

    def __eq__(self, other):
        if isinstance(other, Produto):
            return self.produto_id == other.produto_id
        return False

    def __hash__(self):
        return hash(self.produto_id)

    def __repr__(self):
        return (
            f"Produto(produto_id={self.produto_id}, nome='{self.nome}', "
            f"preco_unitario={self.preco_unitario:.2f}, quantidade={self.quantidade}, "
            f"categoria='{self.categoria}', preco_custo={self.preco_custo:.2f})"
        )
