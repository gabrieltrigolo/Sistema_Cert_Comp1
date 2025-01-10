from ..dao.ConnectionFactory import ConnectionFactory
from ..model.Usuario import Usuario

class UsuarioDAO:

    def inserir(self, usuario):
        if not usuario or not usuario.nome or not usuario.email or not usuario.senha:
            raise ValueError("Nome, email e senha não podem ser nulos.")

        insert_usuario_sql = """
            INSERT INTO usuario (nome, email, senha)
            VALUES (%s, %s, %s)
        """

        try:
            # Conectar ao banco de dados
            conn = ConnectionFactory.get_connection()
            with conn.cursor() as cursor:
                # Inserir os dados do usuário
                cursor.execute(insert_usuario_sql, (
                    usuario.nome,
                    usuario.email,
                    usuario.senha,
                ))

                # Confirmar a transação
                conn.commit()
                print("Usuário cadastrado com sucesso!")

        except Exception as e:
            if conn:
                conn.rollback()
            print(f"Erro ao inserir usuário: {e}")
            raise

        finally:
            if conn:
                conn.close()

    def buscarPorId(self, usuario_id):
        select_usuario_sql = """
            SELECT
                u.id_usuario AS id_usuario,
                u.nome AS nome_usuario,
                u.email AS email_usuario,
                u.senha AS senha_usuario
            FROM
                usuario u
            WHERE
                u.id_usuario = %s;
        """

        try:
            # Conectar ao banco de dados
            conn = ConnectionFactory.get_connection()
            with conn.cursor() as cursor:
                cursor.execute(select_usuario_sql, (usuario_id,))
                result = cursor.fetchone()
                if result:
                    return Usuario(idUsuario=result[0], nome=result[1], email=result[2], senha=result[3])
                else:
                    return None

        except Exception as e:
            print(f"Erro ao buscar usuário por ID: {e}")
            raise

        finally:
            if conn:
                conn.close()

    def atualizar(self, usuario):
        sql_usuario = """
        UPDATE usuario
        SET nome = %s, email = %s, senha = %s
        WHERE id_usuario = %s
        """
        try:
            conn = ConnectionFactory.get_connection()
            if conn:
                cursor = conn.cursor()

                # Atualizar os dados do usuário
                cursor.execute(sql_usuario, (
                    usuario.nome,
                    usuario.email,
                    usuario.senha,
                    usuario.idUsuario
                ))

                conn.commit()
                print("Usuário atualizado com sucesso!")

                cursor.close()
                conn.close()

        except Exception as e:
            print(f"Erro ao atualizar usuário: {e}")

    def buscarPorEmail(self, email):
        select_usuario_sql = """
            SELECT
                u.id_usuario AS id_usuario,
                u.nome AS nome_usuario,
                u.email AS email_usuario,
                u.senha AS senha_usuario
            FROM
                usuario u
            WHERE
                u.email = %s;
        """

        try:
            # Conectar ao banco de dados
            conn = ConnectionFactory.get_connection()
            with conn.cursor() as cursor:
                cursor.execute(select_usuario_sql, (email,))
                result = cursor.fetchone()
                if result:
                    return Usuario(idUsuario=result[0], nome=result[1], email=result[2], senha=result[3])
                else:
                    return None

        except Exception as e:
            print(f"Erro ao buscar usuário por email: {e}")
            raise

        finally:
            if conn:
                conn.close()
