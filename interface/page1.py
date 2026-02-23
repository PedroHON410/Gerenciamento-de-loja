import customtkinter as ctk
from PIL import Image
import os

class Page1(ctk.CTk):
    def __init__(self, master=None):
        super().__init__(master)
        
        # --- CONFIGURAÇÃO DA JANELA ---
        self.title("Sistema de Controle de Loja")
        self.geometry("1000x700")
        
        # --- LÓGICA PARA ENCONTRAR A IMAGEM ---
        # Obtém o caminho da pasta onde este arquivo .py está salvo
        caminho_diretorio = os.path.dirname(os.path.abspath(__file__))
        # Junta o caminho da pasta com o nome do arquivo da imagem
        caminho_imagem = os.path.join(caminho_diretorio, "logo.png")
        
        # --- INTERFACE ---
        try:
            # Carregando a imagem com o caminho completo (absoluto)
            self.image = ctk.CTkImage(Image.open(caminho_imagem), size=(200, 200))
            self.image_label = ctk.CTkLabel(self, image=self.image, text="")
        except FileNotFoundError:
            print(f"Erro: O arquivo 'logo.png' não foi encontrado em: {caminho_imagem}")
            self.image_label = ctk.CTkLabel(self, text="[Imagem não encontrada]")

        self.label = ctk.CTkLabel(
            self, 
            text="Bem-vindo ao Sistema de Controle de Loja!", 
            font=ctk.CTkFont(size=20, weight="bold")
        )
        self.label.pack(pady=20)
        
        self.image_label.pack(pady=20)

        # Botões
        self.button1 = ctk.CTkButton(
            self, 
            text="Gerenciar Produtos",
            corner_radius=35, 
            fg_color="#740E6D",
            hover_color="#4158D0",
            command=self.gerenciar_produtos
        )
        self.button1.pack(pady=10) # Usei pack para manter consistência, ou use place como preferir

        self.button2 = ctk.CTkButton(
            self, 
            text="Gerenciar Vendas",
            corner_radius=35, 
            fg_color="#740E6D",
            hover_color="#4158D0"
        )
        self.button2.pack(pady=10)

        self.button3 = ctk.CTkButton(
            self, 
            text="Gerenciar Clientes",
            corner_radius=35, 
            fg_color="#740E6D",
            hover_color="#4158D0"
        )
        self.button3.pack(pady=10)

    def gerenciar_produtos(self):
        print("Gerenciando Produtos...")

if __name__ == "__main__":
    app = Page1()
    app.mainloop()