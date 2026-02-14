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
            # 1. Busca o produto para pegar ID e Preço atual
            cursor.execute("SELECT id_produto, preco FROM produtos WHERE nome = %s", (self.produto_nome,))
            produto = cursor.fetchone()

            if not produto:
                print("Produto não encontrado!")
                return

            self.id_produto = produto[0]
            self.valor_unitario = produto[2]
            
            # 2. Realiza o cálculo
            if self.desconto > 0:
                valor_total = (self.valor_unitario * self.qtd_venda) - (self.desconto/100)
            else:
                valor_total = self.valor_unitario * self.qtd_venda

            # 3. Insere na tabela de vendas (incluindo o ID do produto e valor total)
            insert_query = """ 
                INSERT INTO vendas (id_produto, qtd_venda, desconto, valor_total) 
                VALUES (%s, %s, %s, %s) 
            """
            cursor.execute(insert_query, (self.id_produto, self.qtd_venda, self.desconto, valor_total))
            
            connection.commit()
            print(f"Venda de {self.produto_nome} realizada! Total: R$ {valor_total:.2f}")

        except Exception as e:
            print(f"Erro ao realizar venda: {e}")
        finally:
            close_connection(connection)