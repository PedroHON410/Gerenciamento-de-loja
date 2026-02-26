# import customtkinter as ctk
# class Page2(ctk.CTk):
#     def __init__(self, master=None):
#         super().__init__(master)
        
#         self.title("Gerenciar Produtos")
#         self.geometry("800x700")
#         ctk.set_appearance_mode("light")
        
#         # --- INTERFACE ---
#         self.label = ctk.CTkLabel(
#             self, 
#             text="Gerenciar Produtos", 
#             font=ctk.CTkFont(size=20, weight="bold")
#         )
#         self.label.pack(pady=10)

import customtkinter as ctk
from tkinter import ttk
from Produto import Produto

class Page2(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Sistema de Gestão de Loja - Produtos")
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
        self.criar_aba_produtos()

    def criar_sidebar(self):
        # Frame Lateral
        self.sidebar = ctk.CTkFrame(self, width=200, corner_radius=0, fg_color=self.cor_roxo_escuro)
        self.sidebar.grid(row=0, column=0, sticky="nsew")
        
        # Logo ou Título
        self.logo_label = ctk.CTkLabel(self.sidebar, text="LOJA APP", font=ctk.CTkFont(size=20, weight="bold"), text_color="white")
        self.logo_label.pack(pady=30)

        # Botões do Menu
        botoes = ["Dashboard", "Produtos", "Vendas", "Clientes", "Configurações"]
        for nome in botoes:
            btn = ctk.CTkButton(self.sidebar, text=nome, fg_color="transparent", 
                                text_color="white", hover_color=self.cor_roxo, anchor="w")
            btn.pack(fill="x", padx=20, pady=5)

    def criar_aba_produtos(self):
        # Frame Principal da Direita
        self.main_frame = ctk.CTkFrame(self, fg_color="white", corner_radius=0)
        self.main_frame.grid(row=0, column=1, sticky="nsew", padx=20, pady=20)
        
        # Header - Título e Botão Novo
        self.header_frame = ctk.CTkFrame(self.main_frame, fg_color="transparent")
        self.header_frame.pack(fill="x", pady=(0, 20))
        
        self.label_titulo = ctk.CTkLabel(self.header_frame, text="Gerenciamento de Produtos", 
                                        font=ctk.CTkFont(size=24, weight="bold"), text_color="black")
        self.label_titulo.pack(side="left")
        
        self.btn_novo = ctk.CTkButton(self.header_frame, text="+ Novo Produto", 
                                      fg_color=self.cor_roxo, hover_color=self.cor_roxo_escuro)
        self.btn_novo.pack(side="right")

        # Cards de Resumo (Simulando os 3 cards da foto)
        self.cards_frame = ctk.CTkFrame(self.main_frame, fg_color="transparent")
        self.cards_frame.pack(fill="x", pady=10)
        
        self.card1 = self.criar_card(self.cards_frame, "Total Produtos",Produto.total_produtos())
        self.card2 = self.criar_card(self.cards_frame, "Estoque Baixo", "15")
        self.card3 = self.criar_card(self.cards_frame, "Categorias", "23")

        # Barra de Busca
        self.search_entry = ctk.CTkEntry(self.main_frame, placeholder_text="Buscar Produto...", width=400)
        self.search_entry.pack(pady=20, anchor="w")

        # Tabela (Treeview) - Para listar os produtos
        self.style = ttk.Style()
        self.style.configure("Treeview", rowheight=30, font=("Arial", 10))
        self.style.configure("Treeview.Heading", font=("Arial", 11, "bold"), foreground=self.cor_roxo)
        
        # Criando a tabela com as colunas ID, Nome, Preço, Estoque e Categoria
        self.tabela = ttk.Treeview(self.main_frame, columns=("ID", "Nome", "Preço", "Estoque","Categoria"), show="headings")
        self.tabela.heading("ID", text="ID Produto")
        self.tabela.heading("Nome", text="Nome do Item")
        self.tabela.heading("Preço", text="Preço")
        self.tabela.heading("Estoque", text="Estoque")
        self.tabela.heading("Categoria", text="Categoria")
        
        # Ajuste de largura das colunas
        self.tabela.column("ID", width=80)
        self.tabela.column("Preço", width=100)
        
        self.tabela.pack(fill="both", expand=True)
        self.carregar_dados_iniciais()

    def criar_card(self, master, titulo, valor):
        card = ctk.CTkFrame(master, fg_color=self.cor_roxo, width=200, height=80, corner_radius=10)
        card.pack(side="left", padx=10)
        card.pack_propagate(False)
        
        lbl_titulo = ctk.CTkLabel(card, text=titulo, text_color="white", font=("Arial", 12))
        lbl_titulo.pack(pady=(10, 0))
        
        lbl_valor = ctk.CTkLabel(card, text=valor, text_color="white", font=("Arial", 18, "bold"))
        lbl_valor.pack()
        return card

    def carregar_dados_iniciais(self):
        for i in self.tabela.get_children():
            self.tabela.delete(i)

        # Chama o método que agora RETORNA a lista
        dados_do_banco = Produto.listar_produtos()
        
        for item in dados_do_banco:
            # item[0]=ID, item[1]=Nome, item[2]=Categoria, item[3]=Preço, item[4]=Estoque
            self.tabela.insert("", "end", values=(
                item[0], 
                item[1], 
                f"R$ {item[2]:.2f}", 
                item[3]
            ))
