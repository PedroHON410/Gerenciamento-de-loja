from db_gerenciamento import close_connection, create_connection

class GerenciamentoEstoque:
    def __init__(self, qtd_reposicao, id_produto_estoque, nome):
        self.qtd_reposicao = qtd_reposicao
        self.id_produto_estoque = id_produto_estoque
        self.nome = nome
        
        
    def adicionar_estoque (self):
        connection = create_connection()
        cursor = connection.cursor()
        try:
            update_query = "UPDATE produtos SET qtd_estoque = qtd_estoque + %s WHERE nome = %s"
            cursor.execute(update_query, (self.qtd_reposicao, self.nome))
            connection.commit()
            print(f"Estoque do produto {self.nome} atualizado! Quantidade adicionada: {self.qtd_reposicao}")
        except Exception as e:
            print(f"Erro ao atualizar estoque: {e}")
        finally:
            close_connection(connection)
    
    def remover_estoque (self):
        connection = create_connection()
        cursor = connection.cursor()
        
        try:
            update_query = "UPDATE produtos SET qtd_estoque = qtd_estoque - %s WHERE nome = %s"
            cursor.execute(update_query, (self.qtd_reposicao, self.nome))
            connection.commit()
            print(f"Estoque do produto {self.nome} atualizado! Quantidade removida: {self.qtd_reposicao}")
        except Exception as e:
            print(f"Erro ao atualizar estoque: {e}")
        finally:
            close_connection(connection)