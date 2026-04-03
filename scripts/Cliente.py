from db_gerenciamento import close_connection, create_connection
class Cliente:
    
    def __init__(self, nome_cliente, CPF, qtd_compras, faltando_pagar):
        self.nome_cliente = nome_cliente
        self.CPF = CPF
        self.qtd_compras = qtd_compras
        self.faltando_pagar = faltando_pagar


    def novo_cliente (self):
        connection = create_connection()
        cursor = connection.cursor()
        try:
            insert_query = """ INSERT INTO clientes (nome, CPF, qtd_compras, faltando_pagar) VALUES (%s, %s, %s, %s)"""
            values = (self.nome_cliente, self.CPF, self.qtd_compras, self.faltando_pagar)
            cursor.execute(insert_query, values)
            connection.commit()
            print(f"Cliente {self.nome_cliente} inserido com sucesso na tabela clientes")
        except Exception as e:
            print(f"Erro ao inserir cliente: {e}")
        finally:
            close_connection(connection)
    
    def listar_clientes():
        connection = create_connection()
        cursor = connection.cursor()
        try:
            select_query = "SELECT * FROM clientes"
            cursor.execute(select_query)
            clientes = cursor.fetchall()
            return clientes
        except Exception as e:
            print(f"Erro ao listar clientes: {e}")
            return []
        finally:
            close_connection(connection)
    
    def buscar_por_nome(nome):
        connection = create_connection()
        cursor = connection.cursor()
        try:
            select_query = "SELECT * FROM clientes WHERE nome = %s"
            cursor.execute(select_query, (nome,))
            cliente = cursor.fetchone()
            return cliente
        except Exception as e:
            print(f"Erro ao buscar cliente por nome: {e}")
            return None
        finally:
            close_connection(connection)
    
    def compra(self):
        self.qtd_compras += 1
        connection = create_connection()
        cursor = connection.cursor()
        try:
            update_query = "UPDATE clientes SET qtd_compras = %s WHERE nome = %s"
            cursor.execute(update_query, (self.qtd_compras, self.nome_cliente))
            connection.commit()
        except Exception as e:
            print(f"Erro ao atualizar quantidade de compras: {e}")
        finally:
            close_connection(connection)