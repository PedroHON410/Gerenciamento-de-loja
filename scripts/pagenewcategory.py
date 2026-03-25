import customtkinter as ctk
from CTkMessagebox import CTkMessagebox
from tkinter import ttk
from Produto import Produto
from PIL import Image
import os

class PageNewCategory(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Adicionar Nova Categoria")
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

        self.lbl_logo = ctk.CTkLabel(self.sidebar, text="CADASTRO", text_color="white", font=("Arial", 20, "bold"))
        self.lbl_logo.pack(pady=20)

        #Botão Voltar
        self.btn_voltar = ctk.CTkButton(self.sidebar, text="Voltar", fg_color="transparent", text_color="white", hover_color="#5a0b54", command=self.voltar_btn)
        self.btn_voltar.pack(pady=10)

        # --- FORMULÁRIO PRINCIPAL ---
        self.container_form = ctk.CTkFrame(self, fg_color="transparent")
        self.container_form.grid(row=0, column=1, padx=40, pady=40, sticky="nsew")

        # Categoria (Usando um ComboBox para o usuário escolher categorias existentes)
        self.combo_categoria = ttk.Combobox(self.container_form, state="readonly", width=38)
        self.combo_categoria['values'] = [cat[1] for cat in Produto.listar_categorias()]
        self.combo_categoria.set("Selecione a Categoria")
        self.combo_categoria.pack(pady=10)
        self.lbl_nova_categoria = ctk.CTkLabel(self.container_form, text="Adicionar Nova Categoria", font=("Arial", 14))
        self.lbl_nova_categoria.pack(pady=(20, 5), anchor="w")
        self.entry_nova_categoria = ctk.CTkEntry(self.container_form, placeholder_text="Nome da Nova Categoria", width=400, height=40)
        self.entry_nova_categoria.pack(pady=10)
        self.btn_add_categoria = ctk.CTkButton(self.container_form, text="Adicionar Categoria", fg_color="#5a0b54", command=self.adicionar_categoria)
        self.btn_add_categoria.pack(pady=10)

    def voltar_btn(self):
        self.destroy()
        from page1 import Page1
        app = Page1()
        app.mainloop()

    def adicionar_categoria(self):
        nova_categoria = self.entry_nova_categoria.get().strip()
        if not nova_categoria:
            CTkMessagebox(title="Erro", message="O nome da categoria não pode ser vazio.", icon="error")
            return
        
        if Produto.criar_categoria(nova_categoria):
            CTkMessagebox(title="Sucesso", message=f"Categoria '{nova_categoria}' adicionada com sucesso!", icon="check")
            #self.combo_categoria['values'] = [cat[1] for cat in Produto.listar_categorias()]
            self.entry_nova_categoria.delete(0, 'end')
        else:
            CTkMessagebox(title="Erro", message=f"Falha ao adicionar a categoria '{nova_categoria}'. Verifique se já existe ou tente novamente.", icon="error")
        