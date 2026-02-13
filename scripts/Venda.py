from db_gerenciamento import create_connection, close_connection

class Venda:
    def __init__(self, id_venda, produto_venda, qtd_venda, desconto, id_produto_venda=None):
        self.id_venda = id_venda
        self.produto_venda = produto_venda
        self.qtd_venda = qtd_venda
        self.desconto = desconto
        self.id_produto_venda = id_produto_venda

    @staticmethod
    #Aqui deve ser implementada a função de buscar produto para venda, que deve solicitar o nome do produto ao usuário e buscar o produto no banco de dados. 
    # Caso o produto seja encontrado, deve retornar o id do produto para ser utilizado na venda.
    def buscar_produto_venda(self, produto_venda):
        connection = create_connection()
        cursor = connection.cursor()
        try:
            select_query = """ SELECT id_produto FROM produtos WHERE nome = %s"""
            cursor.execute(select_query, (produto_venda,))
            result = cursor.fetchone()
            if result:
                self.id_produto_venda = result[0]
                return self.id_produto_venda
            else:
                return 'Produto não encontrado para venda'
        except Exception as e:
            print(f"Erro ao buscar produto para venda: {e}")


    @staticmethod
    def vender(self, id_produto_venda, qtd_venda, desconto):
        connection = create_connection()
        cursor = connection.cursor()
        try:
            insert_query = """ INSERT INTO vendas (id_produto_venda, qtd_venda, desconto) VALUES (%s, %s, %s)"""
            values = (id_produto_venda, qtd_venda, desconto)
            cursor.execute(insert_query, values)
            connection.commit()
            print("Venda realizada com sucesso")
        except Exception as e:
            print(f"Erro ao realizar venda: {e}")
        finally:
            close_connection(connection)
        
        