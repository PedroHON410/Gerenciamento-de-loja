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


    #Método primeiro busca se já existe categoria na tabela, se existir não cria, caso contrario, cria uma nova categoria no banco de dados.
    @staticmethod
    def criar_categoria(nome_categoria):
        connection = create_connection()
        cursor = connection.cursor()
        try:
            if Produto.buscar_categoria(nome_categoria):
                return f"Categoria: {nome_categoria} já existe na tabela categorias"

            else:    
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


    @staticmethod
    def listar_produtos():
        connection = create_connection()
        cursor = connection.cursor()
        try:
            select_query = """ SELECT p.id_produto, p.nome, p.preco, p.qtd_estoque, c.nome AS categoria FROM produtos p JOIN categorias c ON p.categoria_id = c.id"""
            cursor.execute(select_query)
            produtos = cursor.fetchall()
            print("Produtos cadastrados:")
            for produto in produtos:
                print(f"ID: {produto[0]}, Nome: {produto[1]}, Preço: {produto[2]}, Quantidade em Estoque: {produto[3]}, Categoria: {produto[4]}")
        except Exception as e:
            print(f"Erro ao listar produtos: {e}")
        finally:
            close_connection(connection)

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