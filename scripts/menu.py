from unittest import case
from Produto import Produto
from Produto import Venda
class GerenciamentoLoja:
    def menu_principal(escolha):

    print("Sistema de Gerenciamento de Loja")
    print("1 - Gerenciar Produtos")
    print("2 - Gerenciar Vendas")
    print("3 - Gerenciar Clientes")
    print("4 - Gerenciamento de Estoque")
    print("0 - Sair")
    escolha = int(input("Escolha uma opção (1-4): "))
    if escolha == '1':
        print("Gerenciamento de Produtos selecionado.")
        print('1 - Adicionar Produto')
        print('2 - Adicionar Categoria')
        print('3 - Listar Produtos')
        print('4 - Voltar ao Menu Principal')

        opcao_produto = int(input("Escolha uma opção (1-4): "))
        match opcao_produto:
                #Aqui deve ser implementada a função de adicionar produto, que deve solicitar o nome, preço, quantidade e categoria do produto. 
                # A função deve verificar se a categoria existe antes de adicionar o produto. Caso a categoria não exista, deve solicitar ao usuário para criar a categoria primeiro.
            
            case 1:
                nome = str(input('Nome do produto: '))
                preco = float(input('Preço: '))
                qtd_estoque = int(input('Quantidade: '))
                categoria = str(input('Categoria: '))
                categoria_encontrada = Produto.buscar_categoria(categoria)
                if not categoria_encontrada:
                    print('Categoria não encontrada. Por favor, crie a categoria primeiro.')
                    categoria = str(input('Nome da nova categoria: '))
                    Produto.criar_categoria(categoria)
                produto = Produto(nome, preco, qtd_estoque)
                produto.insert_produto(nome, preco, qtd_estoque, categoria)


            #Criando uma  nova categoria, solicitando o nome da categoria ao usuário e verificando se a categoria já existe antes de criar a nova categoria. 
            # Caso a categoria já exista, deve informar ao usuário que a categoria já existe.
            case 2:
                nova_categoria = str(input('Nome da nova categoria: '))
                Produto.criar_categoria(nova_categoria)
            
            
            #Aqui deve ser implementada a função de listar produtos, que deve buscar os produtos cadastrados no banco de dados e exibir as informações do produto.
            case 3:
                Produto.listar_produtos()
        

            #Aqui deve ser implementada a função de voltar ao menu principal, que deve retornar ao menu principal do sistema.
            case 4:
                print("Retornando ao Menu Principal.")

        
            case 4:
                print("Opção inválida. Retornando ao Menu Principal.")
    elif escolha == '2':
        print("Gerenciamento de Vendas selecionado.")
        venda = Venda()
        venda.registrar_venda()        