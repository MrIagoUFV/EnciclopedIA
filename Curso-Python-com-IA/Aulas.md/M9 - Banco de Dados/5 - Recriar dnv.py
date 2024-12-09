import customtkinter as ctk

class ModalTarefa(ctk.CTkToplevel):
    def __init__(self, parent, titulo):
        super().__init__(parent)
        
        # Configurações do modal
        self.title("Detalhes da Tarefa")
        largura = 500
        altura = 400
        pos_x = parent.winfo_x() + (parent.winfo_width() // 2) - (largura // 2)
        pos_y = parent.winfo_y() + (parent.winfo_height() // 2) - (altura // 2)
        self.geometry(f"{largura}x{altura}+{pos_x}+{pos_y}")
        
        # Configurações adicionais do modal
        self.grab_set()  # Torna a janela modal (bloqueia a janela principal)
        self.transient(parent)  # Faz o modal sempre ficar acima da janela principal
        self.resizable(False, False)  # Impede redimensionamento
        
        # Título
        self.label_titulo = ctk.CTkLabel(
            self,
            text=titulo,
            font=ctk.CTkFont(size=16, weight="bold")
        )
        self.label_titulo.pack(pady=(20, 10), padx=20)
        
        # Área de texto para descrição
        self.texto_descricao = ctk.CTkTextbox(
            self,
            width=460,
            height=300,
            font=ctk.CTkFont(size=14)
        )
        self.texto_descricao.pack(pady=10, padx=20)
        
        # Botão fechar
        self.btn_fechar = ctk.CTkButton(
            self,
            text="Fechar",
            command=self.destroy
        )
        self.btn_fechar.pack(pady=(0, 20))
        
        # Foca na área de texto após abrir
        self.after(100, lambda: self.texto_descricao.focus())
        
        # Bind da tecla Escape para fechar o modal
        self.bind("<Escape>", lambda e: self.destroy())

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        
        # Configurações da janela principal
        self.title("Clone Keep")
        self.geometry(f"{self.winfo_screenwidth()}x{self.winfo_screenheight()}+0+0")
        self.state("zoomed")
        ctk.set_appearance_mode("dark")
        
        # Criação do frame lateral
        self.frame_lateral = ctk.CTkFrame(self, width=50, corner_radius=0)
        self.frame_lateral.pack(side="left", fill="y")
        self.frame_lateral.pack_propagate(False)
        
        # Entrada de texto no topo
        self.entrada_texto = ctk.CTkEntry(
            self,
            height=40,
            corner_radius=8,
            fg_color="#1a1a1a",  # Cor de fundo escura quase preta
            text_color="white",  # Cor do texto branca
            font=ctk.CTkFont(weight="bold"),  # Fonte em negrito
            justify="left"  # Alinhamento do texto à esquerda
        )
        self.entrada_texto.pack(fill="x", padx=20, pady=(20, 0))  # Padding no topo
        
        # Frame para lista de tarefas com grid
        self.frame_tarefas = ctk.CTkFrame(self, fg_color="transparent")
        self.frame_tarefas.pack(fill="both", expand=True, padx=20, pady=20)
        
        # Configurar as colunas da grid
        self.frame_tarefas.grid_columnconfigure((0, 1, 2), weight=1, uniform="column")
        
        # Criar tarefas mockup
        self.criar_tarefa("Tarefa 1", 0, 0)
        self.criar_tarefa("Tarefa 2", 1, 0)
        self.criar_tarefa("Tarefa 3", 2, 0)
        self.criar_tarefa("Tarefa 4", 0, 1)
        self.criar_tarefa("Tarefa 5", 1, 1)
        self.criar_tarefa("Tarefa 6", 2, 1)
        self.criar_tarefa("Tarefa 7", 0, 2)
        self.criar_tarefa("Tarefa 8", 1, 2)
        self.criar_tarefa("Tarefa 9", 2, 2)
        
        # Botões com emojis
        self.btn_home = ctk.CTkButton(
            self.frame_lateral,
            text="🏠",
            width=40,
            height=40,
            corner_radius=8,
            fg_color="transparent",
            hover_color=("gray70", "gray30"),
            anchor="center"
        )
        self.btn_home.pack(pady=(10, 5))
        
        self.btn_arquivo = ctk.CTkButton(
            self.frame_lateral,
            text="📁",
            width=40,
            height=40,
            corner_radius=8,
            fg_color="transparent",
            hover_color=("gray70", "gray30"),
            anchor="center"
        )
        self.btn_arquivo.pack(pady=5)
        
        # Frame para empurrar a lixeira para baixo
        self.espacador = ctk.CTkFrame(self.frame_lateral, fg_color="transparent")
        self.espacador.pack(expand=True, fill="both")
        
        self.btn_lixeira = ctk.CTkButton(
            self.frame_lateral,
            text="🗑️",
            width=40,
            height=40,
            corner_radius=8,
            fg_color="transparent",
            hover_color=("gray70", "gray30"),
            anchor="center"
        )
        self.btn_lixeira.pack(pady=10)
        
        # Força a janela a permanecer em (0,0) e maximizada
        self.bind("<Configure>", self.manter_configuracao)
        
    def manter_configuracao(self, event):
        # Mantém a janela maximizada e na posição (0,0)
        self.geometry(f"{self.winfo_screenwidth()}x{self.winfo_screenheight()}+0+0")
        self.state("zoomed")
    
    def criar_tarefa(self, titulo, coluna, linha):
        # Frame da tarefa
        frame_tarefa = ctk.CTkFrame(
            self.frame_tarefas,
            fg_color="#2b2b2b",
            corner_radius=8,
            height=200  # Aumentado para acomodar a descrição
        )
        frame_tarefa.grid(row=linha, column=coluna, padx=5, pady=5, sticky="nsew")
        frame_tarefa.grid_propagate(False)
        
        # Container para título e descrição
        container = ctk.CTkFrame(frame_tarefa, fg_color="transparent")
        container.pack(side="left", fill="both", expand=True, padx=10, pady=10)
        
        # Checkbox e título
        frame_titulo = ctk.CTkFrame(container, fg_color="transparent")
        frame_titulo.pack(fill="x")
        
        checkbox_tarefa = ctk.CTkCheckBox(
            frame_titulo,
            text="",
            font=ctk.CTkFont(size=14),
            checkbox_width=24,
            checkbox_height=24,
            corner_radius=4
        )
        checkbox_tarefa.pack(side="left")
        
        label_titulo = ctk.CTkLabel(
            frame_titulo,
            text=titulo,
            font=ctk.CTkFont(size=14, weight="bold"),
            anchor="w"
        )
        label_titulo.pack(side="left", padx=(5, 0))
        
        # Preview da descrição
        preview_texto = ctk.CTkTextbox(
            container,
            height=120,
            font=ctk.CTkFont(size=12),
            fg_color="transparent",
            activate_scrollbars=False,
            wrap="word"
        )
        preview_texto.pack(fill="both", expand=True, pady=(5, 0))
        preview_texto.insert("1.0", "Este é um exemplo de descrição da tarefa que pode conter várias linhas de texto...")
        preview_texto.configure(state="disabled")
        
        # Frame para os botões de ação
        frame_acoes = ctk.CTkFrame(frame_tarefa, fg_color="transparent")
        frame_acoes.pack(side="right", padx=10)
        
        # Botão de arquivar
        btn_arquivar = ctk.CTkButton(
            frame_acoes,
            text="📁",
            width=30,
            height=30,
            corner_radius=8,
            fg_color="transparent",
            hover_color=("gray70", "gray30")
        )
        btn_arquivar.pack(side="top", pady=(0, 5))
        
        # Botão de excluir
        btn_excluir = ctk.CTkButton(
            frame_acoes,
            text="🗑️",
            width=30,
            height=30,
            corner_radius=8,
            fg_color="transparent",
            hover_color=("gray70", "gray30")
        )
        btn_excluir.pack(side="top")
        
        # Fazer o frame clicável
        for widget in [frame_tarefa, container, preview_texto, label_titulo]:
            widget.bind("<Button-1>", lambda e, t=titulo: self.abrir_modal(t))
    
    def abrir_modal(self, titulo):
        modal = ModalTarefa(self, titulo)
        modal.focus()

if __name__ == "__main__":
    app = App()
    app.mainloop()
