from ..dao.ConnectionFactory import ConnectionFactory

class RelatorioDAO:

    def distribuicoes_por_mes(self, mes, ano):
        """
        Retorna as distribuições realizadas em um mês e ano específicos.
        """
        sql_query = """
        SELECT d.data_distribuicao, b.nome AS beneficiario, p.nome AS produto, d.quantidade
        FROM distribuicao d
        JOIN beneficiario b ON d.beneficiario_id = b.beneficiario_id
        JOIN produto p ON d.produto_id = p.produto_id
        WHERE MONTH(d.data_distribuicao) = %s AND YEAR(d.data_distribuicao) = %s
        """
        try:
            conn = ConnectionFactory.get_connection()
            if conn:
                cursor = conn.cursor(dictionary=True)
                cursor.execute(sql_query, (mes, ano))
                resultados = cursor.fetchall()

                cursor.close()
                conn.close()
                return resultados
        except Exception as e:
            raise e

    def doacoes_por_doador(self):
        """
        Retorna o total de doações feitas por cada doador.
        """
        sql_query = """
        SELECT d.doador, SUM(d.quantidade) AS total_doacoes
        FROM doacao d
        GROUP BY d.doador
        ORDER BY total_doacoes DESC
        """
        try:
            conn = ConnectionFactory.get_connection()
            if conn:
                cursor = conn.cursor(dictionary=True)
                cursor.execute(sql_query)
                resultados = cursor.fetchall()

                cursor.close()
                conn.close()
                return resultados
        except Exception as e:
            raise e

    def beneficiarios_mais_produtos(self):
        """
        Retorna os beneficiários que receberam a maior quantidade de produtos.
        """
        sql_query = """
        SELECT b.nome AS beneficiario, SUM(d.quantidade) AS total_recebido
        FROM distribuicao d
        JOIN beneficiario b ON d.beneficiario_id = b.beneficiario_id
        GROUP BY b.beneficiario_id
        ORDER BY total_recebido DESC
        LIMIT 10  -- Retorna os 10 principais beneficiários
        """
        try:
            conn = ConnectionFactory.get_connection()
            if conn:
                cursor = conn.cursor(dictionary=True)
                cursor.execute(sql_query)
                resultados = cursor.fetchall()

                cursor.close()
                conn.close()
                return resultados
        except Exception as e:
            raise e
