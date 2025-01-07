import mysql.connector
from mysql.connector import Error
from model.Beneficiario import Beneficiario
from model.Produto import Produto
from model.Distribuicao import Distribuicao

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

    def consultar_por_id(self, id_distribuicao):
        """
        Consulta uma distribuição por seu ID e retorna seus detalhes.
        :param id_distribuicao: ID da distribuição a ser consultada.
        :return: Objeto Distribuicao com os dados correspondentes ou None se não encontrar.
        """
        sql_distribuicao = """
        SELECT d.distribuicao_id, d.beneficiario_id, d.data_distribuicao, b.nome, b.email
        FROM distribuicao d
        JOIN beneficiario b ON d.beneficiario_id = b.beneficiario_id
        WHERE d.distribuicao_id = %s
        """
        sql_produtos = """
        SELECT p.produto_id, p.nome, dp.quantidade
        FROM distribuicao_produtos dp
        JOIN produto p ON dp.produto_id = p.produto_id
        WHERE dp.distribuicao_id = %s
        """
        
        try:
            conn = self.get_connection()
            if conn:
                cursor = conn.cursor()

                # Consultar a distribuição
                cursor.execute(sql_distribuicao, (id_distribuicao,))
                distribuicao_data = cursor.fetchone()

                if distribuicao_data:
                    # Criar objeto Beneficiario
                    beneficiario = Beneficiario(idBeneficiario=distribuicao_data[1], nome=distribuicao_data[3], email=distribuicao_data[4])

                    # Criar objeto Distribuicao
                    distribuicao = Distribuicao(idDistribuicao=distribuicao_data[0], beneficiario=beneficiario, dataDistribuicao=distribuicao_data[2])

                    # Consultar produtos da distribuição
                    cursor.execute(sql_produtos, (id_distribuicao,))
                    produtos = []
                    for row in cursor.fetchall():
                        produto = Produto(idProduto=row[0], nome=row[1], quantidade=row[2])
                        produtos.append(produto)

                    distribuicao.produtos = produtos
                    return distribuicao
                else:
                    print(f"Distribuição com ID {id_distribuicao} não encontrada.")
                    return None
        except Error as e:
            print(f"Erro ao consultar distribuição: {e}")
            return None
        finally:
            if cursor:
                cursor.close()
            if conn:
                conn.close()

    def relatorio_por_beneficiario(self, id_beneficiario):
        """
        Gera um relatório de todas as distribuições feitas a um beneficiário.
        :param id_beneficiario: ID do beneficiário.
        :return: Lista de distribuições feitas a esse beneficiário.
        """
        sql = """
        SELECT d.distribuicao_id, d.data_distribuicao, p.produto_id, p.nome, dp.quantidade
        FROM distribuicao d
        JOIN distribuicao_produtos dp ON d.distribuicao_id = dp.distribuicao_id
        JOIN produto p ON dp.produto_id = p.produto_id
        WHERE d.beneficiario_id = %s
        ORDER BY d.data_distribuicao DESC
        """

        try:
            conn = self.get_connection()
            if conn:
                cursor = conn.cursor()

                # Consultar distribuições do beneficiário
                cursor.execute(sql, (id_beneficiario,))
                distribuições = {}
                
                for row in cursor.fetchall():
                    distribuicao_id = row[0]
                    data_distribuicao = row[1]
                    produto_id = row[2]
                    nome_produto = row[3]
                    quantidade = row[4]

                    if distribuicao_id not in distribuições:
                        distribuições[distribuicao_id] = {
                            'data_distribuicao': data_distribuicao,
                            'produtos': []
                        }
                    
                    # Adiciona o produto à lista de produtos da distribuição
                    produto = Produto(idProduto=produto_id, nome=nome_produto, quantidade=quantidade)
                    distribuições[distribuicao_id]['produtos'].append(produto)

                # Organizar as distribuições em objetos Distribuicao
                relatorio = []
                for distribuicao_id, dados in distribuições.items():
                    # Criando o objeto Distribuicao
                    distribuicao = Distribuicao(idDistribuicao=distribuicao_id, dataDistribuicao=dados['data_distribuicao'])
                    distribuicao.produtos = dados['produtos']
                    relatorio.append(distribuicao)

                return relatorio
        except Error as e:
            print(f"Erro ao gerar relatório: {e}")
            return []
        finally:
            if cursor:
                cursor.close()
            if conn:
                conn.close()

    def relatorio_periodo(self, data_inicio, data_fim):
        """
        Gera um relatório de todas as distribuições feitas em um período específico.
        :param data_inicio: Data de início do período.
        :param data_fim: Data de fim do período.
        :return: Lista de distribuições feitas no período.
        """
        sql = """
        SELECT d.distribuicao_id, d.data_distribuicao, b.nome, b.email, p.produto_id, p.nome, dp.quantidade
        FROM distribuicao d
        JOIN beneficiario b ON d.beneficiario_id = b.beneficiario_id
        JOIN distribuicao_produtos dp ON d.distribuicao_id = dp.distribuicao_id
        JOIN produto p ON dp.produto_id = p.produto_id
        WHERE d.data_distribuicao BETWEEN %s AND %s
        ORDER BY d.data_distribuicao
        """

        try:
            conn = self.get_connection()
            if conn:
                cursor = conn.cursor()

                # Consultar distribuições no período
                cursor.execute(sql, (data_inicio, data_fim))
                distribuições = {}

                for row in cursor.fetchall():
                    distribuicao_id = row[0]
                    data_distribuicao = row[1]
                    beneficiario_nome = row[2]
                    beneficiario_email = row[3]
                    produto_id = row[4]
                    produto_nome = row[5]
                    quantidade = row[6]

                    if distribuicao_id not in distribuições:
                        distribuições[distribuicao_id] = {
                            'data_distribuicao': data_distribuicao,
                            'beneficiario': Beneficiario(nome=beneficiario_nome, email=beneficiario_email),
                            'produtos': []
                        }

                    # Adiciona o produto à lista de produtos da distribuição
                    produto = Produto(idProduto=produto_id, nome=produto_nome, quantidade=quantidade)
                    distribuições[distribuicao_id]['produtos'].append(produto)

                # Organizar as distribuições em objetos Distribuicao
                relatorio = []
                for distribuicao_id, dados in distribuições.items():
                    # Criando o objeto Distribuicao
                    distribuicao = Distribuicao(idDistribuicao=distribuicao_id, dataDistribuicao=dados['data_distribuicao'])
                    distribuicao.beneficiario = dados['beneficiario']
                    distribuicao.produtos = dados['produtos']
                    relatorio.append(distribuicao)

                return relatorio
        except Error as e:
            print(f"Erro ao gerar relatório do período: {e}")
            return []
        finally:
            if cursor:
                cursor.close()
            if conn:
                conn.close()
