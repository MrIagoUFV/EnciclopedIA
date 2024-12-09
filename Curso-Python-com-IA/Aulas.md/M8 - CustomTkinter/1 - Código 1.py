import customtkinter as ctk

# Configurações da janela
ctk.set_appearance_mode("light")  # Temas: dark, light, system
ctk.set_default_color_theme("blue")  # Temas: blue, dark-blue, green

# Criar janela principal
janela = ctk.CTk()
janela.title("Módulo 8 - CustomTkinter")

# Obtém as dimensões da tela
largura_tela = janela.winfo_screenwidth()
altura_tela = janela.winfo_screenheight()

# Define o tamanho da janela igual ao tamanho da tela
janela.geometry(f"{largura_tela}x{altura_tela}+0+0")

# Força a janela a permanecer maximizada
janela.state('zoomed')  # Para Windows
# janela.attributes('-zoomed', True)  # Para Linux
janela.resizable(False, False)  # Impede redimensionamento da janela

# Iniciar o loop da aplicação
janela.mainloop()

# Mudar o tema
# Mudar a cor do tema
# Mudar o tamanho da janela
# Mudar a posição da janela
# Manter a janela sempre ativa
# Mudar o título da janela
