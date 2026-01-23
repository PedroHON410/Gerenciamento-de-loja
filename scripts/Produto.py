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
    def __init__(self, id_venda, qtd_venda, desconto):
        self.vendas = []
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
