import customtkinter as ctk

class Calculadora:
    def __init__(self):
        # Configuração da janela principal
        self.janela = ctk.CTk()
        self.janela.title('Calculadora')
        self.janela.geometry('300x400')
        self.janela.resizable(False, False)

        # Variáveis
        self.expressao = ''
        self.resultado = '0'
        
        # Criação dos frames
        self.criar_frames()
        # Criação do display
        self.criar_display()
        # Criação dos botões
        self.criar_botoes()
        
        self.janela.mainloop()

    def criar_frames(self):
        # Frame mais externo (borda branca)
        self.frame_externo = ctk.CTkFrame(self.janela, fg_color='white')
        self.frame_externo.pack(expand=True, fill='both', padx=10, pady=10)
        
        # Frame principal verde
        self.frame_principal = ctk.CTkFrame(self.frame_externo, fg_color='#2fa572')
        self.frame_principal.pack(expand=True, fill='both', padx=3, pady=3)
        
        # Frame do título
        self.frame_titulo = ctk.CTkFrame(self.frame_principal, fg_color='white', height=40)
        self.frame_titulo.pack(fill='x', padx=2, pady=(2,0))
        self.frame_titulo.pack_propagate(False)
        
        # Label do título
        self.label_titulo = ctk.CTkLabel(
            self.frame_titulo,
            text="CALCULADORA",
            font=('Arial', 16, 'bold'),
            text_color='black'
        )
        self.label_titulo.pack(expand=True)
        
        # Frame do display
        self.frame_display = ctk.CTkFrame(self.frame_principal, fg_color='white')
        self.frame_display.pack(fill='x', padx=2, pady=2)
        
        # Frame dos botões
        self.frame_botoes = ctk.CTkFrame(self.frame_principal, fg_color='white')
        self.frame_botoes.pack(expand=True, fill='both', padx=2, pady=2)

    def criar_display(self):
        # Label do display
        self.label_resultado = ctk.CTkLabel(
            self.frame_display,
            text=self.resultado,
            font=('Arial', 40, 'bold'),
            anchor='e',
            justify='right'
        )
        self.label_resultado.pack(expand=True, fill='both', padx=10, pady=10)

    def criar_botoes(self):
        # Configuração do grid
        self.frame_botoes.rowconfigure((0,1,2,3), weight=1, uniform='a')
        self.frame_botoes.columnconfigure((0,1,2,3), weight=1, uniform='a')

        # Botões numéricos e operadores
        botoes = [
            ('7', 0, 0), ('8', 0, 1), ('9', 0, 2), ('/', 0, 3),
            ('4', 1, 0), ('5', 1, 1), ('6', 1, 2), ('*', 1, 3),
            ('1', 2, 0), ('2', 2, 1), ('3', 2, 2), ('-', 2, 3),
            ('0', 3, 0, 2), ('C', 3, 2), ('+', 3, 3)  # 0 ocupa 2 colunas
        ]
        
        for botao in botoes:
            texto = botao[0]
            row = botao[1]
            col = botao[2]
            colspan = botao[3] if len(botao) > 3 else 1
            
            if texto == '=':
                bg_color = '#265073'
            elif texto in ['/', '*', '-', '+']:
                bg_color = '#F4D03F'
            elif texto == 'C':
                bg_color = '#E74C3C'
            else:
                bg_color = '#808080'
                
            btn = ctk.CTkButton(
                self.frame_botoes,
                text=texto,
                font=('Arial', 20, 'bold'),
                fg_color=bg_color,
                hover_color=self.ajustar_cor(bg_color),
                width=50,
                height=50,
                command=lambda x=texto: self.click_botao(x)
            )
            btn.grid(row=row, column=col, columnspan=colspan, padx=2, pady=2, sticky='nsew')
        
        # Botão igual em um frame separado
        frame_igual = ctk.CTkFrame(self.frame_principal, fg_color='white')
        frame_igual.pack(fill='x', padx=2, pady=2)
        
        btn_igual = ctk.CTkButton(
            frame_igual,
            text='=',
            font=('Arial', 20, 'bold'),
            fg_color='#265073',
            hover_color=self.ajustar_cor('#265073'),
            height=40,
            command=lambda: self.click_botao('=')
        )
        btn_igual.pack(fill='both', padx=2, pady=2)

    def ajustar_cor(self, cor_hex):
        # Escurece a cor para o efeito hover
        r = int(cor_hex[1:3], 16)
        g = int(cor_hex[3:5], 16)
        b = int(cor_hex[5:7], 16)
        
        fator = 0.8
        r = int(r * fator)
        g = int(g * fator)
        b = int(b * fator)
        
        return f'#{r:02x}{g:02x}{b:02x}'

    def click_botao(self, valor):
        if valor == 'C':
            self.expressao = ''
            self.resultado = '0'
        elif valor == '=':
            try:
                self.resultado = str(eval(self.expressao))
                self.expressao = self.resultado
            except:
                self.resultado = 'Erro'
                self.expressao = ''
        else:
            if self.expressao == '0':
                self.expressao = ''
            self.expressao += valor
            self.resultado = self.expressao
            
        self.atualizar_display()

    def atualizar_display(self):
        self.label_resultado.configure(text=self.resultado)

if __name__ == '__main__':
    Calculadora()
