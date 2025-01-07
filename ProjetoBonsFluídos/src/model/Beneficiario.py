class Beneficiario:
    def __init__(self, idBeneficiario=None, nome=None, email=None):
        self._idBeneficiario = idBeneficiario
        self._nome = nome
        self._email = email

    @property
    def idBeneficiario(self):
        return self._idBeneficiario

    @idBeneficiario.setter
    def idBeneficiario(self, value):
        self._idBeneficiario = value

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, value):
        self._nome = value

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, value):
        self._email = value

    def __eq__(self, other):
        if isinstance(other, Beneficiario):
            return self.idBeneficiario == other.idBeneficiario
        return False

    def __hash__(self):
        return hash(self.idBeneficiario)

    def __repr__(self):
        return f"Beneficiario(idBeneficiario={self.idBeneficiario}, nome='{self.nome}', email='{self.email}')"
