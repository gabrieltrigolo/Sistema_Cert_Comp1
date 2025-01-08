from datetime import date
from ..model.Produto import Produto
from ..model.Beneficiario import Beneficiario

class Distribuicao:
    def __init__(self, idDistribuicao=None, beneficiario=None, dataDistribuicao=None, produto=None, quantidade=None):
        self._idDistribuicao = idDistribuicao
        self._beneficiario = beneficiario
        self._dataDistribuicao = dataDistribuicao
        self._produto = produto
        self._quantidade = quantidade

    @property
    def idDistribuicao(self):
        return self._idDistribuicao

    @idDistribuicao.setter
    def idDistribuicao(self, value):
        self._idDistribuicao = value

    @property
    def beneficiario(self):
        return self._beneficiario

    @beneficiario.setter
    def beneficiario(self, value: Beneficiario):
        if not isinstance(value, Beneficiario) and value is not None:
            raise TypeError("O beneficiário deve ser uma instância de Beneficiario ou None.")
        self._beneficiario = value

    @property
    def dataDistribuicao(self):
        return self._dataDistribuicao

    @dataDistribuicao.setter
    def dataDistribuicao(self, value):
        if not isinstance(value, (date, type(None))):
            raise TypeError("A data de distribuição deve ser uma instância de datetime.date ou None.")
        self._dataDistribuicao = value

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

    def __repr__(self):
        return (
            f"Distribuicao(idDistribuicao={self.idDistribuicao}, "
            f"beneficiario={self.beneficiario}, dataDistribuicao={self.dataDistribuicao}, "
            f"produto={self.produto}, quantidade={self.quantidade})"
        )
