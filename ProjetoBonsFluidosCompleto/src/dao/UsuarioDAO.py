from ..dao.ConnectionFactory import ConnectionFactory
from ..model.Usuario import Usuario

class UsuarioDAO:

    def inserir(self, usuario):
        sql_check_email = """
        SELECT 1 FROM usuario WHERE email = %s
        """
        sql_check_admin = """
        SELECT 1 FROM usuario WHERE cargo = 'ADMIN'
        """
        sql_insert = """
        INSERT INTO usuario (nome, senha, email, cargo)
        VALUES (%s, %s, %s, %s)
        """
        try:
            conn = ConnectionFactory.get_connection()
            if conn:
                cursor = conn.cursor()

                # Verifica se o email já existe
                cursor.execute(sql_check_email, (usuario.email,))
                result_email = cursor.fetchone()

                if result_email:
                    raise Exception("Usuário com este email já está cadastrado.")

                # Verifica se há algum usuário com cargo "Administrador"
                cursor.execute(sql_check_admin)
                result_admin = cursor.fetchone()

                # Define o cargo como "Administrador" caso não haja nenhum usuário com esse cargo ou a tabela esteja vazia
                if not result_admin and usuario.cargo is None:
                    usuario.cargo = "Administrador"

                # Insere o novo usuário
                cursor.execute(sql_insert, (
                    usuario.nome,
                    usuario.senha,
                    usuario.email,
                    usuario.cargo
                ))
                conn.commit()
                if cursor.rowcount > 0:
                    print(f"Usuário cadastrado com sucesso! Cargo: {usuario.cargo}")
                else:
                    raise Exception("Usuário não cadastrado por algum motivo desconhecido.")

                cursor.close()
                conn.close()
        except Exception as e:
            raise e  # Relevanta a exceção para ser tratada no código principal

    def buscarPorId(self, usuario_id):
        sql = """
        SELECT usuario_id, nome, senha, email, cargo
        FROM usuario
        WHERE usuario_id = %s
        """
        try:
            conn = ConnectionFactory.get_connection()
            if conn:
                cursor = conn.cursor()
                cursor.execute(sql, (usuario_id,))
                resultado = cursor.fetchone()
                cursor.close()
                conn.close()

                if resultado:
                    # Retorna um objeto Usuario
                    return Usuario(
                        idUsuario=resultado[0],
                        nome=resultado[1],
                        senha=resultado[2],
                        email=resultado[3],
                        cargo=resultado[4]
                    )
                else:
                    print(f"Usuário com ID {usuario_id} não encontrado.")
                    return None
        except Exception as e:
            print(f"Erro ao buscar usuário por ID: {e}")
            return None

    def atualizar(self, usuario_id, usuario):
        sql_check_email = """
        SELECT 1 FROM usuario WHERE email = %s AND usuario_id != %s
        """
        sql_update = """
        UPDATE usuario
        SET nome = %s, senha = %s, email = %s, cargo = %s
        WHERE usuario_id = %s
        """
        conn = None
        cursor = None
        try:
            conn = ConnectionFactory.get_connection()
            if not conn:
                raise Exception("Não foi possível estabelecer conexão com o banco de dados")

            cursor = conn.cursor()
            # Verifica se o novo email já está sendo usado
            cursor.execute(sql_check_email, (usuario.email, usuario_id))
            if cursor.fetchone():
                raise Exception("O email informado já está sendo utilizado por outro usuário.")

            # Atualiza o usuário
            cursor.execute(sql_update, (
                usuario.nome,
                usuario.senha,
                usuario.email,
                usuario.cargo,
                usuario_id
            ))
            conn.commit()

            if cursor.rowcount == 0:
                raise Exception(f"Usuário com ID {usuario_id} não encontrado.")

            return True

        except Exception as e:
            if conn:
                conn.rollback()
            raise e
        finally:
            if cursor:
                cursor.close()
            if conn:
                conn.close()

    def listarTodosUsuarios(self):
        sql = "SELECT usuario_id, nome, email, cargo FROM usuario"
        try:
            conn = ConnectionFactory.get_connection()
            if conn:
                with conn.cursor() as cursor:
                    cursor.execute(sql)
                    resultados = cursor.fetchall()

                    usuarios = []
                    for result in resultados:
                        usuarios.append((result[0], result[1], result[2], result[3]))  # Retornando tuplas
                    return usuarios
        except Exception as e:
            print(f"Erro ao listar usuários: {e}")
            return []
        finally:
            if conn:
                conn.close()

    def deletar(self, usuario_id):
        sql = "DELETE FROM usuario WHERE usuario_id = %s"
        try:
            conn = ConnectionFactory.get_connection()
            if conn:
                with conn.cursor() as cursor:
                    cursor.execute(sql, (usuario_id,))
                    conn.commit()

                    if cursor.rowcount > 0:
                        print("Usuário deletado com sucesso!")
                    else:
                        print("Nenhum usuário foi deletado.")
        except Exception as e:
            print(f"Erro ao deletar usuário: {e}")
        finally:
            if conn:
                conn.close()

    def verificarLogin(self, email, senha):
        sql = """
        SELECT usuario_id, nome, cargo FROM usuario 
        WHERE email = %s AND senha = %s
        """
        try:
            conn = ConnectionFactory.get_connection()
            with conn.cursor() as cursor:
                cursor.execute(sql, (email, senha))
                result = cursor.fetchone()

            if result:
                usuario = {
                    "id": result[0],
                    "nome": result[1],
                    "tipo": result[2]
                }
                print(f"Login realizado com sucesso! Usuário: {usuario['nome']}")

                if usuario["tipo"] == "Administrador":
                    print("Redirecionando para tela de administrador...")
                    return {"sucesso": True, "tipo": "Administrador", "usuario": usuario}
                else:
                    print("Redirecionando para tela de visitante...")
                    return {"sucesso": True, "tipo": "Visitante/Usuario", "usuario": usuario}
            else:
                print("Email ou senha incorretos.")
                return {"sucesso": False, "mensagem": "Credenciais inválidas"}

        except Exception as e:
            print(f"Erro ao verificar login: {e}")
            return {"sucesso": False, "mensagem": str(e)}