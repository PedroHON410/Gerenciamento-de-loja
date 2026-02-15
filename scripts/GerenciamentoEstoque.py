from db_gerenciamento import close_connection, create_connection

class GerenciamentoEstoque:
    def __init__(self, qtd_reposicao, id_produto_estoque):
        self.qtd_reposicao = qtd_reposicao
        self.id_produto_estoque = id_produto_estoque
        
        
    def atualizar_estoque (self):
        connection = create_connection()
        cursor = connection.cursor()
        
        try:
            update_query = "UPDATE produtos SET qtd_estoque = qtd_estoque + %s WHERE id_produto = %s"
            cursor.execute(update_query, (self.qtd_reposicao, self.id_produto_estoque))
            connection.commit()
            print(f"Estoque do produto ID {self.id_produto_estoque} atualizado! Quantidade adicionada: {self.qtd_reposicao}")
        except Exception as e:
            print(f"Erro ao atualizar estoque: {e}")
        finally:
            close_connection(connection)