from db_gerenciamento import create_connection, close_connection


class Produto:
    #Criando a estrutura da classe Produto, com os atributos. id_produto e categoria_id são feitos para serem usados como chaves estrangeiras no banco de dados,
    #para relacionar os produtos com suas categorias.    
    def __init__(self, nome, preco, qtd_estoque, id_produto=None, categoria_id=None):
        self.id_produto = id_produto
        self.nome = nome
        self.preco = preco
        self.qtd_estoque = qtd_estoque
        self.categoria_id = categoria_id
    
    #Método para inserir um novo produto no banco de dados.
    @staticmethod
    def insert_produto(nome, preco, qtd_estoque, categoria):
        connection = create_connection()
        cursor = connection.cursor()
        try:
            insert_query = """ INSERT INTO produtos (nome, preco, qtd_estoque, categoria_id) VALUES (%s, %s, %s, %s)"""
            #Values é uma tupla que contém os valores a serem inseridos na tabela produtos, sendo mais fácil de ler ou alterar futuramente.
            values = (nome, preco, qtd_estoque, categoria)
            cursor.execute(insert_query, values)
            connection.commit()
            print("Produto inserido com sucesso na tabela produtos")
        except Exception as e:
            print(f"Erro ao inserir produto: {e}")
        finally:
            close_connection(connection)

    #Método para criar uma nova categoria no banco de dados, caso a categoria do produto a ser inserido não exista ou queira criar uma nova categoria.
    @staticmethod
    def criar_categoria(nome_categoria):
        connection = create_connection()
        cursor = connection.cursor()
        try:
            insert_query = """ INSERT INTO categorias (nome) VALUES (%s)"""
            cursor.execute(insert_query, (nome_categoria,))
            connection.commit()
            print(f"Categoria: {nome_categoria} criada com sucesso na tabela categorias")
        except Exception as e:
            print(f"Erro ao criar categoria: {e}")
        finally:
            close_connection(connection)
    

    #Método para buscar o id da categoria no banco de dados, para relacionar o produto com a categoria correta. 
    #O método retorna o id da categoria encontrada ou None se a categoria não for encontrada.
    @staticmethod
    def buscar_categoria(categoria):
        connection = create_connection()
        cursor = connection.cursor()
        try:
            select_query = """ SELECT id FROM categorias WHERE nome = %s"""
            cursor.execute(select_query, (categoria))
            categoria_result = cursor.fetchone()
            connection.close()
            return categoria_result[0] if categoria_result else None
        except Exception as e:
            print(f"Erro ao buscar categoria: {e}")



    # def novo_produto (self, nome, preco, qtd_estoque):
    #     if not produto in self.categoria:
    #         novo_id = 1
    #     else:
    #         ultimo_produto = self.categoria[-1]
    #         novo_id = ultimo_produto['id'] + 1
    #     self.nome = nome
    #     self.preco = preco
    #     self.qtd_estoque = qtd_estoque
    #     self.produto_novo = {
    #         'id': self.id_produto,
    #         'nome': self.nome,
    #         'preco': self.preco,
    #         'qtd_estoque': self.qtd_estoque
    #     }
    #     buscar_categoria = str(input('Categoria do produto: '))
    #     if buscar_categoria in self.list_categoria:
    #         return self.list_categoria[buscar_categoria].append(self.produto_novo)
    #     else:
    #         return 'Categoria não encontrada. Por favor, crie a categoria primeiro.'

    # def nova_categoria (self):
    #     nova_categoria = str(input('Nome da categoria: '))
    #     if nova_categoria not in self.list_categoria:
    #         self.list_categoria[nova_categoria] = []
    #         return self.list_categoria
    #     elif nova_categoria in self.list_categoria:
    #         return 'Categoria já existe'
    #     else:
    #         return 'Erro inesperado'


class GerenciamentoEstoque:
    def __init__(self, qtd_reposicao, id_produto_estoque):
        self.qtd_reposicao = qtd_reposicao
        self.id_produto_estoque = id_produto_estoque
        
    def atualizar_estoque (self):
        self.id_produto_estoque = int(input('ID do produto para atualizar o estoque: '))
        if self.id_produto_estoque in Produto.produtos_cadastrados:
            qtd_reposicao = int(input('Quantidade para reposição: '))
            if qtd_reposicao > 0:
                Produto.qtd_estoque += qtd_reposicao
                return Produto.qtd_estoque
            else:
                return 'Quantidade inválida para reposição'
        else:
            return 'Produto não encontrado no estoque'

class Venda:
    def buscar_produto_venda(self):
        self.id_produto_venda = id_produto_venda
        if self.id_produto_venda in Produto.produtos_cadastrados:
            return Produto.produtos_cadastrados[self.id_produto_venda]
        else:
            return 'Produto não encontrado para venda'
        
    def __init__(self, id_venda, qtd_venda, desconto):
        self.id_venda = id_venda
        self.qtd_venda = qtd_venda
        self.desconto = desconto


    def vender (self): 
        self.id_venda
        

class Cliente:
    
    def __init__(self, id_cliente, nome_cliente, CPF, pontos):
        self.id_cliente = id_cliente
        self.nome_cliente = nome_cliente
        self.historico_compras = []
        self.CPF = CPF
        self.pontos = pontos
        self.cliente_novo = {}
        self.clientes_cadastrados = []

    def novo_cliente (self):
        if not self.clientes_cadastrados:
            novo_id = 1
        else:
            ultimo_cliente = self.clientes_cadastrados[-1]
            novo_id = ultimo_cliente['id_cliente'] + 1
        self.id_cliente = novo_id
        self.nome_cliente = str(input('Nome do cliente: '))
        self.CPF = str(input('CPF do cliente: '))
        self.cliente_novo = {
            'id_cliente': self.id_cliente,
            'nome_cliente': self.nome_cliente,
            'CPF': self.CPF,
            'pontos': self.pontos
        }
        return self.clientes_cadastrados.append(self.cliente_novo)

if __name__ == "__main__":
    produto = Produto(1, 'Caneta', 2.5, 100)
    produto.nova_categoria()
    produto.novo_produto()
    print(produto.list_categoria)