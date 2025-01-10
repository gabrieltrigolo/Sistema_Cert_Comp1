from ..dao.ConnectionFactory import ConnectionFactory
from ..model.Doacao import Doacao
from ..model.Produto import Produto
from ..model.Beneficiario import Beneficiario

class DoacaoDAO:

    def inserir(self, doacao):
        if not doacao or not doacao.beneficiario or not doacao.produto:
            raise ValueError("Doação, beneficiário e produto não podem ser nulos.")

        insert_doacao_sql = """
            INSERT INTO doacao (beneficiario_id, produto_id, data_doacao, quantidade)
            VALUES (%s, %s, %s, %s)
        """
        update_produto_sql = """
            UPDATE produto SET quantidade = quantidade - %s WHERE produto_id = %s
        """

        try:
            # Conectar ao banco de dados
            conn = ConnectionFactory.get_connection()
            with conn.cursor() as cursor:
                # Desabilitar commit automático
                conn.autocommit = False

                if doacao.produto.quantidade <= 0:
                    raise ValueError(f"Quantidade inválida para o produto {doacao.produto.nome}.")

                # Verificar a quantidade disponível no estoque
                cursor.execute("SELECT quantidade FROM produto WHERE produto_id = %s", (doacao.produto.idProduto,))
                estoque = cursor.fetchone()
                if estoque is None or estoque[0] < doacao.produto.quantidade:
                    raise ValueError(f"Estoque insuficiente para o produto {doacao.produto.nome}.")

                # Inserir os dados na tabela `doacao`
                cursor.execute(insert_doacao_sql, (
                    doacao.beneficiario.idBeneficiario,
                    doacao.produto.idProduto,
                    doacao.dataDoacao,
                    doacao.quantidade,
                ))

                # Atualizar o estoque do produto
                cursor.execute(update_produto_sql, (doacao.quantidade, doacao.produto.idProduto))
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
                d.doacao_id AS doacao_id,
                b.nome AS beneficiario_nome,
                b.email AS beneficiario_email,
                b.cnpj_cpf AS beneficiario_cnpj_cpf,
                p.nome AS produto_nome,
                p.descricao AS produto_descricao,
                d.data_doacao AS data_doacao,
                d.quantidade AS quantidade_doada
            FROM
                doacao d
            JOIN
                beneficiario b ON d.beneficiario_id = b.beneficiario_id
            JOIN
                produto p ON d.produto_id = p.produto_id
            WHERE
                d.doacao_id = %s;
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
        sql_doacao = """
        UPDATE doacao
        SET beneficiario_id = %s, data_doacao = %s
        WHERE doacao_id = %s
        """
        sql_produtos_doacao = """
        UPDATE doacao_produtos
        SET quantidade = %s
        WHERE doacao_id = %s AND produto_id = %s
        """
        try:
            conn = ConnectionFactory.get_connection()
            if conn:
                cursor = conn.cursor()

                # Atualizar a doação
                cursor.execute(sql_doacao, (
                    doacao.beneficiario.idBeneficiario,
                    doacao.dataDoacao,
                    doacao.idDoacao
                ))

                # Atualizar os produtos na doação
                cursor.execute(sql_produtos_doacao, (
                    doacao.quantidade,
                    doacao.idDoacao,
                    doacao.produto.idProduto
                ))

                conn.commit()
                print("Doação atualizada com sucesso!")

                cursor.close()
                conn.close()

        except Exception as e:
            print(f"Erro ao atualizar doação: {e}")

