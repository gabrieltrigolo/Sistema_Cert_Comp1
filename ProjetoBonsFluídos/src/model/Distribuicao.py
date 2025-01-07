from Beneficiario import Beneficiario
from Produto import Produto
from datetime import date
from typing import List

class Distribuicao:
    def __init__(self, idDistribuicao=None, beneficiario=None, dataDistribuicao=None, produtos=None):

        self._idDistribuicao = idDistribuicao
        self._beneficiario = beneficiario
        self._dataDistribuicao = dataDistribuicao
        self._produtos = produtos if produtos is not None else []

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
    def beneficiario(self, value):
        self._beneficiario = value

    @property
    def dataDistribuicao(self):
        return self._dataDistribuicao

    @dataDistribuicao.setter
    def dataDistribuicao(self, value):
        self._dataDistribuicao = value

    @property
    def produtos(self):
        return self._produtos

    @produtos.setter
    def produtos(self, value: List):
        self._produtos = value

    def __repr__(self):
        return (
            f"Distribuicao(idDistribuicao={self.idDistribuicao}, "
            f"beneficiario={self.beneficiario}, dataDistribuicao={self.dataDistribuicao}, "
            f"produtos={self.produtos})"
        )
