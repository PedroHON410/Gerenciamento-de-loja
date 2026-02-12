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