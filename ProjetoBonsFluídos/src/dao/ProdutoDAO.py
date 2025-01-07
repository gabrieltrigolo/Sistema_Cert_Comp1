import mysql.connector
from mysql.connector import Error
from model.Produto import Produto

class ProdutoDAO:
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

    def inserir(self, produto):
        sql = """
        INSERT INTO produto (nome, categoria, quantidade, validade, lote)
        VALUES (%s, %s, %s, %s, %s)
        """
        try:
            conn = self.get_connection()
            if conn:
                cursor = conn.cursor()
                cursor.execute(sql, (
                    produto.nome,
                    produto.categoria,
                    produto.quantidade,
                    produto.validade,
                    produto.lote
                ))
                conn.commit()
                if cursor.rowcount > 0:
                    print("Produto cadastrado com sucesso!")
                else:
                    print("Produto não cadastrado.")
                cursor.close()
                conn.close()
        except Error as e:
            print(f"Erro ao inserir produto: {e}")

    def atualizar(self, produto):
        sql = """
        UPDATE produto
        SET nome = %s, categoria = %s, quantidade = %s, validade = %s, lote = %s
        WHERE produto_id = %s
        """
        try:
            conn = self.get_connection()
            if conn:
                cursor = conn.cursor()
                cursor.execute(sql, (
                    produto.nome,
                    produto.categoria,
                    produto.quantidade,
                    produto.validade,
                    produto.lote,
                    produto.idProduto
                ))
                conn.commit()
                if cursor.rowcount > 0:
                    print("Produto atualizado com sucesso!")
                else:
                    print("Produto não encontrado ou não houve alterações.")
                cursor.close()
                conn.close()
        except Error as e:
            print(f"Erro ao atualizar produto: {e}")
