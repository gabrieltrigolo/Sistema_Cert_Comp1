from datetime import date
from src.dao.ProdutoDAO import ProdutoDAO
from src.model.Beneficiario import Beneficiario
from src.model.Produto import Produto
from src.model.Distribuicao import Distribuicao
from src.dao.DistribuicaoDAO import DistribuicaoDAO

if __name__ == "__main__":
    dao = ProdutoDAO()
    #
    # Teste do metodo inserir
    produto_novo1 = Produto(None, "Produto Teste1", "Descrição Teste45", 20, date(2025, 12, 31))
    produto_novo2 = Produto(None, "Produto Teste2", "Descrição Teste6464", 100, date.today())
    produto_novo3 = Produto(None, "Produto Teste3", "Descrição Teste4545", 50, date(2020, 12, 31))
    dao.inserir(produto_novo1)
    dao.inserir(produto_novo2)
    dao.inserir(produto_novo3)
    #
    # # Listar todos os produtos após a inserção
    # print("Produtos cadastrados:")
    # for produto in dao.listarTodosProdutos():
    #     print(vars(produto))

    # # Teste do metodo buscar_por_id
    # produto_id = 5  # Substitua pelo ID gerado ao inserir
    # produto = dao.buscarPorId(produto_id)
    # if produto:
    #     print("Produto encontrado:", vars(produto))
    #
    # # Teste do metodo atualizar, usar junto com o teste buscar_por_id
    # if produto:
    #     # Alterando vários campos
    #     produto.nome = "Produto Atualizado2"
    #     produto.descricao = "Descrição Atualizada"
    #     produto.quantidade = 200
    #     produto.dataRecebimento = date(2025, 1, 9)  # Nova data de recebimento
    #
    #     dao.atualizar(produto)
    #
    #     # Verificar a atualização
    #     produto_atualizado = dao.buscarPorId(produto_id)
    #     if produto_atualizado:
    #         print("Produto atualizado:", vars(produto_atualizado))
    #     else:
    #         print("Produto não encontrado após a atualização.")
    # else:
    #     print("Produto não encontrado para atualização.")
    #
    # # Teste do metodo deletar, usar junto com o teste buscar_por_id
    # if produto:
    #     dao.deletar(produto.idProduto)
    #
    # # Listar todos os produtos ao final
    # print("Produtos restantes:")
    # for produto in dao.listarTodosProdutos():
    #     print(vars(produto))