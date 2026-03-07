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
        # Widgets
        self.label_titulo = ctk.CTkLabel(self, text="Adicionar Novo Produto", 
                                        font=ctk.CTkFont(size=20, weight="bold"), text_color="black")
        
        self.label_nome = ctk.CTkLabel(self, text="Nome do Produto:", text_color="black")
        self.entry_nome = ctk.CTkEntry(self)
