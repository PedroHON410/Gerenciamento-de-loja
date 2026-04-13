from db_gerenciamento import create_connection, close_connection
from decimal import Decimal
class Venda:
    def __init__(self, produto_nome, qtd_venda, desconto=0, id_cliente=None):
        self.produto_nome = produto_nome
        self.qtd_venda = qtd_venda
        self.desconto = desconto
        self.id_cliente = id_cliente
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
            if self.desconto != 0 or self.desconto != None:
                valor_total = self.valor_unitario * self.qtd_venda * (1 - Decimal(self.desconto) / 100)
            else:
                valor_total = self.valor_unitario * self.qtd_venda

            # Insere na tabela de vendas
            insert_query = """ 
                INSERT INTO vendas (id_produto, qtd_venda, desconto, valor_total, data_venda, cliente_id) 
                VALUES (%s, %s, %s, %s, NOW(), %s) 
            """
            cursor.execute(insert_query, (self.id_produto, self.qtd_venda, self.desconto, valor_total, self.id_cliente))

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

    def listar_vendas():
        connection = create_connection()
        cursor = connection.cursor()
        try:
            select_query = """
                SELECT v.id, p.nome, p.preco, v.qtd_venda, v.desconto, v.valor_total, v.data_venda, v.cliente_id
                FROM vendas v
                JOIN produtos p ON v.id_produto = p.id
                JOIN clientes c ON v.cliente_id = c.id
                ORDER BY v.data_venda DESC
                """
            cursor.execute(select_query)
            vendas = cursor.fetchall()
            return vendas
        except Exception as e:
            print(f"Erro ao listar vendas: {e}")
            return []
    
    def total_vendas():
        connection = create_connection()
        cursor = connection.cursor()
        try:
            cursor.execute("SELECT COUNT(*) FROM vendas")
            total = cursor.fetchone()[0]
            return total
        except Exception as e:
            print(f"Erro ao contar vendas: {e}")
            return 0
        
    def total_receita():
        connection = create_connection()
        cursor = connection.cursor()
        try:
            cursor.execute("SELECT SUM(valor_total) FROM vendas")
            total = cursor.fetchone()[0]
            return total if total else 0
        except Exception as e:
            print(f"Erro ao calcular receita: {e}")
            return 0
        