from ..dao.ConnectionFactory import ConnectionFactory
from ..model.Doacao import Doacao
from ..model.Produto import Produto

class DoacaoDAO:

    def inserir(self, doacao):
        if not doacao  or not doacao.produto:
            raise ValueError("Doação e produto não podem ser nulos.")

        # Inserir o produto na tabela produto
        query_inserir_produto = """
                        INSERT INTO produto (nome, descricao, quantidade, data_doacao)
                        VALUES (%s, %s, %s, %s)
                    """
        # Inserir a doação na tabela doacao
        query_inserir_doacao = """
                        INSERT INTO doacao (produto_id, data_doacao, quantidade, doador)
                        VALUES (%s, %s, %s, %s)
                    """

        try:
            # Conectar ao banco de dados
            conn = ConnectionFactory.get_connection()
            with conn.cursor() as cursor:
                # Desabilitar commit automático
                conn.autocommit = False

                cursor.execute(query_inserir_produto, (
                    doacao.produto.nome,
                    doacao.produto.descricao,
                    doacao.produto.quantidade,
                    doacao.produto.dataRecebimento))
                # Obter o ID do produto inserido
                produto_id = cursor.lastrowid

                # Inserir os dados na tabela `doacao`
                cursor.execute(query_inserir_doacao, (
                    produto_id,
                    doacao.dataDoacao,
                    doacao.quantidade,
                    doacao.responsavel
                ))

                # Confirmar a transação
                conn.commit()
                print("Doação cadastrada com sucesso!")

        except Exception as e:
            if conn:
                conn.rollback()
            print(f"Erro ao inserir doação: {e}")
            raise
        finally:
            if conn:
                conn.close()

    def buscarPorId(self, doacao_id):
        select_doacao_sql = """
            SELECT 
                d.doacao_id,
                d.doador,
                p.nome AS nome_produto,
                p.descricao,
                d.quantidade AS quantidade_doada,
                d.data_doacao
            FROM doacao d
            INNER JOIN produto p ON d.produto_id = p.produto_id
            WHERE doacao_id = %s
            ORDER BY d.data_doacao DESC;
        """

        try:
            # Conectar ao banco de dados
            conn = ConnectionFactory.get_connection()
            with conn.cursor() as cursor:
                cursor.execute(select_doacao_sql, (doacao_id,))
                result = cursor.fetchone()
                if result:
                    return result
                else:
                    return None

        except Exception as e:
            print(f"Erro ao buscar doação por ID: {e}")
            raise

        finally:
            if conn:
                conn.close()

    def atualizar(self, doacao):
        if not doacao or not doacao.produto:
            raise ValueError("Doação e produto não podem ser nulos.")

        # Query para atualizar a tabela produto
        query_atualizar_produto = """
            UPDATE produto 
            SET nome = %s,
                descricao = %s,
                quantidade = %s,
                data_doacao = %s
            WHERE produto_id = %s
        """

        # Query para atualizar a tabela doacao
        query_atualizar_doacao = """
            UPDATE doacao
            SET data_doacao = %s,
                quantidade = %s,
                doador = %s
            WHERE produto_id = %s
        """

        try:
            # Conectar ao banco de dados
            conn = ConnectionFactory.get_connection()
            with conn.cursor() as cursor:
                # Desabilitar commit automático
                conn.autocommit = False

                # Atualizar dados na tabela produto
                cursor.execute(query_atualizar_produto, (
                    doacao.produto.nome,
                    doacao.produto.descricao,
                    doacao.produto.quantidade,
                    doacao.produto.dataRecebimento,
                    doacao.produto.id
                ))

                # Atualizar dados na tabela doacao
                cursor.execute(query_atualizar_doacao, (
                    doacao.dataDoacao,
                    doacao.quantidade,
                    doacao.responsavel,
                    doacao.produto.id
                ))

                # Confirmar a transação
                conn.commit()
                print("Doação atualizada com sucesso!")

        except Exception as e:
            if conn:
                conn.rollback()
            print(f"Erro ao atualizar doação: {e}")
            raise
        finally:
            if conn:
                conn.close()


    def listarTodasDoacoes(self):
        # Consulta SQL para buscar todas as doações
        query_buscar_doacoes = """
                SELECT d.doacao_id, d.produto_id, d.data_doacao, d.quantidade, d.doador,
                       p.nome AS produto_nome, p.descricao AS produto_descricao, p.quantidade AS produto_quantidade
                FROM doacao d
                JOIN produto p ON d.produto_id = p.produto_id
            """

        try:
            # Conectar ao banco de dados
            conn = ConnectionFactory.get_connection()
            with conn.cursor() as cursor:
                cursor.execute(query_buscar_doacoes)
                doacoes = cursor.fetchall()  # Busca todas as doações

                # Formatar os resultados em uma lista de dicionários
                lista_doacoes = []
                for doacao in doacoes:
                    lista_doacoes.append((
                        doacao[0],
                        doacao[1],
                        doacao[2],
                        doacao[3],
                        doacao[4],
                        doacao[5],
                        doacao[6],
                        doacao[7]
                    ))

                return lista_doacoes  # Retorna a lista de doações

        except Exception as e:
            print(f"Erro ao buscar doações: {e}")
            raise
        finally:
            if conn:
                conn.close()

    def deletarDoacaoPorId(self, doacao_id):
        if not doacao_id:
            raise ValueError("ID da doação é obrigatório.")

        # SQL para buscar os dados da doação (produto_id e quantidade)
        select_doacao_sql = """
            SELECT produto_id, quantidade 
            FROM doacao 
            WHERE doacao_id = %s
        """

        # SQL para deletar a doação
        delete_doacao_sql = """
            DELETE FROM doacao 
            WHERE doacao_id = %s
        """

        # SQL para deletar o produto
        delete_produto_sql = """
            DELETE FROM produto 
            WHERE produto_id = %s
        """

        try:
            conn = ConnectionFactory.get_connection()
            with conn.cursor() as cursor:
                conn.autocommit = False

                # Buscar os dados da doação
                cursor.execute(select_doacao_sql, (doacao_id,))
                doacao = cursor.fetchone()

                if not doacao:
                    raise ValueError("Doação não encontrada com o ID fornecido.")

                produto_id, quantidade = doacao

                # Deletar a doação
                cursor.execute(delete_doacao_sql, (doacao_id,))

                # Deletar o produto
                cursor.execute(delete_produto_sql, (produto_id,))

                conn.commit()
                print("Doação e produto deletados com sucesso!")

        except Exception as e:
            if conn:
                conn.rollback()
            print(f"Erro ao deletar doação: {e}")
            raise

        finally:
            if conn:
                conn.close()
