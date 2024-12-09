import customtkinter as ctk

# Configurações da janela
janela = ctk.CTk()
janela.title("Widgets Básicos CustomTkinter")
janela.geometry("600x400")
janela.configure(fg_color="#EBEBEB")

# Configuração do tema
ctk.set_appearance_mode("light")
ctk.set_default_color_theme("green")

# Frame principal
frame = ctk.CTkFrame(janela, fg_color="#EBEBEB")
frame.pack(pady=20, padx=20, fill="both", expand=True)

# Label
label = ctk.CTkLabel(
    frame,
    text="Texto Personalizado",
    font=("Arial", 20, "bold"),
    text_color="#FF1493",
    anchor="w",
    wraplength=200,
    justify="left",
    corner_radius=10,
    padx=10,
    pady=5
)
label.pack(pady=10)

# Entry (campo de entrada)
entrada = ctk.CTkEntry(
    frame,
    placeholder_text="Digite algo aqui...",
    width=300,
    height=40,
    border_width=2,
    corner_radius=10
)
entrada.pack(pady=10)

# Button
botao = ctk.CTkButton(
    frame,
    text="Clique Aqui",
    width=200,
    height=40,
    corner_radius=8,
    hover_color="#FF1493",
    command=lambda: print("Botão clicado!")
)
botao.pack(pady=10)

# Checkbox
checkbox = ctk.CTkCheckBox(
    frame,
    text="Marque esta opção",
    checkbox_width=24,
    checkbox_height=24,
    corner_radius=4
)
checkbox.pack(pady=10)

# Switch
switch = ctk.CTkSwitch(
    frame,
    text="Ativar/Desativar",
    switch_width=60,
    switch_height=30,
)
switch.pack(pady=10)

# Slider
slider = ctk.CTkSlider(
    frame,
    from_=0,
    to=100,
    width=300,
)
slider.pack(pady=10)
slider.set(50)  # Valor inicial

# Inicia o loop principal
janela.mainloop()