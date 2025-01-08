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
    #
    # def consultar_por_id(self, id_distribuicao):
    #     """
    #     Consulta uma distribuição por seu ID e retorna seus detalhes.
    #     :param id_distribuicao: ID da distribuição a ser consultada.
    #     :return: Objeto Distribuicao com os dados correspondentes ou None se não encontrar.
    #     """
    #     sql_distribuicao = """
    #     SELECT d.distribuicao_id, d.beneficiario_id, d.data_distribuicao, b.nome, b.email
    #     FROM distribuicao d
    #     JOIN beneficiario b ON d.beneficiario_id = b.beneficiario_id
    #     WHERE d.distribuicao_id = %s
    #     """
    #     sql_produtos = """
    #     SELECT p.produto_id, p.nome, dp.quantidade
    #     FROM distribuicao_produtos dp
    #     JOIN produto p ON dp.produto_id = p.produto_id
    #     WHERE dp.distribuicao_id = %s
    #     """
    #
    #     try:
    #         conn = ConnectionFactory.get_connection()
    #         if conn:
    #             cursor = conn.cursor()
    #
    #             # Consultar a distribuição
    #             cursor.execute(sql_distribuicao, (id_distribuicao,))
    #             distribuicao_data = cursor.fetchone()
    #
    #             if distribuicao_data:
    #                 # Criar objeto Beneficiario
    #                 beneficiario = Beneficiario(idBeneficiario=distribuicao_data[1], nome=distribuicao_data[3],
    #                                             email=distribuicao_data[4])
    #
    #                 # Criar objeto Distribuicao
    #                 distribuicao = Distribuicao(idDistribuicao=distribuicao_data[0], beneficiario=beneficiario,
    #                                             dataDistribuicao=distribuicao_data[2])
    #
    #                 # Consultar produtos da distribuição
    #                 cursor.execute(sql_produtos, (id_distribuicao,))
    #                 produtos = []
    #                 for row in cursor.fetchall():
    #                     produto = Produto(idProduto=row[0], nome=row[1], quantidade=row[2])
    #                     produtos.append(produto)
    #
    #                 distribuicao.produtos = produtos
    #                 return distribuicao
    #             else:
    #                 print(f"Distribuição com ID {id_distribuicao} não encontrada.")
    #                 return None
    #     except Exception as e:
    #         print(f"Erro ao consultar distribuição: {e}")
    #         return None
    #     finally:
    #         if cursor:
    #             cursor.close()
    #         if conn:
    #             conn.close()
    #
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
    # def relatorio_periodo(self, data_inicio, data_fim):
    #     """
    #     Gera um relatório de todas as distribuições feitas em um período específico.
    #     :param data_inicio: Data de início do período.
    #     :param data_fim: Data de fim do período.
    #     :return: Lista de distribuições feitas no período.
    #     """
    #     sql = """
    #     SELECT d.distribuicao_id, d.data_distribuicao, b.nome, b.email, p.produto_id, p.nome, dp.quantidade
    #     FROM distribuicao d
    #     JOIN beneficiario b ON d.beneficiario_id = b.beneficiario_id
    #     JOIN distribuicao_produtos dp ON d.distribuicao_id = dp.distribuicao_id
    #     JOIN produto p ON dp.produto_id = p.produto_id
    #     WHERE d.data_distribuicao BETWEEN %s AND %s
    #     ORDER BY d.data_distribuicao
    #     """
    #
    #     try:
    #         conn = ConnectionFactory.get_connection()
    #         if conn:
    #             cursor = conn.cursor()
    #
    #             # Consultar distribuições no período
    #             cursor.execute(sql, (data_inicio, data_fim))
    #             distribuições = {}
    #
    #             for row in cursor.fetchall():
    #                 distribuicao_id = row[0]
    #                 data_distribuicao = row[1]
    #                 beneficiario_nome = row[2]
    #                 beneficiario_email = row[3]
    #                 produto_id = row[4]
    #                 produto_nome = row[5]
    #                 quantidade = row[6]
    #
    #                 if distribuicao_id not in distribuições:
    #                     distribuições[distribuicao_id] = {
    #                         'data_distribuicao': data_distribuicao,
    #                         'beneficiario': Beneficiario(nome=beneficiario_nome, email=beneficiario_email),
    #                         'produtos': []
    #                     }
    #
    #                 # Adiciona o produto à lista de produtos da distribuição
    #                 produto = Produto(idProduto=produto_id, nome=produto_nome, quantidade=quantidade)
    #                 distribuições[distribuicao_id]['produtos'].append(produto)
    #
    #             # Organizar as distribuições em objetos Distribuicao
    #             relatorio = []
    #             for distribuicao_id, dados in distribuições.items():
    #                 # Criando o objeto Distribuicao
    #                 distribuicao = Distribuicao(idDistribuicao=distribuicao_id,
    #                                             dataDistribuicao=dados['data_distribuicao'])
    #                 distribuicao.beneficiario = dados['beneficiario']
    #                 distribuicao.produtos = dados['produtos']
    #                 relatorio.append(distribuicao)
    #
    #             return relatorio
    #     except Exception as e:
    #         print(f"Erro ao gerar relatório do período: {e}")
    #         return []
    #     finally:
    #         if cursor:
    #             cursor.close()
    #         if conn:
    #             conn.close()