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