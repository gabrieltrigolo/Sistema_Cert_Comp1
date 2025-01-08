from ..model.Produto import Produto
from ..dao.ConnectionFactory import ConnectionFactory

class ProdutoDAO:
    def inserir(self, produto):
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

    def atualizar(self, produto):
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

    def buscarPorId(self, produto_id):
        sql = """
        SELECT produto_id, nome, descricao, quantidade, data_doacao
        FROM produto
        WHERE produto_id = %s
        """
        try:
            conn = ConnectionFactory.get_connection()
            if conn:
                cursor = conn.cursor()
                cursor.execute(sql, (produto_id,))
                row = cursor.fetchone()
                cursor.close()
                conn.close()
                if row:
                    return Produto(*row)  # Presume que a classe Produto tem o mesmo construtor
                else:
                    print("Produto não encontrado.")
                    return None
        except Exception as e:
            print(f"Erro ao buscar produto por ID: {e}")
            return None

    def listarTodosProdutos(self):
        sql = """
        SELECT produto_id, nome, descricao, quantidade, data_doacao
        FROM produto
        """
        try:
            conn = ConnectionFactory.get_connection()
            if conn:
                cursor = conn.cursor()
                cursor.execute(sql)
                rows = cursor.fetchall()
                cursor.close()
                conn.close()
                produtos = [Produto(*row) for row in rows]
                return produtos
        except Exception as e:
            print(f"Erro ao listar produtos: {e}")
            return []

    def deletar(self, produto_id):
        sql = """
        DELETE FROM produto
        WHERE produto_id = %s
        """
        try:
            conn = ConnectionFactory.get_connection()
            if conn:
                cursor = conn.cursor()
                cursor.execute(sql, (produto_id,))
                conn.commit()
                if cursor.rowcount > 0:
                    print("Produto deletado com sucesso!")
                else:
                    print("Produto não encontrado ou não deletado.")
                cursor.close()
                conn.close()
        except Exception as e:
            print(f"Erro ao deletar produto: {e}")
