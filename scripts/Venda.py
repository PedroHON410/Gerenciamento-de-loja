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
        