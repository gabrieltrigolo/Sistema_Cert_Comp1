from datetime import date

from src.dao.BeneficiarioDAO import BeneficiarioDAO
from src.dao.ProdutoDAO import ProdutoDAO
from src.dao.DistribuicaoDAO import DistribuicaoDAO
from src.model.Beneficiario import Beneficiario
from src.model.Produto import Produto
from src.model.Distribuicao import Distribuicao
from src.model.Doacao import Doacao
from src.dao.DoacaoDAO import DoacaoDAO


if __name__ == "__main__":
    produto_dao = ProdutoDAO()
    doacao_dao = DoacaoDAO()


    # Inserir produtos
    produto1 = Produto(None, "Arroz", "Arroz branco", 100, date.today())
    # produto2 = Produto(None, "Feijão", "Feijão preto", 50, date.today())
    # produto_dao.inserir(produto1)
    # produto_dao.inserir(produto2)
    #
    # produto1 = produto_dao.buscarPorId(2)

    # Teste do metodo inserir
    doacao1 = Doacao(idDoacao=None,produto=produto1, dataDoacao=date.today(), quantidade=produto1.quantidade, responsavel='Mateus')
    doacao_dao.inserir(doacao1)


    # # Teste do metodo buscarPorId
    # doacao_id = 1  # Substitua pelo ID gerado ao inserir
    # doacao = doacao_dao.buscarPorId(doacao_id)
    # if doacao:
    #     print("doacao encontrada:", doacao)
    #
    # #Metodo atualizar
    # produto_atualizado = Produto()
    # produto_atualizado.id = 11  # ID do produto que você quer atualizar
    # produto_atualizado.nome = "Arroz Atualizado"
    # produto_atualizado.descricao = "Pacote de 5kg - Novo lote"
    # produto_atualizado.quantidade = 50
    # produto_atualizado.dataRecebimento = date.today()
    #
    #     # Criar um objeto Doacao com os dados atualizados
    # doacao_atualizada = Doacao()
    # doacao_atualizada.produto = produto_atualizado
    # doacao_atualizada.dataDoacao = date.today()
    # doacao_atualizada.quantidade = 50
    # doacao_atualizada.responsavel = "João Silva"
    #
    # doacao_dao.atualizar(doacao_atualizada)