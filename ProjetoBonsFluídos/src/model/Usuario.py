from datetime import date

class Usuario:
    def __init__(self, idUsuario=None, nome=None, email=None, senha=None, cargo=None):
        self._idUsuario = idUsuario
        self._nome = nome
        self._email = email
        self._senha = senha
        self._cargo = cargo

    @property
    def idUsuario(self):
        return self._idUsuario

    @idUsuario.setter
    def idUsuario(self, value):
        self._idUsuario = value

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, value):
        if not isinstance(value, str):
            raise TypeError("O nome deve ser uma string.")
        self._nome = value

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, value):
        if not isinstance(value, str):
            raise TypeError("O email deve ser uma string.")
        self._email = value

    @property
    def senha(self):
        return self._senha

    @senha.setter
    def senha(self, value):
        if not isinstance(value, str):
            raise TypeError("A senha deve ser uma string.")
        self._senha = value

    @property
    def cargo(self):
        return self._cargo

    @cargo.setter
    def cargo(self, value):
        self._cargo = value

    def __repr__(self):
        return f"Usuario(idUsuario={self.idUsuario}, nome={self.nome}, email={self.email}, cargo={self.cargo})"
