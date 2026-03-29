import customtkinter as ctk
from CTkMessagebox import CTkMessagebox
from tkinter import ttk
from Venda import Venda
from PIL import Image
import os

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

    def voltar_btn(self):
        self.destroy()
        from page1 import Page1
        app = Page1()
        app.mainloop()