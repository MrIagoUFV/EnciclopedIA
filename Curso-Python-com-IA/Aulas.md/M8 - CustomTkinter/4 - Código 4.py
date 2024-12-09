import customtkinter as ctk
from tkinter import messagebox

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        
        # Configuração da janela
        self.title("Demonstração de Eventos")
        self.geometry("400x500")
        
        # Variáveis
        self.switch_var = ctk.StringVar(value="off")
        
        # Widgets
        self.criar_widgets()
        
    def criar_widgets(self):
        # Frame principal
        frame = ctk.CTkFrame(self)
        frame.pack(padx=20, pady=20, fill="both", expand=True)
        
        # Entrada de texto
        self.entrada = ctk.CTkEntry(frame, placeholder_text="Digite algo aqui...")
        self.entrada.pack(padx=10, pady=10, fill="x")
        self.entrada.bind("<Return>", self.processar_entrada)  # Evento ao pressionar Enter
        
        # Botão
        btn = ctk.CTkButton(frame, text="Clique-me!", command=self.botao_clicado)
        btn.pack(padx=10, pady=10)
        
        # Switch
        switch = ctk.CTkSwitch(frame, text="Ativar/Desativar", 
                             variable=self.switch_var,
                             onvalue="on", offvalue="off",
                             command=self.switch_alterado)
        switch.pack(padx=10, pady=10)
        
        # Slider
        self.slider = ctk.CTkSlider(frame, from_=0, to=100,
                                  command=self.slider_alterado)
        self.slider.pack(padx=10, pady=10)
        
        # Label para mostrar valor do slider
        self.valor_label = ctk.CTkLabel(frame, text="Valor: 0")
        self.valor_label.pack(padx=10, pady=5)
        
        # Caixa de seleção
        self.combo = ctk.CTkComboBox(frame, 
                                   values=["Opção 1", "Opção 2", "Opção 3"],
                                   command=self.combo_selecionado)
        self.combo.pack(padx=10, pady=10)
        
        # Área de texto
        self.texto = ctk.CTkTextbox(frame, height=100)
        self.texto.pack(padx=10, pady=10, fill="x")
        
    def processar_entrada(self, event):
        texto = self.entrada.get()
        if texto:
            self.texto.insert("end", f"Entrada: {texto}\n")
            self.entrada.delete(0, "end")
    
    def botao_clicado(self):
        messagebox.showinfo("Evento", "Botão foi clicado!")
        
    def switch_alterado(self):
        estado = self.switch_var.get()
        self.texto.insert("end", f"Switch alterado para: {estado}\n")
        
    def slider_alterado(self, valor):
        self.valor_label.configure(text=f"Valor: {int(valor)}")
        
    def combo_selecionado(self, escolha):
        self.texto.insert("end", f"Selecionado: {escolha}\n")

if __name__ == "__main__":
    app = App()
    app.mainloop()
