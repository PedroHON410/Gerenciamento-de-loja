import customtkinter as ctk
from CTkMessagebox import CTkMessagebox
from tkinter import ttk
from Venda import Venda
from PIL import Image
import os
from Produto import Produto

class PageNovaVenda(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Registrar Nova Venda")
        self.geometry("900x550")
        self.cor_roxo_escuro = "#740E6D"
        
        ctk.set_appearance_mode("light")

        # Configuração do Grid Principal: Coluna 0 (Sidebar) fixa, Coluna 1 (Form) expande
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.criar_widgets()
        self.aba_vendas()
    def criar_widgets(self):
        # --- SIDEBAR ---
        self.sidebar = ctk.CTkFrame(self, width=200, corner_radius=0, fg_color=self.cor_roxo_escuro)
        self.sidebar.grid(row=0, column=0, sticky="nsew")
        
        self.logo_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "logo.png")
        self.logo_image = ctk.CTkImage(Image.open(self.logo_path), size=(150, 150))
        self.logo_label = ctk.CTkLabel(self.sidebar, image=self.logo_image, text="")
        self.logo_label.pack(pady=20)

        self.lbl_logo = ctk.CTkLabel(self.sidebar, text="VENDAS", text_color="white", font=("Arial", 20, "bold"))
        self.lbl_logo.pack(pady=20)

        #Botão Voltar
        self.btn_voltar = ctk.CTkButton(self.sidebar, text="Voltar", fg_color="transparent", text_color="white", hover_color="#5a0b54", command=self.voltar_btn)
        self.btn_voltar.pack(pady=10)

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
            text="+ Novo Produto", 
            fg_color=self.cor_roxo, hover_color=self.cor_roxo_escuro, command=self.abrir_tela_novo_produto)
        
        
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

    def todas_vendas(self):
        vendas = Venda.listar_vendas()
        for venda in vendas:
            print(f"ID: {venda[0]}, Produto: {venda[1]}, Quantidade: {venda[2]}, Data: {venda[3]}")

    def voltar_btn(self):
        self.destroy()
        from page1 import Page1
        app = Page1()
        app.mainloop()

    