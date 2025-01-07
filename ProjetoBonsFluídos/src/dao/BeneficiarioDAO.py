import mysql.connector
from mysql.connector import Error
from model.Beneficiario import Beneficiario

class BeneficiarioDAO:
    def __init__(self, host, database, user, password):
        self.host = host
        self.database = database
        self.user = user
        self.password = password

    def get_connection(self):
        try:
            connection = mysql.connector.connect(
                host=self.host,
                database=self.database,
                user=self.user,
                password=self.password
            )
            if connection.is_connected():
                return connection
        except Error as e:
            print(f"Erro ao conectar ao MySQL: {e}")
            return None

    def inserir(self, beneficiario):
        sql = """
        INSERT INTO beneficiario (nome, email)
        VALUES (%s, %s)
        """
        try:
            conn = self.get_connection()
            if conn:
                cursor = conn.cursor()
                cursor.execute(sql, (
                    beneficiario.nome,
                    beneficiario.email,
                ))
                conn.commit()
                if cursor.rowcount > 0:
                    print("Beneficiario cadastrado com sucesso!")
                else:
                    print("Beneficiario não cadastrado.")
                cursor.close()
                conn.close()
        except Error as e:
            print(f"Erro ao inserir Beneficiario: {e}")
