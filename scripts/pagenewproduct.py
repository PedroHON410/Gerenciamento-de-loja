import customtkinter as ctk
from tkinter import ttk
from Produto import Produto
from PIL import Image
import os
class PageNewProduct(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Adicionar Novo Produto")
        self.geometry("800x600")
        # Configuração de Cores
        self.cor_roxo_escuro = "#740E6D"

        # Tema e Aparência
        ctk.set_appearance_mode("light")
        # Layout de Grid
        self.grid_columnconfigure(0, weight=1)
        self.criar_widgets()
    # Widgets
    def criar_widgets(self):
        self.sidebar = ctk.CTkFrame(self, width=200, corner_radius=0, fg_color=self.cor_roxo_escuro)
        self.sidebar.grid(row=0, column=0, sticky="nsew")
        self.search_entry = ctk.CTkEntry(self.sidebar, placeholder_text="Buscar Produto...", width=100)
        self.search_entry.pack(pady=20)
        
        self.label_titulo.pack(pady=0)
        self.entryNome = ctk.CTkEntry(self, placeholder_text="Nome do Produto", width=300)
        self.entry_preco = ctk.CTkEntry(self, width=300, placeholder_text="Preço")
        self.entry_quantidade = ctk.CTkEntry(self, width=300, placeholder_text="Quantidade")
    

    def criar_card(self, master, titulo, valor):
        card = ctk.CTkFrame(master, fg_color=self.cor_roxo_escuro, width=200, corner_radius=10)
        card.pack(side="top", padx=10)
        card.pack_propagate(False)
        
        lbl_titulo = ctk.CTkLabel(card, text=titulo, text_color="white", font=("Arial", 12))
        lbl_titulo.pack(pady=(10, 0))
        
        lbl_valor = ctk.CTkLabel(card, text=valor, text_color="white", font=("Arial", 18, "bold"))
        lbl_valor.pack()
        return card