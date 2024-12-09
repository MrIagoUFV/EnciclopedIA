import customtkinter as ctk
from PIL import Image
import os

# Configurações iniciais
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        
        # Configuração da janela principal
        self.title("Painel de Controle")
        self.geometry("800x600")
        
        # Criando o grid principal
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)
        
        # Frame da barra lateral
        self.sidebar_frame = ctk.CTkFrame(self, width=200, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, rowspan=4, sticky="nsew")
        self.sidebar_frame.grid_rowconfigure(4, weight=1)
        
        # Logo
        self.logo_label = ctk.CTkLabel(self.sidebar_frame, text="Painel de Controle", 
                                     font=ctk.CTkFont(size=20, weight="bold"))
        self.logo_label.grid(row=0, column=0, padx=20, pady=20)
        
        # Botões da barra lateral
        self.sidebar_button_1 = ctk.CTkButton(self.sidebar_frame, text="Dashboard",
                                            command=self.sidebar_button_event)
        self.sidebar_button_1.grid(row=1, column=0, padx=20, pady=10)
        
        self.sidebar_button_2 = ctk.CTkButton(self.sidebar_frame, text="Configurações",
                                            command=self.sidebar_button_event)
        self.sidebar_button_2.grid(row=2, column=0, padx=20, pady=10)
        
        # Frame principal
        self.main_frame = ctk.CTkFrame(self)
        self.main_frame.grid(row=0, column=1, padx=20, pady=20, sticky="nsew")
        
        # Frames superiores
        self.upper_frame = ctk.CTkFrame(self.main_frame)
        self.upper_frame.grid(row=0, column=0, padx=10, pady=10, sticky="ew")
        
        # Estatísticas
        self.stat1 = ctk.CTkLabel(self.upper_frame, text="Usuários: 150",
                                font=ctk.CTkFont(size=16))
        self.stat1.grid(row=0, column=0, padx=20, pady=20)
        
        self.stat2 = ctk.CTkLabel(self.upper_frame, text="Vendas: R$ 15.000",
                                font=ctk.CTkFont(size=16))
        self.stat2.grid(row=0, column=1, padx=20, pady=20)
        
        # Frame central
        self.center_frame = ctk.CTkFrame(self.main_frame)
        self.center_frame.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")
        
        # Área de entrada
        self.entry = ctk.CTkEntry(self.center_frame, placeholder_text="Digite algo...")
        self.entry.grid(row=0, column=0, padx=20, pady=20)
        
        self.button = ctk.CTkButton(self.center_frame, text="Enviar",
                                  command=self.button_event)
        self.button.grid(row=0, column=1, padx=20, pady=20)
        
        # Frame inferior
        self.lower_frame = ctk.CTkFrame(self.main_frame)
        self.lower_frame.grid(row=2, column=0, padx=10, pady=10, sticky="ew")
        
        # Área de status
        self.status = ctk.CTkLabel(self.lower_frame, text="Status: Online",
                                font=ctk.CTkFont(size=14))
        self.status.grid(row=0, column=0, padx=20, pady=20)
        
    def sidebar_button_event(self):
        print("Botão da barra lateral clicado")
        
    def button_event(self):
        print("Botão principal clicado")

if __name__ == "__main__":
    app = App()
    app.mainloop()
