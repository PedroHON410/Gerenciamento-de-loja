import customtkinter as ctk
from PIL import Image
class Page1(ctk.CTk):
    def __init__(self, master):
        super().__init__(master)
        self.title("Sistema de Controle de Loja")
        self.geometry("1000x700")
        img1 = Image.open("images/logo.png")
        self.image=ctk.CTkImage(img1, size=(200, 200))
        self.label = ctk.CTkLabel(self, text="Bem-vindo ao Sistema de Controle de Loja!", font=ctk.CTkFont(size=20, weight="bold"))
        self.label.pack(pady=20)
        #self.label_image = ctk.CTkLabel(self, image=image, text="")
        #self.label_image.pack(pady=20)
        self.button1 = ctk.CTkButton(self, text="Gerenciar Produtos",corner_radius=35, fg_color="#C850C0",hover_color="#4158D0",
                                    command=self.gerenciar_produtos)
        self.button1.place(relx=0.5, rely=0.5, anchor="center")
        self.button2 = ctk.CTkButton(self, text="Gerenciar Vendas",corner_radius=35, fg_color="#C850C0",hover_color="#4158D0")# command=self.gerenciar_vendas)
        self.button2.pack(pady=10)
        self.button3 = ctk.CTkButton(self, text="Gerenciar Clientes",corner_radius=35, fg_color="#C850C0",hover_color="#4158D0")#, command=self.gerenciar_clientes)
        self.button3.pack(pady=10)
    def gerenciar_produtos(self):
        print("Gerenciando Produtos...")
if __name__ == "__main__":
    app = Page1(None)
    app.mainloop()