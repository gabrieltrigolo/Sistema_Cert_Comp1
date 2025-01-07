import mysql.connector
from mysql.connector import Error
from datetime import date
from model.Beneficiario import Beneficiario
from model.Produto import Produto

class DistribuicaoDAO:
    def __init__(self, db_config):
        """
        Inicializa o DAO com as configurações do banco de dados.
        :param db_config: Um dicionário com as configurações do banco (host, user, password, database)
        """
        self.db_config = db_config

    def get_connection(self):
        """
        Obtém a conexão com o banco de dados.
        """
        try:
            connection = mysql.connector.connect(**self.db_config)
            if connection.is_connected():
                return connection
        except Error as e:
            print(f"Erro ao conectar ao MySQL: {e}")
            return None

    def inserir(self, distribuicao):
        """
        Insere uma nova distribuição no banco de dados.
        :param distribuicao: Objeto da classe Distribuicao a ser inserido.
        """
        if not distribuicao or not distribuicao.beneficiario or not distribuicao.produtos:
            raise ValueError("Distribuição, beneficiário e produtos não podem ser nulos.")

        # SQL Statements
        insert_distribuicao_sql = """
            INSERT INTO distribuicao (beneficiario_id, data_distribuicao) 
            VALUES (%s, %s)
        """
        insert_produtos_distribuicao_sql = """
            INSERT INTO distribuicao_produtos (distribuicao_id, produto_id, quantidade) 
            VALUES (%s, %s, %s)
        """
        update_produto_sql = """
            UPDATE produto SET quantidade = quantidade - %s WHERE produto_id = %s
        """

        connection = None
        cursor = None

        try:
            # Conectar ao banco de dados
            connection = self.get_connection()
            cursor = connection.cursor()

            # Desabilitar commit automático
            connection.autocommit = False

            # Inserir a distribuição
            cursor.execute(insert_distribuicao_sql, (
                distribuicao.beneficiario.id,
                distribuicao.data_distribuicao,
            ))
            distribuicao_id = cursor.lastrowid  # Obter o ID gerado para a distribuição

            # Inserir produtos da distribuição
            for produto in distribuicao.produtos:
                if produto.quantidade <= 0:
                    raise ValueError(f"Quantidade inválida para o produto {produto.nome}.")
                
                # Verificar a quantidade disponível no estoque
                cursor.execute("SELECT quantidade FROM produto WHERE produto_id = %s", (produto.id,))
                estoque = cursor.fetchone()
                if estoque is None or estoque[0] < produto.quantidade:
                    raise ValueError(f"Estoque insuficiente para o produto {produto.nome}.")

                # Inserir o produto na tabela de distribuição_produtos
                cursor.execute(insert_produtos_distribuicao_sql, (
                    distribuicao_id,
                    produto.id,
                    produto.quantidade,
                ))

                # Atualizar o estoque do produto
                cursor.execute(update_produto_sql, (produto.quantidade, produto.id))

            # Confirmar a transação
            connection.commit()
            print("Distribuição cadastrada com sucesso!")
        
        except Error as e:
            if connection:
                connection.rollback()
            print(f"Erro ao inserir distribuição: {e}")
        
        finally:
            # Fechar os recursos
            if cursor:
                cursor.close()
            if connection:
                connection.close()

    def atualizar(self, distribuicao):
        """
        Atualiza uma distribuição no banco de dados.
        :param distribuicao: Objeto da classe Distribuicao a ser atualizado.
        """
        sql_distribuicao = """
        UPDATE distribuicao
        SET beneficiario_id = %s, data_distribuicao = %s
        WHERE distribuicao_id = %s
        """
        sql_produtos_distribuicao = """
        UPDATE distribuicao_produtos
        SET quantidade = %s
        WHERE distribuicao_id = %s AND produto_id = %s
        """
        try:
            conn = self.get_connection()
            if conn:
                cursor = conn.cursor()

                # Atualizar a distribuição
                cursor.execute(sql_distribuicao, (
                    distribuicao.beneficiario.id,
                    distribuicao.data_distribuicao,  # corrigido para o nome correto
                    distribuicao.idDistribuicao
                ))

                # Atualizar os produtos na distribuição
                for produto in distribuicao.produtos:
                    cursor.execute(sql_produtos_distribuicao, (
                        produto.quantidade,
                        distribuicao.idDistribuicao,
                        produto.id
                    ))

                conn.commit()
                print("Distribuição atualizada com sucesso!")

                cursor.close()
                conn.close()

        except Error as e:
            print(f"Erro ao atualizar distribuição: {e}")
