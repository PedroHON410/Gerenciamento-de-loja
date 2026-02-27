import customtkinter as ctk
from PIL import Image
import os

class Page1(ctk.CTk):
    def __init__(self, master=None):
        super().__init__(master)
        
        self.title("Sistema de Controle de Loja")
        self.geometry("800x600")
        ctk.set_appearance_mode("light")
        caminho_diretorio = os.path.dirname(os.path.abspath(__file__))
        # Junta o caminho da pasta com o nome do arquivo da imagem
        caminho_imagem = os.path.join(caminho_diretorio, "logo.png")
        
        # --- INTERFACE ---
        try:
            self.image = ctk.CTkImage(Image.open(caminho_imagem), size=(489, 589))
            self.image_label = ctk.CTkLabel(self, image=self.image, text="")
            
        except FileNotFoundError:
            print(f"Erro: O arquivo 'logo.png' não foi encontrado em: {caminho_imagem}")
            self.image_label = ctk.CTkLabel(self, text="[Imagem não encontrada]")

        self.label = ctk.CTkLabel(
            self, 
            text="Bem-vindo ao Sistema de Controle de Loja!", 
            font=ctk.CTkFont(size=20, weight="bold")
        )

        # Organizando os widgets
        self.label.pack(pady=10)
        self.image_label.pack(side="left", padx=0, pady=0)
    
        # Botões
        self.button1 = ctk.CTkButton(
             self, 
            text="Gerenciar Produtos",
            width=200,
            corner_radius=35, 
            fg_color="#740E6D",
            hover_color="#4158D0",
            command=self.gerenciar_produtos
            )
        
        self.button1.pack(side="top",pady=0 ) 
            
        self.button2 = ctk.CTkButton(
            self, 
            text="Gerenciar Vendas",
            width=200,
            corner_radius=35, 
            fg_color="#740E6D",
            hover_color="#4158D0"
            )
        self.button2.pack(side="top", pady=20)

        self.button3 = ctk.CTkButton(
            self, 
            text="Gerenciar Clientes",
            width=200,
            corner_radius=35, 
            fg_color="#740E6D",
                hover_color="#4158D0"
            )
        self.button3.pack(side="top", pady=0)

    def gerenciar_produtos(self):
        try:
            from page2 import Page2
            self.destroy()  # Fecha a janela atual
            app = Page2()  # Cria a nova janela
            app.mainloop()  # Inicia o loop da nova janela
        except ImportError as e:
            print(f"Erro ao importar Page2: {e}")
            
if __name__ == "__main__":
    app = Page1()
    app.mainloop()