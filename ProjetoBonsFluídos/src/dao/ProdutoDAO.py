from ..model.Produto import Produto
from ..dao.ConnectionFactory import ConnectionFactory
from typing import List, Optional

class ProdutoDAO:

    def inserir(self, produto: Produto) -> None:
        """
        Insere um produto na tabela 'produto'.
        :param produto: Objeto Produto contendo os dados a serem inseridos.
        """
        sql = """
        INSERT INTO produto (nome, descricao, quantidade, data_doacao)
        VALUES (%s, %s, %s, %s)
        """
        try:
            conn = ConnectionFactory.get_connection()
            if conn:
                cursor = conn.cursor()
                cursor.execute(sql, (
                    produto.nome,
                    produto.descricao,
                    produto.quantidade,
                    produto.dataRecebimento
                ))
                conn.commit()
                if cursor.rowcount > 0:
                    print("Produto cadastrado com sucesso!")
                else:
                    print("Produto não cadastrado.")
                cursor.close()
                conn.close()
        except Exception as e:
            print(f"Erro ao inserir produto: {e}")

    def atualizar(self, produto: Produto) -> None:
        """
        Atualiza os dados de um produto existente na tabela 'produto'.
        :param produto: Objeto Produto contendo os dados atualizados.
        """
        sql = """
        UPDATE produto
        SET nome = %s, descricao = %s, quantidade = %s, data_doacao = %s
        WHERE produto_id = %s
        """
        try:
            conn = ConnectionFactory.get_connection()
            if conn:
                cursor = conn.cursor()
                cursor.execute(sql, (
                    produto.nome,
                    produto.descricao,
                    produto.quantidade,
                    produto.dataRecebimento,
                    produto.idProduto
                ))
                conn.commit()
                if cursor.rowcount > 0:
                    print("Produto atualizado com sucesso!")
                else:
                    print("Produto não encontrado ou não atualizado.")
                cursor.close()
                conn.close()
        except Exception as e:
            print(f"Erro ao atualizar produto: {e}")

    def buscarPorId(self, produtoId: int) -> Optional[Produto]:
        """
        Busca um produto pelo ID na tabela 'produto'.
        :param produto_id: ID do produto a ser buscado.
        :return: Objeto Produto se encontrado, ou None se não encontrado.
        """
        sql = """
        SELECT produto_id, nome, descricao, quantidade, data_doacao
        FROM produto
        WHERE produto_id = %s
        """
        try:
            conn = ConnectionFactory.get_connection()
            if conn:
                cursor = conn.cursor()
                cursor.execute(sql, (produtoId,))
                row = cursor.fetchone()
                cursor.close()
                conn.close()
                if row:
                    return Produto(
                        idProduto=row[0],
                        nome=row[1],
                        descricao=row[2],
                        quantidade=row[3],
                        dataRecebimento=row[4]
                    )
                else:
                    print("Produto não encontrado.")
                    return None
        except Exception as e:
            print(f"Erro ao buscar produto por ID: {e}")
            return None

    def listarTodosProdutos(self) -> List[Produto]:
        """
        Retorna todos os produtos da tabela 'produto' com quantidade > 0.
        :return: Lista de objetos Produto.
        """
        sql = """
        SELECT produto_id, nome, descricao, quantidade, data_doacao
        FROM produto
        WHERE quantidade > 0  -- Filtra produtos com quantidade maior que zero
        """
        try:
            conn = ConnectionFactory.get_connection()
            if conn:
                cursor = conn.cursor()
                cursor.execute(sql)
                results = cursor.fetchall()
                cursor.close()
                conn.close()
                produtos = []
                for result in results:
                    produtos.append((result[1], result[2], result[3], result[4]))
                return produtos
        except Exception as e:
            print(f"Erro ao listar produtos: {e}")
            return []

    def deletar(self, produtoId: int) -> None:
        """
        Deleta um produto pelo ID da tabela 'produto'.
        :param produto_id: ID do produto a ser deletado.
        """
        sql = """
        DELETE FROM produto
        WHERE produto_id = %s
        """
        try:
            conn = ConnectionFactory.get_connection()
            if conn:
                cursor = conn.cursor()
                cursor.execute(sql, (produtoId,))
                conn.commit()
                if cursor.rowcount > 0:
                    print("Produto deletado com sucesso!")
                else:
                    print("Produto não encontrado ou não deletado.")
                cursor.close()
                conn.close()
        except Exception as e:
            print(f"Erro ao deletar produto: {e}")