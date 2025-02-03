from ..dao.ConnectionFactory import ConnectionFactory
from ..model.Beneficiario import Beneficiario

class BeneficiarioDAO:

    def inserir(self, beneficiario):
        sql_check = """
        SELECT 1 FROM beneficiario WHERE cnpj_cpf = %s
        """
        sql_insert = """
        INSERT INTO beneficiario (nome, email, cnpj_cpf)
        VALUES (%s, %s, %s)
        """
        try:
            conn = ConnectionFactory.get_connection()
            if conn:
                cursor = conn.cursor()

                # Verifica se o cnpj_cpf já existe
                cursor.execute(sql_check, (beneficiario.identificador,))
                result = cursor.fetchone()

                if result:
                    print("Beneficiário com este CNPJ/CPF já está cadastrado.")
                else:
                    # Insere o novo beneficiário
                    cursor.execute(sql_insert, (
                        beneficiario.nome,
                        beneficiario.email,
                        beneficiario.identificador
                    ))
                    conn.commit()
                    if cursor.rowcount > 0:
                        print("Beneficiário cadastrado com sucesso!")
                    else:
                        print("Beneficiário não cadastrado.")

                cursor.close()
                conn.close()
        except Exception as e:
            print(f"Erro ao inserir Beneficiário: {e}")

    def atualizar(self, beneficiario):
        sql_update = """
        UPDATE beneficiario
        SET nome = %s, email = %s
        WHERE cnpj_cpf = %s
        """
        try:
            conn = ConnectionFactory.get_connection()
            if conn:
                cursor = conn.cursor()
                cursor.execute(sql_update, (
                    beneficiario.nome,
                    beneficiario.email,
                    beneficiario.identificador
                ))
                conn.commit()
                if cursor.rowcount > 0:
                    print("Beneficiário atualizado com sucesso!")
                else:
                    print("Beneficiário não encontrado.")

                cursor.close()
                conn.close()
        except Exception as e:
            print(f"Erro ao atualizar Beneficiário: {e}")

    def buscarPorId(self, cnpj_cpf):
        sql_select = """
        SELECT * FROM beneficiario WHERE cnpj_cpf = %s
        """
        try:
            conn = ConnectionFactory.get_connection()
            if conn:
                cursor = conn.cursor()
                cursor.execute(sql_select, (cnpj_cpf,))
                result = cursor.fetchone()
                cursor.close()
                conn.close()
                if result:
                    return Beneficiario(*result)
                else:
                    print("Beneficiário não encontrado.")
                    return None
        except Exception as e:
            print(f"Erro ao buscar Beneficiário: {e}")
            return None

    def listarTodosBeneficiarios(self):
        sql_select_all = """
        SELECT beneficiario_id, nome, email, cnpj_cpf FROM beneficiario
        """
        try:
            conn = ConnectionFactory.get_connection()
            if conn:
                cursor = conn.cursor()
                cursor.execute(sql_select_all)
                results = cursor.fetchall()
                cursor.close()
                conn.close()
                beneficiarios = []
                for result in results:
                    beneficiarios.append((result[3], result[1], result[2]))
                return beneficiarios
        except Exception as e:
            print(f"Erro ao listar Beneficiários: {e}")
            return []

    def deletarBeneficiario(self, cnpj_cpf):
        sql_delete = """
        DELETE FROM beneficiario WHERE cnpj_cpf = %s
        """
        try:
            conn = ConnectionFactory.get_connection()
            if conn:
                cursor = conn.cursor()
                cursor.execute(sql_delete, (cnpj_cpf,))
                conn.commit()
                if cursor.rowcount > 0:
                    print("Beneficiário deletado com sucesso!")
                else:
                    print("Beneficiário não encontrado.")

                cursor.close()
                conn.close()
        except Exception as e:
            print(f"Erro ao deletar Beneficiário: {e}")
