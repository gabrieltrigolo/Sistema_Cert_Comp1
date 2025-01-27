from datetime import date

from src.dao.BeneficiarioDAO import BeneficiarioDAO
from src.dao.ProdutoDAO import ProdutoDAO
from src.dao.DistribuicaoDAO import DistribuicaoDAO
from src.model.Beneficiario import Beneficiario
from src.model.Produto import Produto
from src.model.Distribuicao import Distribuicao

if __name__ == "__main__":
    beneficiario_dao = BeneficiarioDAO()
    produto_dao = ProdutoDAO()
    distribuicao_dao = DistribuicaoDAO()

    # # Inserir beneficiários
    # beneficiario1 = Beneficiario(None, "Mateus", "mateus@email.com", "123.456.789-00")
    # beneficiario2 = Beneficiario(None, "João", "joao@email.com", "987.654.321-00")
    # beneficiario_dao.inserir(beneficiario1)
    # beneficiario_dao.inserir(beneficiario2)
    #
    # # Inserir produtos
    # produto1 = Produto(None, "Arroz", "Arroz branco", 100, date.today())
    # produto2 = Produto(None, "Feijão", "Feijão preto", 50, date.today())
    # produto_dao.inserir(produto1)
    # produto_dao.inserir(produto2)

    distribuicao_dao.inserirEspecial('Água', 1,22,date.today())
    # beneficiario1 = beneficiario_dao.buscarPorId('123.456.789-00')
    # produto1 = produto_dao.buscarPorId(2)
    #
    # # Teste do metodo inserir
    # distribuicao1 = Distribuicao(idDistribuicao=None,beneficiario=beneficiario1,produto=produto1, dataDistribuicao=date.today(), quantidade=5)
    # distribuicao_dao.inserir(distribuicao1)
    #
    # # Listar todas as distribuições após a inserção
    # print("Distribuições cadastradas:")
    # for distribuicao in distribuicao_dao.listarDistribuicoes():
    #     print(distribuicao)

    # # Teste do metodo buscarPorId
    # distribuicao_id = 1  # Substitua pelo ID gerado ao inserir
    # distribuicao = distribuicao_dao.buscarPorId(distribuicao_id)
    # if distribuicao:
    #     print("Distribuição encontrada:", distribuicao)

    # beneficiario_id=1
    # distribuicoes = distribuicao_dao.buscarDistribuicoesPorBeneficiario(beneficiario_id)
    # if distribuicoes:
    #     for dist in distribuicoes:
    #         print(f"ID: {dist[0]}, Beneficiário: {dist[1]}, Produto: {dist[2]}, Quantidade: {dist[3]}, Data: {dist[4]}")
    # else:
    #     print(f"Nenhuma distribuição encontrada para o beneficiário ID {beneficiario_id}.")

    # # Teste do metodo obterDistribuicoesPorPeriodo
    # distribuicoes = distribuicao_dao.obterDistribuicoesPorPeriodo("2025-01-01", "2025-01-10")
    # for dist in distribuicoes:
    #     print(f"Distribuição ID: {dist['distribuicao_id']}, Produto: {dist['produto_nome']}, "
    #           f"Beneficiário: {dist['beneficiario_nome']}, Quantidade: {dist['quantidade']}, "
    #           f"Data: {dist['data_distribuicao']}")

    # # Teste do metodo obterDistribuicoesPorMesEAno
    # distribuicoes = distribuicao_dao.obterDistribuicoesPorMesEAno(1, 2025)
    # for dist in distribuicoes:
    #     print(f"Distribuição ID: {dist['distribuicao_id']}, Produto: {dist['produto_nome']}, "
    #           f"Beneficiário: {dist['beneficiario_nome']}, Quantidade: {dist['quantidade']}, "
    #           f"Data: {dist['data_distribuicao']}")

    # # Teste do metodo atualizar, usar junto com o teste buscarPorId
    # if distribuicao:
    #     # Alterando vários campos
    #     distribuicao['quantidade'] = 15
    #     distribuicao['data_distribuicao'] = date.today()
    #
    #     distribuicao_atualizada = Distribuicao(
    #         distribuicao['distribuicao_id'],
    #         Beneficiario(beneficiario1.idBeneficiario, beneficiario1.nome, beneficiario1.email, beneficiario1.cnpj_cpf),
    #         Produto(produto1.idProduto, produto1.nome, produto1.descricao, produto1.quantidade),
    #         distribuicao['data_distribuicao'],
    #         distribuicao['quantidade']
    #     )
    #
    #     distribuicao_dao.atualizar(distribuicao_atualizada)
    #
    #     # Verificar a atualização
    #     distribuicao_atualizada = distribuicao_dao.buscarPorId(distribuicao_id)
    #     if distribuicao_atualizada:
    #         print("Distribuição atualizada:", distribuicao_atualizada)
    #     else:
    #         print("Distribuição não encontrada após a atualização.")
    # else:
    #     print("Distribuição não encontrada para atualização.")
    #
    # # Teste do metodo deletar, usar junto com o teste buscarPorId
    # if distribuicao:
    #     distribuicao_dao.deletarDistribuicao(distribuicao_id)
    #
    # # Listar todas as distribuições ao final
    # print("Distribuições restantes:")
    # for distribuicao in distribuicao_dao.listarTodasDistribuicoes():
    #     print(distribuicao)
