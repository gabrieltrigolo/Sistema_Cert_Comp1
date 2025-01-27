from datetime import date

from src.dao.BeneficiarioDAO import BeneficiarioDAO
from src.dao.ProdutoDAO import ProdutoDAO
from src.model.Beneficiario import Beneficiario
from src.model.Produto import Produto
from src.model.Distribuicao import Distribuicao
from src.dao.DistribuicaoDAO import DistribuicaoDAO

if __name__ == "__main__":
    dao = BeneficiarioDAO()
    #
    # # Teste do metodo inserir
    # beneficiario_novo1 = Beneficiario(None, "mateus", "mateus@email", "123-55")
    # beneficiario_novo2 = Beneficiario(None, "asdasd", "asdasdda@email", "1234-55")
    # beneficiario_novo3 = Beneficiario(None, "asdasdad", "asdasdas@email", "12377-55")
    # dao.inserir(beneficiario_novo1)
    # dao.inserir(beneficiario_novo2)
    # dao.inserir(beneficiario_novo3)
    #
    # # Listar todos os beneficiários após a inserção
    # print("Beneficiários cadastrados:")
    # for beneficiario in dao.listarTodosBeneficiarios():
    #     print(vars(beneficiario))
    #
    # # Teste do metodo buscarPorId
    # cnpj_cpf = "123-55"  # Substitua pelo CNPJ/CPF gerado ao inserir
    # beneficiario = dao.buscarPorId(cnpj_cpf)
    # if beneficiario:
    #     print("Beneficiário encontrado:", vars(beneficiario))
    #
    # # Teste do metodo atualizar, usar junto com o teste buscarPorId
    # if beneficiario:
    #     # Alterando vários campos
    #     beneficiario.nome = "Beneficiário Atualizado"
    #     beneficiario.email = "atualizado@example.com"
    #
    #     dao.atualizar(beneficiario)
    #
    #     # Verificar a atualização
    #     beneficiario_atualizado = dao.buscarPorId(cnpj_cpf)
    #     if beneficiario_atualizado:
    #         print("Beneficiário atualizado:", vars(beneficiario_atualizado))
    #     else:
    #         print("Beneficiário não encontrado após a atualização.")
    # else:
    #     print("Beneficiário não encontrado para atualização.")
    #
    # # Teste do metodo deletar, usar junto com o teste buscarPorId
    # if beneficiario:
    #     dao.deletarBeneficiario(cnpj_cpf)
    #
    # # Listar todos os beneficiários ao final
    # print("Beneficiários restantes:")
    # for beneficiario in dao.listarTodosBeneficiarios():
    #     print(vars(beneficiario))