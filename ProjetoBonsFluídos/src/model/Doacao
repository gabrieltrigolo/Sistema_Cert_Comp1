from datetime import date
from ..model.Produto import Produto
from ..model.Beneficiario import Beneficiario

class Doacao:
    def __init__(self, idDoacao=None, beneficiario=None, dataDoacao=None, produto=None, quantidade=None):
        self._idDoacao = idDoacao
        self._beneficiario = beneficiario
        self._dataDoacao = dataDoacao
        self._produto = produto
        self._quantidade = quantidade

    @property
    def idDoacao(self):
        return self._idDoacao

    @idDoacao.setter
    def idDoacao(self, value):
        self._idDoacao = value

    @property
    def beneficiario(self):
        return self._beneficiario

    @beneficiario.setter
    def beneficiario(self, value: Beneficiario):
        if not isinstance(value, Beneficiario) and value is not None:
            raise TypeError("O beneficiário deve ser uma instância de Beneficiario ou None.")
        self._beneficiario = value

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

    def __repr__(self):
        return (
            f"Doacao(idDoacao={self.idDoacao}, "
            f"beneficiario={self.beneficiario}, dataDoacao={self.dataDoacao}, "
            f"produto={self.produto}, quantidade={self.quantidade})"
        )
