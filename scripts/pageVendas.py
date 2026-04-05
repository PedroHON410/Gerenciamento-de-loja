import customtkinter as ctk
from tkinter import ttk
from Venda import Venda
from PIL import Image
import os
from Produto import Produto
from Cliente import Cliente
class PageVendas(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Sistema de Gestão de Loja - Vendas")
        self.geometry("1100x600")
        
        # Configuração de Cores
        self.cor_roxo = "#740E6D" # SlateBlue
        self.cor_roxo_escuro = "#740E6D"
        
        # Tema e Aparência
        ctk.set_appearance_mode("light")
        
        # Layout de Grid Principal (2 colunas: Menu e Conteúdo)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.criar_sidebar()
        self.criar_aba_vendas()
    
    def criar_sidebar(self):
        # Frame Lateral
        self.sidebar = ctk.CTkFrame(self, width=200, corner_radius=0, fg_color=self.cor_roxo_escuro)
        self.sidebar.grid(row=0, column=0, sticky="nsew")
        
        # Logo ou Título
        self.logo_image = ctk.CTkImage(light_image=Image.open(os.path.join(os.path.dirname(__file__), "logo.png")), size=(100, 100))
        self.logo_label = ctk.CTkLabel(self.sidebar, image=self.logo_image, text="")
        self.logo_label.pack(pady=30)

        # Botões do Menu
        botoes = ["Página Inicial", "Produtos", "Vendas", "Clientes", "Configurações"]
        for nome in botoes:
            btn = ctk.CTkButton(self.sidebar, text=nome, fg_color="transparent", 
                                text_color="white", hover_color=self.cor_roxo, anchor="w")
            btn.pack(fill="x", padx=20, pady=5)

    def criar_aba_vendas(self):
        # Frame Principal da Direita
        self.main_frame = ctk.CTkFrame(self, fg_color="white", corner_radius=0)
        self.main_frame.grid(row=0, column=1, sticky="nsew", padx=20, pady=20)
        
        # Header - Título e Botão Novo
        self.header_frame = ctk.CTkFrame(self.main_frame, fg_color="transparent")
        self.header_frame.pack(fill="x", pady=(0, 20))
        
        self.label_titulo = ctk.CTkLabel(self.header_frame, text="Gerenciamento de Vendas", 
                                        font=ctk.CTkFont(size=24, weight="bold"), text_color="black")
        self.label_titulo.pack(side="left")
        
        self.btn_novo = ctk.CTkButton(
            self.header_frame,
            text="+ Nova Venda",
            fg_color=self.cor_roxo,
            hover_color=self.cor_roxo_escuro,
            command=self.nova_venda
        )
        self.btn_novo.pack(side="right")

        # Cards de Resumo (Simulando os 3 cards da foto)
        self.aba_vendas()
    
    # def tela_vendas(self):
    #      # Frame Principal da Direita
    #     self.main_frame = ctk.CTkFrame(self, fg_color="white", corner_radius=0)
    #     self.main_frame.grid(row=0, column=1, sticky="nsew", padx=20, pady=20)
        
    #     # Header - Título e Botão Novo
    #     self.header_frame = ctk.CTkFrame(self.main_frame, fg_color="transparent")
    #     self.header_frame.pack(fill="x", pady=(0, 20))
        
    #     self.label_titulo = ctk.CTkLabel(self.header_frame, text="Gerenciamento de Vendas", 
    #                                     font=ctk.CTkFont(size=24, weight="bold"), text_color="black")
    #     self.label_titulo.pack(side="left")
        
    #     self.btn_novo = ctk.CTkButton(
    #         self.header_frame,
    #         text="+ Nova Venda",
    #         fg_color=self.cor_roxo,
    #         hover_color=self.cor_roxo_escuro,
    #         command=self.nova_venda
    #     )
        
        
    #     self.btn_novo.pack(side="right")

    #     # Cards de Resumo (Simulando os 3 cards da foto)
    #     self.cards_frame = ctk.CTkFrame(self.main_frame, fg_color="transparent")
    #     self.cards_frame.pack(fill="x", pady=10)
        
    #     self.card1 = self.criar_card(self.cards_frame, "Total Vendas", Venda.total_vendas())
    #     self.card2 = self.criar_card(self.cards_frame, "Total Receitas", Venda.total_receita())
    #     self.card3 = self.criar_card(self.cards_frame, "Clientes", Cliente.total_clientes())

    #     # Barra de Busca
    #     self.search_entry = ctk.CTkEntry(self.main_frame, placeholder_text="Buscar Venda...", width=400)
    #     self.search_entry.pack(pady=20, anchor="w")

    #     # Tabela (Treeview) - Para listar os produtos
    #     self.style = ttk.Style()
    #     self.style.configure("Treeview", rowheight=30, font=("Arial", 10))
    #     self.style.configure("Treeview.Heading", font=("Arial", 11, "bold"), foreground=self.cor_roxo)
        
    #     # Criando a tabela com as colunas ID, Nome, Preço, Estoque e Categoria
    #     self.tabela = ttk.Treeview(self.main_frame, columns=("ID", "Nome", "Preço", "Estoque","Categoria"), show="headings")
    #     self.tabela.heading("ID", text="ID Produto")
    #     self.tabela.heading("Nome", text="Nome do Item")
    #     self.tabela.heading("Preço", text="Preço")
    #     self.tabela.heading("Estoque", text="Estoque")
    #     self.tabela.heading("Categoria", text="Categoria")
        
    #     # Ajuste de largura das colunas
    #     self.tabela.column("ID", width=80)
    #     self.tabela.column("Preço", width=100)
        
    #     self.tabela.pack(fill="both", expand=True)
        # self.carregar_dados_iniciais()

    def aba_vendas(self):
        # --- FORMULÁRIO PRINCIPAL ---
        self.main_frame = ctk.CTkFrame(self, fg_color="white", corner_radius=0)
        self.main_frame.grid(row=0, column=1, sticky="nsew", padx=20, pady=20)
        
        # Header - Título e Botão Novo
        self.header_frame = ctk.CTkFrame(self.main_frame, fg_color="transparent")
        self.header_frame.pack(fill="x", pady=(0, 20))
        
        self.label_titulo = ctk.CTkLabel(self.header_frame, text="Gerenciamento de Vendas", 
                                        font=ctk.CTkFont(size=24, weight="bold"), text_color="black")
        self.label_titulo.pack(side="left")
        
        self.btn_novo = ctk.CTkButton(
            self.header_frame,
            text="+ Nova Venda", 
            fg_color=self.cor_roxo, hover_color=self.cor_roxo, command=self.nova_venda)
        
        
        self.btn_novo.pack(side="right")

        # Cards de Resumo (Simulando os 3 cards da foto)
        self.cards_frame = ctk.CTkFrame(self.main_frame, fg_color="transparent")
        self.cards_frame.pack(fill="x", pady=10)
        
        self.card1 = self.criar_card(self.cards_frame, "Total Vendas", Venda.total_vendas())
        self.card2 = self.criar_card(self.cards_frame, "Total Estoque", Produto.total_estoque())
        self.card3 = self.criar_card(self.cards_frame, "Total Receita", Venda.total_receita())

        # Barra de Busca
        self.search_entry = ctk.CTkEntry(self.main_frame, placeholder_text="Buscar Venda...", width=400)
        self.search_entry.pack(pady=20, anchor="w")

        # Tabela (Treeview) - Para listar os produtos
        self.style = ttk.Style()
        self.style.configure("Treeview", rowheight=30, font=("Arial", 10))
        self.style.configure("Treeview.Heading", font=("Arial", 11, "bold"), foreground=self.cor_roxo)
        
        # Criando a tabela com as colunas ID, Nome, Preço, Estoque e Categoria
        self.tabela = ttk.Treeview(self.main_frame, columns=("ID", "Produto", "Preço", "Quantidade","Desconto", "Valor", "Data"), show="headings")
        self.tabela.heading("ID", text="ID Venda")
        self.tabela.heading("Produto", text="Produto")
        self.tabela.heading("Preço", text="Preço")
        self.tabela.heading("Quantidade", text="Quantidade")
        self.tabela.heading("Desconto", text="Desconto")
        self.tabela.heading("Valor", text="Valor")
        self.tabela.heading("Data", text="Data")
        
        # Ajuste de largura das colunas
        self.tabela.column("ID", width=80)
        self.tabela.column("Preço", width=100)
        
        self.tabela.pack(fill="both", expand=True)
        self.carregar_dados_iniciais()

    def criar_card(self, master, titulo, valor):
        card = ctk.CTkFrame(master, fg_color=self.cor_roxo, width=200, height=80, corner_radius=10)
        card.pack(side="left", padx=10)
        card.pack_propagate(False)

        label_titulo = ctk.CTkLabel(card, text=titulo, font=ctk.CTkFont(size=14), text_color="white")
        label_titulo.pack(pady=(10, 0))

        label_valor = ctk.CTkLabel(card, text=str(valor), font=ctk.CTkFont(size=18, weight="bold"), text_color="white")
        label_valor.pack(pady=(5, 10))

        return card

    def todas_vendas(self):
        vendas = Venda.listar_vendas()
        for venda in vendas:
            print(f"ID: {venda[0]}, Produto: {venda[1]}, Preço: {venda[2]}, Quantidade: {venda[3]}, Desconto: {venda[4]}, Valor: {venda[5]}, Data: {venda[6]}")


    def nova_venda(self):
        from pageNovaVenda import PageNovaVenda
        try:
            self.destroy()  # Fecha a janela atual
            app = PageNovaVenda()  # Cria a nova janela
            app.mainloop()  # Inicia o loop da nova janela
        except ImportError as e:
            print(f"Erro ao importar PageNovaVenda: {e}")
    
    def carregar_dados_iniciais(self):
        for i in self.tabela.get_children():
            self.tabela.delete(i)

        # Chama o método que agora RETORNA a lista
        dados_do_banco = Venda.listar_vendas()
        
        for item in dados_do_banco:
            self.tabela.insert("", "end", values=(
                item[0], 
                item[1], 
                f"R$ {item[2]:.2f}", 
                item[3],
                f"R$ {item[4]:.2f}",
                f"R$ {item[5]:.2f}",
                item[6]
            ))
