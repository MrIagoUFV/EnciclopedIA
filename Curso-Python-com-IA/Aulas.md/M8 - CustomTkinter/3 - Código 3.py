import customtkinter as ctk

# Configurações iniciais
ctk.set_appearance_mode("light")
ctk.set_default_color_theme("blue")

# Criar janela principal
janela = ctk.CTk()
janela.title("Exemplo Grid Layout")
janela.geometry("400x300")

# Configurar o peso das colunas para centralização
janela.grid_columnconfigure(1, weight=1)  # Coluna do meio expande
janela.grid_columnconfigure((0, 2), weight=0)  # Colunas laterais não expandem

# Título
label_titulo = ctk.CTkLabel(janela, text="Sejam Bem-Vindos!", 
                           font=("Arial", 20, "bold"), 
                           text_color="#0000FF")
label_titulo.grid(row=0, column=0, columnspan=3, pady=20)

# Entrada de nome
entrada_nome = ctk.CTkEntry(janela, placeholder_text="Digite seu nome",
                           border_color="#E0E0E0")
entrada_nome.grid(row=1, column=0, padx=10, pady=10, sticky="ew")

# Botão de enviar
botao_enviar = ctk.CTkButton(janela, text="botão de enviar", 
                            fg_color="#00AA00", 
                            hover_color="#008800", 
                            text_color="white")
botao_enviar.grid(row=1, column=2, padx=10, pady=10)

# Label da idade
label_idade = ctk.CTkLabel(janela, text="Qual a sua idade?", 
                          font=("Arial", 16))
label_idade.grid(row=2, column=0, columnspan=3, pady=10)

# Slider para idade
slider_idade = ctk.CTkSlider(janela, from_=0, to=100,
                            progress_color="#00AA00")
slider_idade.grid(row=3, column=0, columnspan=3, padx=20, pady=10, sticky="ew")

# Iniciar o loop principal
janela.mainloop()
