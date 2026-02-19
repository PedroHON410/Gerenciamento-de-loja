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
    def insert_produto(self):
        connection = create_connection()
        cursor = connection.cursor()
        try:
            insert_query = """ INSERT INTO produtos (nome, preco, qtd_estoque, categoria_id) VALUES (%s, %s, %s, %s)"""
            #Values é uma tupla que contém os valores a serem inseridos na tabela produtos, sendo mais fácil de ler ou alterar futuramente.
            values = (self.nome, self.preco, self.qtd_estoque, self.categoria_id)
            cursor.execute(insert_query, values)
            connection.commit()
            print("Produto inserido com sucesso na tabela produtos")
        except Exception as e:
            print(f"Erro ao inserir produto: {e}")
        finally:
            close_connection(connection)


    #Método primeiro busca se já existe categoria na tabela, se existir não cria, caso contrario, cria uma nova categoria no banco de dados.
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

    #Método para listar os produtos cadastrados no banco de dados, exibindo as informações do produto, como nome, preço, quantidade em estoque e categoria.
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

