from customtkinter import *



class Page1(CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        
        
        self.label = CTkLabel(self, text="This is page 1")
        self.label.pack(pady=20)

        self.button = CTkButton(self, text="Go to page 2", command=self.go_to_page2)
        self.button.pack(pady=10)

    def go_to_page2(self):
        self.master.show_page("page2")
