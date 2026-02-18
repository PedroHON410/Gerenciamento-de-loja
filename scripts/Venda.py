from db_gerenciamento import create_connection, close_connection

class Venda:
    def __init__(self, produto_nome, qtd_venda, desconto=0):
        self.produto_nome = produto_nome
        self.qtd_venda = qtd_venda
        self.desconto = desconto
        self.id_produto = None
        self.valor_unitario = 0

    def processar_venda(self):
        connection = create_connection()
        cursor = connection.cursor()
        try:
            # Busca o produto usando o self.produto_nome
            select_query = "SELECT id, preco FROM produtos WHERE nome = %s"
            cursor.execute(select_query, (self.produto_nome,))
            produto = cursor.fetchone()

            if not produto:
                print(f"Produto '{self.produto_nome}' não encontrado!")
                return

            self.id_produto = produto[0]
            self.valor_unitario = produto[1]

            # Cálculo correto do desconto percentual
            total_bruto = self.valor_unitario * self.qtd_venda
            valor_total = total_bruto * (1 - self.desconto / 100)

            # Insere na tabela de vendas
            insert_query = """ 
                INSERT INTO vendas (id_produto, qtd_venda, desconto, valor_total) 
                VALUES (%s, %s, %s, %s) 
            """
            cursor.execute(insert_query, (self.id_produto, self.qtd_venda, self.desconto, valor_total))

            # Atualiza o estoque (Atenção ao nome da coluna: id ou id_produto?)
            update_query = "UPDATE produtos SET qtd_estoque = qtd_estoque - %s WHERE id = %s"
            cursor.execute(update_query, (self.qtd_venda, self.id_produto))
            
            connection.commit()
            print(f"Venda de {self.produto_nome} realizada! Total: R$ {valor_total:.2f}")

        except Exception as e:
            connection.rollback() # Importante: desfaz alterações em caso de erro
            print(f"Erro ao realizar venda: {e}")
        finally:
            close_connection(connection)
