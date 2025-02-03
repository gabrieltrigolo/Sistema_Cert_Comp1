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
                    print("Usuário com este email já está cadastrado.")
                else:
                    # Verifica se há algum usuário com cargo "ADMIN"
                    cursor.execute(sql_check_admin)
                    result_admin = cursor.fetchone()

                    # Define o cargo como "ADMIN" caso não haja nenhum usuário com esse cargo ou a tabela esteja vazia
                    if not result_admin:
                        usuario.cargo = "ADMIN"

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
                        print("Usuário não cadastrado.")

                cursor.close()
                conn.close()
        except Exception as e:
            print(f"Erro ao inserir Usuário: {e}")

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
        try:
            conn = ConnectionFactory.get_connection()
            if conn:
                cursor = conn.cursor()

                # Verifica se o novo email já está sendo usado por outro usuário
                cursor.execute(sql_check_email, (usuario.email, usuario_id))
                result_email = cursor.fetchone()

                if result_email:
                    print("O email informado já está sendo utilizado por outro usuário.")
                else:
                    # Atualiza o usuário
                    cursor.execute(sql_update, (
                        usuario.nome,
                        usuario.senha,
                        usuario.email,
                        usuario.cargo,
                        usuario_id
                    ))
                    conn.commit()
                    if cursor.rowcount > 0:
                        print("Usuário atualizado com sucesso!")
                    else:
                        print(f"Usuário com ID {usuario_id} não foi atualizado. Verifique os dados.")

                cursor.close()
                conn.close()
        except Exception as e:
            print(f"Erro ao atualizar usuário: {e}")

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
                        usuarios.append({
                            'usuario_id': result[0],
                            'nome': result[1],
                            'email': result[2],
                            'cargo': result[3]
                        })

                    print(f"Listagem concluída. {len(usuarios)} usuário(s) encontrado(s).")
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
        SELECT * FROM usuario WHERE email = %s AND senha = %s
        """
        try:
            conn = ConnectionFactory.get_connection()
            if conn:
                cursor = conn.cursor()

                # Executa a query com os parâmetros
                cursor.execute(sql, (email, senha))

                # Verifica se encontrou algum usuário
                result = cursor.fetchone()

                cursor.close()
                conn.close()

                if result:
                    print("Login realizado com sucesso!")
                    return True
                else:
                    print("Email ou senha incorretos.")
                    return False

        except Exception as e:
            print(f"Erro ao verificar login: {e}")
            return False