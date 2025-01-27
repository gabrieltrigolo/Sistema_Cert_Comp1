from ..dao.ConnectionFactory import ConnectionFactory
from ..model.Produto import Produto
from ..model.Beneficiario import Beneficiario

class DistribuicaoDAO:

    def inserir(self, distribuicao):

        if not distribuicao or not distribuicao.beneficiario or not distribuicao.produto:
            raise ValueError("Distribuição, beneficiário e produto não podem ser nulos.")

        insert_distribuicao_sql = """
            INSERT INTO distribuicao (beneficiario_id, produto_id, data_distribuicao, quantidade)
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

                if distribuicao.produto.quantidade <= 0:
                    raise ValueError(f"Quantidade inválida para o produto {distribuicao.produto.nome}.")

                # Verificar a quantidade disponível no estoque
                cursor.execute("SELECT quantidade FROM produto WHERE produto_id = %s", (distribuicao.produto.idProduto,))
                estoque = cursor.fetchone()
                if estoque is None or estoque[0] < distribuicao.produto.quantidade:
                    raise ValueError(f"Estoque insuficiente para o produto {distribuicao.produto.nome}.")

                # Inserir os dados na tabela `distribuicao`
                cursor.execute(insert_distribuicao_sql, (
                    distribuicao.beneficiario.idBeneficiario,
                    distribuicao.produto.idProduto,
                    distribuicao.dataDistribuicao,
                    distribuicao.quantidade,
                ))

                # Atualizar o estoque do produto
                cursor.execute(update_produto_sql, (distribuicao.quantidade, distribuicao.produto.idProduto))
                # Confirmar a transação
                conn.commit()
                print("Distribuição cadastrada com sucesso!")

        except Exception as e:
            if conn:
                conn.rollback()
            print(f"Erro ao inserir distribuição: {e}")
            raise

        finally:
            if conn:
                conn.close()

    def inserirEspecial(self, produto_nome, beneficiario_id, quantidade, data_distribuicao):
        if not beneficiario_id or not produto_nome or quantidade <= 0:
            raise ValueError("Beneficiário, nome do produto e quantidade devem ser válidos.")

        # SQL para buscar os registros do produto pelo nome, ordenados por data de doação
        select_produto_sql = """
                    SELECT produto_id, quantidade 
                    FROM produto 
                    WHERE nome = %s AND quantidade > 0 
                    ORDER BY data_doacao ASC
                """
        # SQL para inserir distribuição
        insert_distribuicao_sql = """
                    INSERT INTO distribuicao (beneficiario_id, produto_id, data_distribuicao, quantidade)
                    VALUES (%s, %s, %s, %s)
                """
        # SQL para atualizar estoque
        update_produto_sql = """
                    UPDATE produto 
                    SET quantidade = quantidade - %s 
                    WHERE produto_id = %s
                """

        try:
            conn = ConnectionFactory.get_connection()
            with conn.cursor() as cursor:
                conn.autocommit = False

                # Buscar todos os registros do produto pelo nome no estoque
                cursor.execute(select_produto_sql, (produto_nome,))
                estoque = cursor.fetchall()

                if not estoque:
                    raise ValueError(f"Estoque do produto '{produto_nome}' está vazio ou indisponível.")

                quantidade_a_distribuir = quantidade
                for registro in estoque:
                    produto_id, quantidade_disponivel = registro
                    if quantidade_a_distribuir <= 0:
                        break

                    # Determinar a quantidade a retirar do registro atual
                    quantidade_a_retirar = min(quantidade_a_distribuir, quantidade_disponivel)

                    if quantidade_a_retirar > 0:  # Garantir que não inserimos registros com quantidade 0
                        # Inserir distribuição
                        cursor.execute(insert_distribuicao_sql, (
                            beneficiario_id,
                            produto_id,
                            data_distribuicao,
                            quantidade_a_retirar
                        ))

                        # Atualizar o estoque do produto
                        cursor.execute(update_produto_sql, (quantidade_a_retirar, produto_id))

                    # Atualizar a quantidade restante a distribuir
                    quantidade_a_distribuir -= quantidade_a_retirar

                # Verificar se toda a quantidade foi distribuída
                if quantidade_a_distribuir > 0:
                    raise ValueError(f"Estoque insuficiente para atender à quantidade solicitada de '{produto_nome}'.")

                conn.commit()
                print("Distribuição cadastrada com sucesso!")

        except Exception as e:
            if conn:
                conn.rollback()
            print(f"Erro ao inserir distribuição: {e}")
            raise

        finally:
            if conn:
                conn.close()

    def buscarPorId(self, distribuicao_id):
        select_distribuicao_sql = """
            SELECT
                d.distribuicao_id AS distribuicao_id,
                b.nome AS beneficiario_nome,
                b.email AS beneficiario_email,
                b.cnpj_cpf AS beneficiario_cnpj_cpf,
                p.nome AS produto_nome,
                p.descricao AS produto_descricao,
                d.data_distribuicao AS data_distribuicao,
                d.quantidade AS quantidade_distribuida
            FROM
                distribuicao d
            JOIN
                beneficiario b ON d.beneficiario_id = b.beneficiario_id
            JOIN
                produto p ON d.produto_id = p.produto_id
            WHERE
                d.distribuicao_id = %s;
        """

        try:
            # Conectar ao banco de dados
            conn = ConnectionFactory.get_connection()
            with conn.cursor() as cursor:
                cursor.execute(select_distribuicao_sql, (distribuicao_id,))
                result = cursor.fetchone()
                if result:
                    return result
                else:
                    return None

        except Exception as e:
            print(f"Erro ao buscar distribuição por ID: {e}")
            raise

        finally:
            if conn:
                conn.close()

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
            conn = ConnectionFactory.get_connection()
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

        except Exception as e:
            print(f"Erro ao atualizar distribuição: {e}")

    def buscarDistribuicoesPorBeneficiario(self, beneficiario_id):
        select_distribuicoes_sql = """
            SELECT 
                d.distribuicao_id,
                b.nome AS nome_beneficiario,
                p.nome AS nome_produto,
                d.quantidade,
                d.data_distribuicao
            FROM 
                distribuicao d
            JOIN 
                beneficiario b ON d.beneficiario_id = b.beneficiario_id
            JOIN 
                produto p ON d.produto_id = p.produto_id
            WHERE 
                d.beneficiario_id = %s
            ORDER BY 
                d.data_distribuicao DESC;
        """

        try:
            # Conectar ao banco de dados
            conn = ConnectionFactory.get_connection()
            with conn.cursor() as cursor:
                cursor.execute(select_distribuicoes_sql, (beneficiario_id,))
                result = cursor.fetchall()
                if result:
                    return result
                else:
                    return []

        except Exception as e:
            print(f"Erro ao buscar distribuições para o beneficiário {beneficiario_id}: {e}")
            raise

        finally:
            if conn:
                conn.close()

    # def relatorio_por_beneficiario(self, id_beneficiario):
    #     """
    #     Gera um relatório de todas as distribuições feitas a um beneficiário.
    #     :param id_beneficiario: ID do beneficiário.
    #     :return: Lista de distribuições feitas a esse beneficiário.
    #     """
    #     sql = """
    #     SELECT d.distribuicao_id, d.data_distribuicao, p.produto_id, p.nome, dp.quantidade
    #     FROM distribuicao d
    #     JOIN distribuicao_produtos dp ON d.distribuicao_id = dp.distribuicao_id
    #     JOIN produto p ON dp.produto_id = p.produto_id
    #     WHERE d.beneficiario_id = %s
    #     ORDER BY d.data_distribuicao DESC
    #     """
    #
    #     try:
    #         conn = ConnectionFactory.get_connection()
    #         if conn:
    #             cursor = conn.cursor()
    #
    #             # Consultar distribuições do beneficiário
    #             cursor.execute(sql, (id_beneficiario,))
    #             distribuições = {}
    #
    #             for row in cursor.fetchall():
    #                 distribuicao_id = row[0]
    #                 data_distribuicao = row[1]
    #                 produto_id = row[2]
    #                 nome_produto = row[3]
    #                 quantidade = row[4]
    #
    #                 if distribuicao_id not in distribuições:
    #                     distribuições[distribuicao_id] = {
    #                         'data_distribuicao': data_distribuicao,
    #                         'produtos': []
    #                     }
    #
    #                 # Adiciona o produto à lista de produtos da distribuição
    #                 produto = Produto(idProduto=produto_id, nome=nome_produto, quantidade=quantidade)
    #                 distribuições[distribuicao_id]['produtos'].append(produto)
    #
    #             # Organizar as distribuições em objetos Distribuicao
    #             relatorio = []
    #             for distribuicao_id, dados in distribuições.items():
    #                 # Criando o objeto Distribuicao
    #                 distribuicao = Distribuicao(idDistribuicao=distribuicao_id,
    #                                             dataDistribuicao=dados['data_distribuicao'])
    #                 distribuicao.produtos = dados['produtos']
    #                 relatorio.append(distribuicao)
    #
    #             return relatorio
    #     except Exception as e:
    #         print(f"Erro ao gerar relatório: {e}")
    #         return []
    #     finally:
    #         if cursor:
    #             cursor.close()
    #         if conn:
    #             conn.close()
    #
    def obterDistribuicoesPorPeriodo(self, data_inicio, data_fim):
        """
        Obtém as distribuições realizadas em um determinado período.
        :param data_inicio: Data inicial do período (string no formato 'YYYY-MM-DD').
        :param data_fim: Data final do período (string no formato 'YYYY-MM-DD').
        :return: Lista de distribuições realizadas no período especificado.
        """
        if not data_inicio or not data_fim:
            raise ValueError("As datas de início e fim devem ser fornecidas.")

        query_sql = """
            SELECT d.distribuicao_id, d.beneficiario_id, b.nome AS beneficiario_nome, 
                   d.produto_id, p.nome AS produto_nome, d.data_distribuicao, d.quantidade
            FROM distribuicao d
            INNER JOIN beneficiario b ON d.beneficiario_id = b.beneficiario_id
            INNER JOIN produto p ON d.produto_id = p.produto_id
            WHERE d.data_distribuicao BETWEEN %s AND %s
            ORDER BY d.data_distribuicao ASC
        """

        try:
            # Conectar ao banco de dados
            conn = ConnectionFactory.get_connection()
            with conn.cursor(dictionary=True) as cursor:
                # Executar a consulta
                cursor.execute(query_sql, (data_inicio, data_fim))
                distribuicoes = cursor.fetchall()
                return distribuicoes

        except Exception as e:
            print(f"Erro ao obter distribuições por período: {e}")
            raise

        finally:
            if conn:
                conn.close()


    def obterDistribuicoesPorMesEAno(self, mes, ano):
        """
        Obtém as distribuições realizadas em um determinado mês e ano.
        :param mes: Mês do período (inteiro de 1 a 12).
        :param ano: Ano do período (inteiro com 4 dígitos).
        :return: Lista de distribuições realizadas no mês e ano especificados.
        """
        if not mes or not ano:
            raise ValueError("O mês e o ano devem ser fornecidos.")

        if not (1 <= mes <= 12):
            raise ValueError("O mês deve estar entre 1 e 12.")

        query_sql = """
            SELECT d.distribuicao_id, d.beneficiario_id, b.nome AS beneficiario_nome, 
                   d.produto_id, p.nome AS produto_nome, d.data_distribuicao, d.quantidade
            FROM distribuicao d
            INNER JOIN beneficiario b ON d.beneficiario_id = b.beneficiario_id
            INNER JOIN produto p ON d.produto_id = p.produto_id
            WHERE YEAR(d.data_distribuicao) = %s AND MONTH(d.data_distribuicao) = %s
            ORDER BY d.data_distribuicao ASC
        """

        try:
            # Conectar ao banco de dados
            conn = ConnectionFactory.get_connection()
            with conn.cursor(dictionary=True) as cursor:
                # Executar a consulta
                cursor.execute(query_sql, (ano, mes))
                distribuicoes = cursor.fetchall()
                return distribuicoes

        except Exception as e:
            print(f"Erro ao obter distribuições por mês e ano: {e}")
            raise

        finally:
            if conn:
                conn.close()
