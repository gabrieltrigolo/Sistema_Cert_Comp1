from datetime import date
from src.dao.ProdutoDAO import ProdutoDAO
from src.dao.UsuarioDAO import UsuarioDAO
from src.model.Beneficiario import Beneficiario
from src.model.Produto import Produto
from src.model.Distribuicao import Distribuicao
from src.dao.DistribuicaoDAO import DistribuicaoDAO
from src.model.Usuario import Usuario

if __name__ == "__main__":
    dao = UsuarioDAO()

    # # Teste do metodo inserir
    # user_novo1 = Usuario(None, "Mateus", "mateus@email.com", '123456789')
    # dao.inserir(user_novo1)

    # # Teste do metodo buscarPorId
    # user_id = 2  # Substitua pelo ID gerado ao inserir
    # usuario = dao.buscarPorId(user_id)
    # if usuario:
    #     print("Usuario encontrado:", usuario)
    #
    # # Teste do metodo atualizar, usar junto com o teste buscar_por_id
    # if usuario:
    #     # Alterando vários campos
    #     usuario.nome = "Novo Nome"
    #     usuario.senha = "Nova senha"
    #     usuario.email = "Novo email"
    #
    #     dao.atualizar(3, usuario)

    # # Teste do metodo deletar, usar junto com o teste buscar_por_id
    # if usuario:
    #     dao.deletar(4)

    # # Listar todos os produtos ao final
    # print("Usuarios:")
    # for usuario in dao.listarTodosUsuarios():
    #     print(usuario)