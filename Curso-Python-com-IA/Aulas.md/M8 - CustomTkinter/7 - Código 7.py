import customtkinter as ctk
from PIL import Image
import os

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        
        # Configurações da janela
        self.title("Interface Responsiva com Tabs")
        self.geometry("800x600")
        
        # Grid layout principal (1x1)
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        
        # Criar TabView
        self.tabview = ctk.CTkTabview(self)
        self.tabview.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")
        
        # Adicionar tabs
        self.tabview.add("Perfil")
        self.tabview.add("Lista de Itens")
        self.tabview.add("Configurações")
        
        # Configurar grid das tabs
        for tab in ["Perfil", "Lista de Itens", "Configurações"]:
            self.tabview.tab(tab).grid_columnconfigure(0, weight=1)
        
        # Conteúdo da Tab Perfil
        self.criar_perfil()
        
        # Conteúdo da Tab Lista de Itens
        self.criar_lista_itens()
        
        # Conteúdo da Tab Configurações
        self.criar_configuracoes()
        
        # Bind do evento de redimensionamento
        self.bind("<Configure>", self.on_resize)
        
    def criar_perfil(self):
        # Frame rolável para o perfil
        perfil_frame = ctk.CTkScrollableFrame(self.tabview.tab("Perfil"))
        perfil_frame.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")
        
        # Adicionar widgets ao perfil
        ctk.CTkLabel(perfil_frame, text="Informações do Perfil").grid(row=0, column=0, pady=10)
        ctk.CTkEntry(perfil_frame, placeholder_text="Nome").grid(row=1, column=0, pady=5)
        ctk.CTkEntry(perfil_frame, placeholder_text="Email").grid(row=2, column=0, pady=5)
        ctk.CTkEntry(perfil_frame, placeholder_text="Telefone").grid(row=3, column=0, pady=5)
        
    def criar_lista_itens(self):
        # Frame rolável para a lista de itens
        lista_frame = ctk.CTkScrollableFrame(self.tabview.tab("Lista de Itens"))
        lista_frame.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")
        
        # Adicionar vários itens para demonstrar a rolagem
        for i in range(20):
            item_frame = ctk.CTkFrame(lista_frame)
            item_frame.grid(row=i, column=0, pady=5, sticky="ew")
            
            ctk.CTkLabel(item_frame, text=f"Item {i+1}").grid(row=0, column=0, padx=10)
            ctk.CTkButton(item_frame, text="Detalhes").grid(row=0, column=1, padx=10)
            
    def criar_configuracoes(self):
        # Frame rolável para configurações
        config_frame = ctk.CTkScrollableFrame(self.tabview.tab("Configurações"))
        config_frame.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")
        
        # Adicionar opções de configuração
        temas = ["System", "Light", "Dark"]
        ctk.CTkLabel(config_frame, text="Tema:").grid(row=0, column=0, pady=10)
        ctk.CTkOptionMenu(config_frame, values=temas).grid(row=0, column=1, pady=10)
        
        ctk.CTkLabel(config_frame, text="Notificações:").grid(row=1, column=0, pady=10)
        ctk.CTkSwitch(config_frame, text="Ativar").grid(row=1, column=1, pady=10)
        
    def on_resize(self, event):
        # Ajustar layout baseado no tamanho da janela
        width = self.winfo_width()
        
        if width < 600:  # Tela pequena
            self.tabview.configure(width=width-40)
        else:  # Tela grande
            self.tabview.configure(width=width-40)

if __name__ == "__main__":
    app = App()
    app.mainloop()
