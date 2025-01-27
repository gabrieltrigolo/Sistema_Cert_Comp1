from datetime import date
from ..model.Produto import Produto

class Doacao:
    def __init__(self, idDoacao=None, dataDoacao=None, produto=None, quantidade=None, responsavel=None):
        self._idDoacao = idDoacao
        self._dataDoacao = dataDoacao
        self._produto = produto
        self._quantidade = quantidade
        self._responsavel = responsavel

    @property
    def idDoacao(self):
        return self._idDoacao

    @idDoacao.setter
    def idDoacao(self, value):
        self._idDoacao = value

    @property
    def dataDoacao(self):
        return self._dataDoacao

    @dataDoacao.setter
    def dataDoacao(self, value):
        if not isinstance(value, (date, type(None))):
            raise TypeError("A data de doação deve ser uma instância de datetime.date ou None.")
        self._dataDoacao = value

    @property
    def produto(self):
        return self._produto

    @produto.setter
    def produto(self, value: Produto):
        if not isinstance(value, Produto) and value is not None:
            raise TypeError("O produto deve ser uma instância de Produto ou None.")
        self._produto = value

    @property
    def quantidade(self):
        return self._quantidade

    @quantidade.setter
    def quantidade(self, value):
        if not isinstance(value, (int, type(None))):
            raise TypeError("A quantidade deve ser um número inteiro ou None.")
        self._quantidade = value

    @property
    def responsavel(self):
        return self._responsavel

    @responsavel.setter
    def responsavel(self, value):
        self._responsavel = value

    def __repr__(self):
        return (
            f"Doacao(idDoacao={self.idDoacao}, "
            f"dataDoacao={self.dataDoacao}, "
            f"produto={self.produto}, quantidade={self.quantidade}),responsavel={self.responsavel})"
        )
