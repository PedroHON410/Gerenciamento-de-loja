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