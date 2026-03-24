import customtkinter as ctk
from CTkMessagebox import CTkMessagebox
from tkinter import ttk
from Produto import Produto
from PIL import Image
import os
class PageNewProduct(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Adicionar Novo Produto")
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

        self.lbl_instrucao = ctk.CTkLabel(self.container_form, text="Preencha os dados do produto", font=("Arial", 18, "bold"))
        self.lbl_instrucao.pack(pady=(0, 20), anchor="w")

        # Nome
        self.entry_nome = ctk.CTkEntry(self.container_form, placeholder_text="Nome do Produto", width=400, height=40)
        self.entry_nome.pack(pady=10)
        

        # Preço
        self.entry_preco = ctk.CTkEntry(self.container_form, placeholder_text="Preço (Ex: 99.90)", width=400, height=40)
        self.entry_preco.pack(pady=10)

        # Quantidade
        self.entry_quantidade = ctk.CTkEntry(self.container_form, placeholder_text="Quantidade em Estoque", width=400, height=40)
        self.entry_quantidade.pack(pady=10)

        # Categoria (Usando um ComboBox para o usuário escolher categorias existentes)
        # Aqui depois você pode buscar as categorias do banco com Produto.listar_categorias()
        self.combo_categoria = ctk.CTkComboBox(self.container_form, values=[cat[1] for cat in Produto.listar_categorias()], width=400, height=40)
        self.combo_categoria.set("Selecione a Categoria")
        self.combo_categoria.pack(pady=10)

        # Opção para adicionar nova categoria
        self.lbl_nova_categoria = ctk.CTkLabel(self.container_form, text="Adicionar Nova Categoria", font=("Arial", 14))
        self.lbl_nova_categoria.pack(pady=(20, 5), anchor="w")
        self.btn_nova_categoria = ctk.CTkButton(self.container_form, text="Adicionar Categoria", fg_color="#5a0b54", hover_color="#3e043c", command=self.adicionar_categoria)
        self.btn_nova_categoria.pack(pady=10)

        

        # Botão Salvar
        self.btn_salvar = ctk.CTkButton(self.container_form, text="SALVAR PRODUTO", 
                                        fg_color=self.cor_roxo_escuro, 
                                        hover_color="#5a0b54",
                                        width=400, height=50, font=("Arial", 14, "bold"),
                                        command=self.salvar_dados)
        self.btn_salvar.pack(pady=30)

    def salvar_dados(self):
        nome = self.entry_nome.get()
        preco = self.entry_preco.get()
        quantidade = self.entry_quantidade.get()
        categoria = self.combo_categoria.get()

        if not nome or not preco or not quantidade or categoria == "Selecione a Categoria":
            CTkMessagebox(title="Erro", message="Por favor, preencha todos os campos corretamente.")
            return
        
        try:
            preco = float(preco)
            quantidade = int(quantidade)
        except ValueError:
            CTkMessagebox(title="Erro", message="Preço deve ser um número e Quantidade deve ser um inteiro.")
            return

        # Aqui você pode criar o objeto Produto e chamar o método insert_produto
        nova_categoria_id = Produto.buscar_categoria(categoria)
        if nova_categoria_id is None:
            Produto.criar_categoria(categoria)
            nova_categoria_id = Produto.buscar_categoria(categoria)

        novo_produto = Produto(nome=nome, preco=preco, qtd_estoque=quantidade, categoria_id=nova_categoria_id)
        novo_produto.insert_produto()

        CTkMessagebox(title="Sucesso", message="Produto cadastrado com sucesso!")
        self.limpar_formulario()
    
    def limpar_formulario(self):
        self.entry_nome.delete(0, ctk.END)
        self.entry_preco.delete(0, ctk.END)
        self.entry_quantidade.delete(0, ctk.END)
        self.combo_categoria.set("Selecione a Categoria")

    def voltar_btn(self):
        self.destroy()
        from page1 import Page1
        app = Page1()
        app.mainloop()

    def adicionar_categoria(self):
        self.destroy()
        from pagenewcategory import PageNewCategory
        app = PageNewCategory()
        app.mainloop()