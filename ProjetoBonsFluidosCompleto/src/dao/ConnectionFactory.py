import mysql.connector
from mysql.connector import Error

class ConnectionFactory:
    @staticmethod
    def get_connection():
        """
        Retorna uma conexão com o banco de dados.
        """
        try:
            connection = mysql.connector.connect(
                host='localhost',
                user='root',
                password='123456',
                database='testeprojeto',
            )
            if connection.is_connected():
                return connection
        except Error as e:
            raise RuntimeError(f"Erro ao conectar ao banco de dados: {e}")
