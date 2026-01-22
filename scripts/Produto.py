class Produto:
    def __init__(self, id_produto , nome, preco, qtd_estoque):
        self.id_produto = id_produto
        self.nome = nome
        self.preco = preco
        self.categoria = []
        self.qtd_estoque = qtd_estoque
        self.list_categoria = {}
        self.produtos_cadastrados = []


    def novo_produto (self):
        if not self.categoria:
            novo_id = 1
        else:
            ultimo_produto = self.categoria[-1]
            novo_id = ultimo_produto['id'] + 1
        self.nome = str(input('Nome do produto: '))
        self.preco = float(input('Preço: '))
        self.qtd_estoque = int(input('Quantidade: '))
        self.produto_novo = {
            'id': self.id_produto,
            'nome': self.nome,
            'preco': self.preco,
            'qtd_estoque': self.qtd_estoque
        }
        buscar_categoria = str(input('Categoria do produto: '))
        if buscar_categoria in self.list_categoria:
            return self.list_categoria[buscar_categoria].append(self.produto_novo)
        else:
            return 'Categoria não encontrada. Por favor, crie a categoria primeiro.'

    def nova_categoria (self):
        nova_categoria = str(input('Nome da categoria: '))
        if nova_categoria not in self.list_categoria:
            self.list_categoria[nova_categoria] = []
            return self.list_categoria
        elif nova_categoria in self.list_categoria:
            return 'Categoria já existe'
        else:
            return 'Erro inesperado'

class GerenciamentoEstoque:
    
    def atualizar_estoque (self, qtd_vendida, qtd_reposicao):
        if qtd_vendida > self.qtd_estoque:
            return 'Estoque insuficiente'
        elif qtd_vendida <= self.qtd_estoque:
            self.qtd_estoque -= qtd_vendida
            return self.qtd_estoque
        elif qtd_reposicao > 0:
            self.qtd_estoque += qtd_reposicao
            return self.qtd_estoque
        else:
            return 'Quantidade inválida'

class Venda:
    def __init__(self, id_venda, qtd_venda, desconto):
        self.id_venda = id_venda
        self.qtd_venda = qtd_venda
        self.desconto = desconto


    def vender (self): 
        self.id_venda += 1
        

class Cliente:
    
    def __init__(self, id_cliente, nome_cliente, historico_compras, CPF, pontos):
        self.id_cliente = id_cliente
        self.nome_cliente = nome_cliente
        self.historico_compras = historico_compras
        self.CPF = CPF
        self.pontos = pontos

print('Hello world')