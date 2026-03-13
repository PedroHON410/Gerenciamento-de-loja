import customtkinter as ctk
from tkinter import ttk
from Produto import Produto
from PIL import Image
import os
class PageNewProduct(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Adicionar Novo Produto")
        self.geometry("400x400")
        # Configuração de Cores
        self.cor_roxo = "#740E6D" 
        self.cor_roxo_escuro = "#740E6D"

        # Tema e Aparência
        ctk.set_appearance_mode("light")
        # Layout de Grid
        self.grid_columnconfigure(0, weight=1)
        self.criar_widgets()
    # Widgets
    def criar_widgets(self):
        # self.main_frame = ctk.CTkFrame(self, fg_color="white", corner_radius=0)
        # self.main_frame.grid(row=0, column=1, sticky="nsew", padx=20, pady=20)
        
    
        # self.cards_frame = ctk.CTkFrame(self.main_frame, fg_color="transparent")
        # self.cards_frame.pack(fill="x", pady=10)
        self.label_titulo = ctk.CTkLabel(self, text="Adicionar Novo Produto", 
                                        font=ctk.CTkFont(size=20, weight="bold"), text_color="black")
        
        self.label_titulo.pack(pady=20)
        self.entryNome = ctk.CTkEntry(self, placeholder_text="Nome do Produto", width=400)
        self.entry_preco = ctk.CTkEntry(self, width=300, placeholder_text="Preço")
        self.entry_quantidade = ctk.CTkEntry(self, width=300, placeholder_text="Quantidade")
        