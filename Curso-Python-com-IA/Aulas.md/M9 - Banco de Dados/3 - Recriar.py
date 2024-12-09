import customtkinter as ctk
import tkinter as tk
from datetime import datetime
import sqlite3

def adapt_datetime(dt):
    return dt.isoformat()

def convert_datetime(s):
    try:
        return datetime.fromisoformat(s)
    except (ValueError, TypeError):
        return None

# Registrar adaptadores
sqlite3.register_adapter(datetime, adapt_datetime)
sqlite3.register_converter("timestamp", convert_datetime)

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        
        # Configurações da janela principal
        self.title("Clone Google Keep")
        self.geometry(f"{self.winfo_screenwidth()}x{self.winfo_screenheight()}+0+0")
        self.state("zoomed")
        ctk.set_appearance_mode("dark")
        
        # Força a janela a permanecer em (0,0) e maximizada
        self.bind("<Configure>", self.manter_configuracao)
        
        # Configurar o grid
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        
        # Criar frames principais
        self.frame_lateral = ctk.CTkFrame(self, corner_radius=0)
        self.frame_lateral.grid(row=0, column=0, sticky="nsew")
        
        self.frame_principal = ctk.CTkFrame(self, corner_radius=0)
        self.frame_principal.grid(row=0, column=1, sticky="nsew")
        
        # Configurar frame principal
        self.frame_principal.grid_rowconfigure(1, weight=1)
        self.frame_principal.grid_columnconfigure(0, weight=1)
        
        # Frame de entrada
        self.frame_entrada = ctk.CTkFrame(self.frame_principal)
        self.frame_entrada.grid(row=0, column=0, sticky="ew", padx=20, pady=10)
        
        # Entrada de texto
        self.entrada = ctk.CTkEntry(
            self.frame_entrada, 
            placeholder_text="Criar uma nota...",
            height=40,
            font=("Roboto", 14)
        )
        self.entrada.pack(fill="x", padx=10, pady=10)
        self.entrada.bind("<Return>", self.adicionar_tarefa)
        
        # Frame scrollable para lista de tarefas
        self.frame_tarefas = ctk.CTkScrollableFrame(
            self.frame_principal,
            label_text="As notas adicionadas são exibidas aqui"
        )
        self.frame_tarefas.grid(row=1, column=0, sticky="nsew", padx=20, pady=10)
        
        # Botões do frame lateral
        self.btn_todas = ctk.CTkButton(
            self.frame_lateral,
            text="Todas as Notas",
            command=self.mostrar_todas
        )
        self.btn_todas.pack(padx=20, pady=10)
        
        self.btn_arquivadas = ctk.CTkButton(
            self.frame_lateral,
            text="Arquivadas",
            command=self.mostrar_arquivadas
        )
        self.btn_arquivadas.pack(padx=20, pady=10)
        
        self.btn_lixeira = ctk.CTkButton(
            self.frame_lateral,
            text="Lixeira",
            command=self.mostrar_lixeira
        )
        self.btn_lixeira.pack(padx=20, pady=10)
        
        # Inicializar banco de dados
        self.inicializar_db()
        
        # Carregar tarefas iniciais
        self.carregar_tarefas()
        
    def inicializar_db(self):
        self.conn = sqlite3.connect('tarefas.db')
        self.cursor = self.conn.cursor()
        
        # Criar tabela de tarefas se não existir
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS tarefas (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                texto TEXT NOT NULL,
                concluida BOOLEAN DEFAULT 0,
                arquivada BOOLEAN DEFAULT 0,
                deletada BOOLEAN DEFAULT 0,
                data_delecao TEXT
            )
        ''')
        self.conn.commit()
        
    def adicionar_tarefa(self, event=None):
        texto = self.entrada.get().strip()
        if texto:
            self.cursor.execute(
                'INSERT INTO tarefas (texto) VALUES (?)',
                (texto,)
            )
            self.conn.commit()
            self.entrada.delete(0, tk.END)
            self.carregar_tarefas()
            
    def carregar_tarefas(self, modo="todas"):
        # Limpar frame de tarefas
        for widget in self.frame_tarefas.winfo_children():
            widget.destroy()
            
        # Definir query baseada no modo
        if modo == "todas":
            query = 'SELECT id, texto, concluida FROM tarefas WHERE deletada = 0 AND arquivada = 0'
        elif modo == "arquivadas":
            query = 'SELECT id, texto, concluida FROM tarefas WHERE arquivada = 1 AND deletada = 0'
        elif modo == "lixeira":
            query = 'SELECT id, texto, concluida, data_delecao FROM tarefas WHERE deletada = 1'
            
        self.cursor.execute(query)
        resultados = self.cursor.fetchall()
        
        for resultado in resultados:
            if modo == "lixeira":
                id, texto, concluida, data_delecao = resultado
                self.criar_widget_tarefa_lixeira(id, texto, data_delecao)
            elif modo == "arquivadas":
                id, texto, concluida = resultado
                self.criar_widget_tarefa_arquivada(id, texto, concluida)
            else:
                id, texto, concluida = resultado
                self.criar_widget_tarefa(id, texto, concluida)
    
    def criar_widget_tarefa(self, id, texto, concluida):
        frame = ctk.CTkFrame(self.frame_tarefas)
        frame.pack(fill="x", padx=5, pady=2)
        
        # Checkbox
        var = tk.BooleanVar(value=concluida)
        check = ctk.CTkCheckBox(
            frame, 
            text="",
            variable=var,
            command=lambda: self.marcar_concluida(id, var.get())
        )
        check.pack(side="left", padx=5)
        
        # Texto
        texto_label = f"✓ {texto}" if concluida else texto
        label = ctk.CTkLabel(
            frame,
            text=texto_label,
            font=("Roboto", 12),
            text_color="gray" if concluida else "white"
        )
        label.pack(side="left", padx=5, fill="x", expand=True)
        
        # Botões
        btn_arquivar = ctk.CTkButton(
            frame,
            text="📁",
            width=30,
            command=lambda: self.arquivar_tarefa(id)
        )
        btn_arquivar.pack(side="right", padx=2)
        
        btn_deletar = ctk.CTkButton(
            frame,
            text="🗑️",
            width=30,
            command=lambda: self.deletar_tarefa(id)
        )
        btn_deletar.pack(side="right", padx=2)
    
    def criar_widget_tarefa_lixeira(self, id, texto, data_delecao):
        frame = ctk.CTkFrame(self.frame_tarefas)
        frame.pack(fill="x", padx=5, pady=2)
        
        # Converter a string ISO para datetime
        try:
            if data_delecao:
                data_obj = datetime.fromisoformat(data_delecao)
                data_formatada = data_obj.strftime("%d/%m/%Y %H:%M")
            else:
                data_formatada = "Data desconhecida"
        except (ValueError, TypeError):
            data_formatada = "Data desconhecida"
        
        label = ctk.CTkLabel(
            frame,
            text=f"{texto}\nDeletado em: {data_formatada}",
            font=("Roboto", 12)
        )
        label.pack(side="left", padx=5, fill="x", expand=True)
        
        # Botão restaurar
        btn_restaurar = ctk.CTkButton(
            frame,
            text="↩️",
            width=30,
            command=lambda: self.restaurar_tarefa(id)
        )
        btn_restaurar.pack(side="right", padx=2)
    
    def restaurar_tarefa(self, id):
        self.cursor.execute(
            'UPDATE tarefas SET deletada = 0, data_delecao = NULL WHERE id = ?',
            (id,)
        )
        self.conn.commit()
        self.mostrar_lixeira()
    
    def marcar_concluida(self, id, concluida):
        self.cursor.execute(
            'UPDATE tarefas SET concluida = ? WHERE id = ?',
            (concluida, id)
        )
        self.conn.commit()
        self.carregar_tarefas()
        
    def arquivar_tarefa(self, id):
        self.cursor.execute(
            'UPDATE tarefas SET arquivada = 1 WHERE id = ?',
            (id,)
        )
        self.conn.commit()
        self.carregar_tarefas()
        
    def deletar_tarefa(self, id):
        # Modificar para salvar a data como string ISO
        data_atual = datetime.now().isoformat()
        self.cursor.execute(
            'UPDATE tarefas SET deletada = 1, data_delecao = ? WHERE id = ?',
            (data_atual, id)
        )
        self.conn.commit()
        self.carregar_tarefas()
        
    def mostrar_todas(self):
        self.carregar_tarefas(modo="todas")
        
    def mostrar_arquivadas(self):
        self.carregar_tarefas(modo="arquivadas")
        
    def mostrar_lixeira(self):
        # Primeiro limpar tarefas antigas (mais de 3 dias)
        self.cursor.execute('''
            DELETE FROM tarefas 
            WHERE deletada = 1 
            AND julianday('now') - julianday(data_delecao) > 3
        ''')
        self.conn.commit()
        
        self.carregar_tarefas(modo="lixeira")
    
    def manter_configuracao(self, event=None):
        """Mantém a janela na posição (0,0) e maximizada"""
        if self.winfo_x() != 0 or self.winfo_y() != 0:
            self.geometry(f"+0+0")
        if self.state() != "zoomed":
            self.state("zoomed")
    
    def criar_widget_tarefa_arquivada(self, id, texto, concluida):
        frame = ctk.CTkFrame(self.frame_tarefas)
        frame.pack(fill="x", padx=5, pady=2)
        
        # Checkbox
        var = tk.BooleanVar(value=concluida)
        check = ctk.CTkCheckBox(
            frame, 
            text="",
            variable=var,
            command=lambda: self.marcar_concluida_arquivada(id, var.get())
        )
        check.pack(side="left", padx=5)
        
        # Texto
        texto_label = f"✓ {texto}" if concluida else texto
        label = ctk.CTkLabel(
            frame,
            text=texto_label,
            font=("Roboto", 12),
            text_color="gray" if concluida else "white"
        )
        label.pack(side="left", padx=5, fill="x", expand=True)
        
        # Botões
        btn_restaurar = ctk.CTkButton(
            frame,
            text="↩️",
            width=30,
            command=lambda: self.desarquivar_tarefa(id)
        )
        btn_restaurar.pack(side="right", padx=2)
        
        btn_deletar = ctk.CTkButton(
            frame,
            text="🗑️",
            width=30,
            command=lambda: self.deletar_tarefa(id)
        )
        btn_deletar.pack(side="right", padx=2)
    
    def marcar_concluida_arquivada(self, id, concluida):
        """Marca uma tarefa arquivada como concluída sem mudar de aba"""
        self.cursor.execute(
            'UPDATE tarefas SET concluida = ? WHERE id = ?',
            (concluida, id)
        )
        self.conn.commit()
        self.carregar_tarefas(modo="arquivadas")
    
    def desarquivar_tarefa(self, id):
        """Restaura uma tarefa arquivada para a lista principal"""
        self.cursor.execute(
            'UPDATE tarefas SET arquivada = 0 WHERE id = ?',
            (id,)
        )
        self.conn.commit()
        self.carregar_tarefas(modo="arquivadas")

if __name__ == "__main__":
    app = App()
    app.mainloop()
