import customtkinter as ctk
from CTkMessagebox import CTkMessagebox
from tkinter import ttk
from Venda import Venda
from PIL import Image
import os
from Produto import Produto
from Cliente import Cliente

class PageNovaVenda(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Registrar Nova Venda")
        self.geometry("900x550")
        self.cor_roxo = "#740E6D"
        
        ctk.set_appearance_mode("light")

        # Configuração do Grid Principal: Coluna 0 (Sidebar) fixa, Coluna 1 (Form) expande
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.criar_widgets()
        self.aba_vendas()
    def criar_widgets(self):
        # --- SIDEBAR ---
        self.sidebar = ctk.CTkFrame(self, width=200, corner_radius=0, fg_color=self.cor_roxo)
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
        self.container_form = ctk.CTkFrame(self, fg_color="transparent")
        self.container_form.grid(row=0, column=1, padx=40, pady=40, sticky="nsew")

        self.lbl_instrucao = ctk.CTkLabel(self.container_form, text="Registrar Nova Venda", font=("Arial", 18, "bold"))
        self.lbl_instrucao.pack(pady=(0, 20), anchor="w")

        # Produto
        self.combo_produto = ctk.CTkComboBox(self.container_form, values=[pro[1] for pro in Produto.listar_produtos()], width=400, height=40)
        self.combo_produto.set("Selecione o produto")
        self.combo_produto.pack(pady=10)
        
        # Quantidade
        self.entry_quantidade = ctk.CTkEntry(self.container_form, placeholder_text="Quantidade Vendida", width=400, height=40)
        self.entry_quantidade.pack(pady=10)

        self.combo_cliente = ctk.CTkComboBox(self.container_form, values=[cli[1] for cli in Cliente.listar_clientes()], width=400, height=40)
        self.combo_cliente.set("Selecione o cliente")
        self.combo_cliente.pack(pady=10)
        

        # Botão Registrar Venda
        self.btn_registrar = ctk.CTkButton(self.container_form, text="Registrar Venda", width=200, height=40, command=self.registrar_venda)
        self.btn_registrar.pack(pady=20)

    def voltar_btn(self):
        self.destroy()
        from page1 import Page1
        app = Page1()
        app.mainloop()

    def criar_card(self, parent, titulo, valor):
        card = ctk.CTkFrame(parent, width=200, height=100, corner_radius=10, fg_color="#f0f0f0")
        card.pack(side="left", padx=10, pady=10)
        
        label_titulo = ctk.CTkLabel(card, text=titulo, font=("Arial", 12), text_color="gray")
        label_titulo.pack(pady=(10, 5))
        
        label_valor = ctk.CTkLabel(card, text=str(valor), font=("Arial", 20, "bold"), text_color=self.cor_roxo)
        label_valor.pack(pady=(0, 10))
        
        return card
    
    def registrar_venda(self):
        nome_produto = self.entry_produto.get()
        quantidade_vendida = self.entry_quantidade.get()

        if not nome_produto or not quantidade_vendida:
            CTkMessagebox(title="Erro", message="Por favor, preencha todos os campos.", icon="error")
            return
        
        try:
            quantidade_vendida = int(quantidade_vendida)
        except ValueError:
            CTkMessagebox(title="Erro", message="Quantidade deve ser um número inteiro.", icon="error")
            return
        
        produto = Produto.buscar_por_nome(nome_produto)
        if not produto:
            CTkMessagebox(title="Erro", message="Produto não encontrado.", icon="error")
            return
        
        if quantidade_vendida > produto[3]:  # Verifica se há estoque suficiente
            CTkMessagebox(title="Erro", message="Quantidade vendida excede o estoque disponível.", icon="error")
            return
        
        venda = Venda(produto_id=produto[0], quantidade=quantidade_vendida)
        venda.registrar()
        
        CTkMessagebox(title="Sucesso", message="Venda registrada com sucesso!", icon="check")
        
        # Limpa os campos após registrar a venda
        self.entry_produto.delete(0, ctk.END)
        self.entry_quantidade.delete(0, ctk.END)
    
    def venda_cliente(self):
        nome_cliente = self.entry_cliente.get()
        if not nome_cliente:
            CTkMessagebox(title="Erro", message="Por favor, selecione um cliente.", icon="error")
            return
        
        cliente = Cliente.buscar_por_nome(nome_cliente)
        if not cliente:
            CTkMessagebox(title="Erro", message="Cliente não encontrado.", icon="error")
            return
        else:
            cliente = Cliente.compra(cliente[1])  # Atualiza a quantidade de compras do cliente
        

        return cliente[0]  # Retorna o ID do cliente para associar à venda