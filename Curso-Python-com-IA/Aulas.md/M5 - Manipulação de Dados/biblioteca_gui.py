import customtkinter as ctk
import json
import os
from datetime import datetime
from typing import Callable, Optional

# Configuração do tema
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

# Arquivos utilizados
CONFIG_FILE = "config.json"
LIVROS_FILE = "livros.json" 
EMPRESTIMOS_FILE = "emprestimos.json"
LOG_FILE = "log.txt"

class BibliotecaApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        
        # Configuração da janela principal
        self.title("Sistema de Biblioteca")
        self.geometry("800x600")
        
        # Carrega os dados
        self.config = self.carregar_config()
        self.livros = self.carregar_livros()
        self.emprestimos = self.carregar_emprestimos()
        
        # Cria o layout principal
        self.criar_layout()
        
    def criar_layout(self):
        # Frame do menu lateral
        self.menu_frame = ctk.CTkFrame(self, width=200)
        self.menu_frame.pack(side="left", fill="y", padx=10, pady=10)
        
        # Título do menu
        ctk.CTkLabel(self.menu_frame, text="MENU", font=("Arial", 20, "bold")).pack(pady=10)
        
        # Botões do menu
        botoes = [
            ("Adicionar Livro", self.mostrar_adicionar_livro),
            ("Listar Livros", self.mostrar_listar_livros),
            ("Emprestar Livro", self.mostrar_emprestar_livro),
            ("Devolver Livro", self.mostrar_devolver_livro),
            ("Descartar Livro", self.mostrar_descartar_livro),
            ("Ver Empréstimos", self.mostrar_emprestimos),
            ("Ver Histórico", self.mostrar_historico),
            ("Editar Livro", self.mostrar_editar_livro)
        ]
        
        for texto, comando in botoes:
            ctk.CTkButton(
                self.menu_frame, 
                text=texto, 
                command=comando,
                width=180
            ).pack(pady=5)
        
        # Frame principal de conteúdo
        self.conteudo_frame = ctk.CTkFrame(self)
        self.conteudo_frame.pack(side="right", fill="both", expand=True, padx=10, pady=10)
        
        # Mensagem inicial
        self.mostrar_mensagem_boas_vindas()
    
    def limpar_conteudo(self):
        """Limpa o frame de conteúdo"""
        for widget in self.conteudo_frame.winfo_children():
            widget.destroy()
    
    def mostrar_mensagem_boas_vindas(self):
        """Mostra mensagem inicial"""
        self.limpar_conteudo()
        ctk.CTkLabel(
            self.conteudo_frame,
            text="Bem-vindo ao Sistema de Biblioteca",
            font=("Arial", 24, "bold")
        ).pack(expand=True)
    
    def mostrar_mensagem(self, mensagem: str, tipo: str = "info"):
        """Mostra uma mensagem temporária"""
        cores = {
            "erro": "red",
            "sucesso": "green",
            "info": "gray"
        }
        
        msg_label = ctk.CTkLabel(
            self.conteudo_frame,
            text=mensagem,
            text_color=cores.get(tipo, "gray")
        )
        msg_label.pack(pady=10)
        
        # Remove a mensagem após 3 segundos
        self.after(3000, msg_label.destroy)
    
    def criar_scrollable_frame(self) -> tuple[ctk.CTkScrollableFrame, ctk.CTkFrame]:
        """Cria um frame scrollable com cabeçalho fixo"""
        # Frame para o cabeçalho
        header_frame = ctk.CTkFrame(self.conteudo_frame)
        header_frame.pack(fill="x", padx=10, pady=(10,0))
        
        # Frame scrollable para o conteúdo
        scroll_frame = ctk.CTkScrollableFrame(self.conteudo_frame)
        scroll_frame.pack(fill="both", expand=True, padx=10, pady=10)
        
        return scroll_frame, header_frame
    
    # Funções auxiliares de dados
    def carregar_config(self):
        """Carrega configurações do arquivo"""
        if not os.path.exists(CONFIG_FILE):
            config = {"categorias": ["Ficção", "Não-Ficção", "Técnico"]}
            self.salvar_config(config)
            return config
        with open(CONFIG_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    
    def salvar_config(self, config):
        with open(CONFIG_FILE, "w", encoding="utf-8") as f:
            json.dump(config, f, indent=4, ensure_ascii=False)
    
    def carregar_livros(self):
        if not os.path.exists(LIVROS_FILE):
            return {}
        with open(LIVROS_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    
    def salvar_livros(self):
        with open(LIVROS_FILE, "w", encoding="utf-8") as f:
            json.dump(self.livros, f, indent=4, ensure_ascii=False)
    
    def carregar_emprestimos(self):
        if not os.path.exists(EMPRESTIMOS_FILE):
            return {}
        with open(EMPRESTIMOS_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    
    def salvar_emprestimos(self):
        with open(EMPRESTIMOS_FILE, "w", encoding="utf-8") as f:
            json.dump(self.emprestimos, f, indent=4, ensure_ascii=False)
    
    def registrar_log(self, mensagem):
        data = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        with open(LOG_FILE, "a", encoding="utf-8") as f:
            f.write(f"[{data}] {mensagem}\n")
    
    # Funções das telas
    def mostrar_adicionar_livro(self):
        """Mostra tela de adicionar livro"""
        self.limpar_conteudo()
        
        # Título
        ctk.CTkLabel(
            self.conteudo_frame,
            text="Adicionar Novo Livro",
            font=("Arial", 20, "bold")
        ).pack(pady=20)
        
        # Frame para o formulário
        form_frame = ctk.CTkFrame(self.conteudo_frame)
        form_frame.pack(padx=20, pady=20)
        
        # Campos do formulário
        campos = {}
        
        # Título
        ctk.CTkLabel(form_frame, text="Título:").pack(pady=5)
        campos["titulo"] = ctk.CTkEntry(form_frame, width=300)
        campos["titulo"].pack(pady=5)
        
        # Categoria
        ctk.CTkLabel(form_frame, text="Categoria:").pack(pady=5)
        campos["categoria"] = ctk.CTkComboBox(
            form_frame, 
            values=self.config["categorias"],
            width=300
        )
        campos["categoria"].pack(pady=5)
        
        # Autor
        ctk.CTkLabel(form_frame, text="Autor:").pack(pady=5)
        campos["autor"] = ctk.CTkEntry(form_frame, width=300)
        campos["autor"].pack(pady=5)
        
        # Cópias
        ctk.CTkLabel(form_frame, text="Número de Cópias:").pack(pady=5)
        campos["copias"] = ctk.CTkEntry(form_frame, width=300)
        campos["copias"].pack(pady=5)
        
        def adicionar():
            titulo = campos["titulo"].get().strip()
            categoria = campos["categoria"].get()
            autor = campos["autor"].get().strip()
            copias = campos["copias"].get().strip()
            
            # Validações
            if not all([titulo, categoria, autor, copias]):
                self.mostrar_mensagem("Todos os campos são obrigatórios!", "erro")
                return
            
            try:
                copias = int(copias)
                if copias <= 0:
                    raise ValueError()
            except ValueError:
                self.mostrar_mensagem("Número de cópias inválido!", "erro")
                return
            
            if titulo in self.livros:
                self.mostrar_mensagem("Já existe um livro com este título!", "erro")
                return
            
            # Adiciona o livro
            self.livros[titulo] = {
                "categoria": categoria,
                "autor": autor,
                "copias_totais": copias,
                "copias_disponiveis": copias
            }
            
            self.salvar_livros()
            self.registrar_log(f"Livro '{titulo}' adicionado com {copias} cópias")
            self.mostrar_mensagem("Livro adicionado com sucesso!", "sucesso")
            
            # Limpa os campos
            for campo in campos.values():
                if isinstance(campo, ctk.CTkEntry):  # Se for um campo de entrada normal
                    campo.delete(0, "end")
                elif isinstance(campo, ctk.CTkComboBox):  # Se for um ComboBox
                    campo.set(campo._values[0] if campo._values else "")  # Volta para o primeiro valor
        
        # Botão de adicionar
        ctk.CTkButton(
            form_frame,
            text="Adicionar Livro",
            command=adicionar,
            width=300
        ).pack(pady=20)
    
    def mostrar_listar_livros(self):
        """Mostra tela de listagem de livros"""
        self.limpar_conteudo()
        
        # Título
        ctk.CTkLabel(
            self.conteudo_frame,
            text="Livros Cadastrados",
            font=("Arial", 20, "bold")
        ).pack(pady=20)
        
        if not self.livros:
            ctk.CTkLabel(
                self.conteudo_frame,
                text="Nenhum livro cadastrado!",
                font=("Arial", 16)
            ).pack(expand=True)
            return
        
        # Cria frame scrollable
        scroll_frame, header_frame = self.criar_scrollable_frame()
        
        # Cabeçalho
        colunas = ["Título", "Autor", "Categoria", "Disponíveis/Total"]
        for i, col in enumerate(colunas):
            ctk.CTkLabel(
                header_frame,
                text=col,
                font=("Arial", 12, "bold")
            ).grid(row=0, column=i, padx=10, pady=5)
        
        # Lista de livros
        for i, (titulo, info) in enumerate(self.livros.items(), 1):
            ctk.CTkLabel(scroll_frame, text=titulo).grid(row=i, column=0, padx=10, pady=5)
            ctk.CTkLabel(scroll_frame, text=info["autor"]).grid(row=i, column=1, padx=10, pady=5)
            ctk.CTkLabel(scroll_frame, text=info["categoria"]).grid(row=i, column=2, padx=10, pady=5)
            ctk.CTkLabel(
                scroll_frame, 
                text=f"{info['copias_disponiveis']}/{info['copias_totais']}"
            ).grid(row=i, column=3, padx=10, pady=5)
    
    def mostrar_emprestar_livro(self):
        """Mostra tela de empréstimo de livro"""
        self.limpar_conteudo()
        
        # Título
        ctk.CTkLabel(
            self.conteudo_frame,
            text="Emprestar Livro",
            font=("Arial", 20, "bold")
        ).pack(pady=20)
        
        # Filtra livros disponíveis
        livros_disponiveis = {titulo: info for titulo, info in self.livros.items() 
                             if info["copias_disponiveis"] > 0}
        
        if not livros_disponiveis:
            ctk.CTkLabel(
                self.conteudo_frame,
                text="Não há livros disponíveis para empréstimo!",
                font=("Arial", 16)
            ).pack(expand=True)
            return
        
        # Cria frame scrollable
        scroll_frame, header_frame = self.criar_scrollable_frame()
        
        # Cabeçalho
        colunas = ["Selecionar", "Título", "Autor", "Categoria", "Disponíveis"]
        for i, col in enumerate(colunas):
            ctk.CTkLabel(
                header_frame,
                text=col,
                font=("Arial", 12, "bold")
            ).grid(row=0, column=i, padx=10, pady=5)
        
        # Variável para armazenar a seleção
        selecao = ctk.StringVar()
        
        # Lista de livros com radio buttons
        for i, (titulo, info) in enumerate(livros_disponiveis.items(), 1):
            radio = ctk.CTkRadioButton(
                scroll_frame, 
                text="",
                variable=selecao,
                value=titulo
            )
            radio.grid(row=i, column=0, padx=10, pady=5)
            
            ctk.CTkLabel(scroll_frame, text=titulo).grid(row=i, column=1, padx=10, pady=5)
            ctk.CTkLabel(scroll_frame, text=info["autor"]).grid(row=i, column=2, padx=10, pady=5)
            ctk.CTkLabel(scroll_frame, text=info["categoria"]).grid(row=i, column=3, padx=10, pady=5)
            ctk.CTkLabel(scroll_frame, text=str(info["copias_disponiveis"])).grid(row=i, column=4, padx=10, pady=5)
        
        def emprestar():
            titulo = selecao.get()
            if not titulo:
                self.mostrar_mensagem("Selecione um livro!", "erro")
                return
            
            # Atualiza o número de cópias disponíveis
            self.livros[titulo]["copias_disponiveis"] -= 1
            
            # Cria lista de empréstimos para o livro se não existir
            if titulo not in self.emprestimos:
                self.emprestimos[titulo] = []
            
            # Adiciona novo empréstimo com ID único
            emprestimo_id = len(self.emprestimos[titulo]) + 1
            self.emprestimos[titulo].append({
                "id": emprestimo_id,
                "data_emprestimo": datetime.now().strftime("%d/%m/%Y %H:%M:%S"),
                "status": "emprestado"
            })
            
            self.salvar_livros()
            self.salvar_emprestimos()
            self.registrar_log(f"Livro '{titulo}' emprestado (ID: {emprestimo_id})")
            self.mostrar_mensagem(f"Livro emprestado com sucesso! ID: {emprestimo_id}", "sucesso")
            
            # Atualiza a tela
            self.mostrar_emprestar_livro()
        
        # Botão de emprestar
        ctk.CTkButton(
            self.conteudo_frame,
            text="Emprestar Livro Selecionado",
            command=emprestar,
            width=300
        ).pack(pady=20)
    
    def mostrar_devolver_livro(self):
        """Mostra tela de devolução de livro"""
        self.limpar_conteudo()
        
        # Título
        ctk.CTkLabel(
            self.conteudo_frame,
            text="Devolver Livro",
            font=("Arial", 20, "bold")
        ).pack(pady=20)
        
        # Lista apenas livros com empréstimos ativos
        livros_emprestados = {titulo: info for titulo, info in self.livros.items() 
                             if titulo in self.emprestimos and 
                             any(emp["status"] == "emprestado" for emp in self.emprestimos[titulo])}
        
        if not livros_emprestados:
            ctk.CTkLabel(
                self.conteudo_frame,
                text="Não há livros para devolver!",
                font=("Arial", 16)
            ).pack(expand=True)
            return
        
        # Frame para seleção do livro
        livro_frame = ctk.CTkFrame(self.conteudo_frame)
        livro_frame.pack(fill="x", padx=20, pady=20)
        
        ctk.CTkLabel(livro_frame, text="Selecione o livro:").pack(pady=5)
        
        # ComboBox para selecionar o livro
        livro_selecionado = ctk.StringVar()
        livro_combo = ctk.CTkComboBox(
            livro_frame,
            values=list(livros_emprestados.keys()),
            variable=livro_selecionado,
            width=300
        )
        livro_combo.pack(pady=5)
        
        # Frame para mostrar empréstimos do livro selecionado
        emprestimos_frame = ctk.CTkFrame(self.conteudo_frame)
        emprestimos_frame.pack(fill="both", expand=True, padx=20, pady=20)
        
        def atualizar_emprestimos(*args):
            # Limpa o frame de empréstimos
            for widget in emprestimos_frame.winfo_children():
                widget.destroy()
            
            titulo = livro_selecionado.get()
            if not titulo:
                return
            
            # Mostra apenas empréstimos ativos
            emprestimos_ativos = [emp for emp in self.emprestimos[titulo] 
                                if emp["status"] == "emprestado"]
            
            if not emprestimos_ativos:
                ctk.CTkLabel(
                    emprestimos_frame,
                    text="Não há empréstimos ativos para este livro!"
                ).pack(expand=True)
                return
            
            # Cabeçalho
            ctk.CTkLabel(
                emprestimos_frame,
                text="Empréstimos Ativos",
                font=("Arial", 16, "bold")
            ).pack(pady=10)
            
            # Lista de empréstimos com radio buttons
            selecao = ctk.IntVar()
            for emp in emprestimos_ativos:
                radio = ctk.CTkRadioButton(
                    emprestimos_frame,
                    text=f"ID: {emp['id']} - Data: {emp['data_emprestimo']}",
                    variable=selecao,
                    value=emp['id']
                )
                radio.pack(pady=5)
            
            def devolver():
                id_devolver = selecao.get()
                if not id_devolver:
                    self.mostrar_mensagem("Selecione um empréstimo!", "erro")
                    return
                
                # Remove o empréstimo da lista
                self.emprestimos[titulo] = [emp for emp in self.emprestimos[titulo] 
                                          if emp["id"] != id_devolver]
                
                # Se não houver mais empréstimos, remove a entrada
                if not self.emprestimos[titulo]:
                    self.emprestimos.pop(titulo)
                
                # Atualiza o número de cópias disponíveis
                self.livros[titulo]["copias_disponiveis"] += 1
                
                self.salvar_livros()
                self.salvar_emprestimos()
                self.registrar_log(f"Livro '{titulo}' devolvido (ID: {id_devolver})")
                self.mostrar_mensagem("Livro devolvido com sucesso!", "sucesso")
                
                # Atualiza a tela
                self.mostrar_devolver_livro()
            
            # Botão de devolver
            ctk.CTkButton(
                emprestimos_frame,
                text="Devolver Livro Selecionado",
                command=devolver,
                width=300
            ).pack(pady=20)
        
        # Atualiza a lista de empréstimos quando um livro é selecionado
        livro_selecionado.trace_add("write", atualizar_emprestimos)
        
        # Mostra empréstimos do primeiro livro
        if livros_emprestados:
            livro_combo.set(list(livros_emprestados.keys())[0])
    
    def mostrar_emprestimos(self):
        """Mostra tela de listagem de empréstimos ativos"""
        self.limpar_conteudo()
        
        # Título
        ctk.CTkLabel(
            self.conteudo_frame,
            text="Empréstimos Ativos",
            font=("Arial", 20, "bold")
        ).pack(pady=20)
        
        # Filtra apenas empréstimos ativos
        emprestimos_ativos = {}
        for titulo, lista in self.emprestimos.items():
            ativos = [emp for emp in lista if emp["status"] == "emprestado"]
            if ativos:
                emprestimos_ativos[titulo] = ativos
        
        if not emprestimos_ativos:
            ctk.CTkLabel(
                self.conteudo_frame,
                text="Não há empréstimos ativos no momento!",
                font=("Arial", 16)
            ).pack(expand=True)
            return
        
        # Cria frame scrollable
        scroll_frame, header_frame = self.criar_scrollable_frame()
        
        # Cabeçalho
        colunas = ["Título", "ID", "Data do Empréstimo", "Cópias Disponíveis"]
        for i, col in enumerate(colunas):
            ctk.CTkLabel(
                header_frame,
                text=col,
                font=("Arial", 12, "bold")
            ).grid(row=0, column=i, padx=10, pady=5)
        
        # Lista de empréstimos
        row = 1
        for titulo, emprestimos in emprestimos_ativos.items():
            info_livro = self.livros[titulo]
            for emp in emprestimos:
                ctk.CTkLabel(scroll_frame, text=titulo).grid(row=row, column=0, padx=10, pady=5)
                ctk.CTkLabel(scroll_frame, text=str(emp["id"])).grid(row=row, column=1, padx=10, pady=5)
                ctk.CTkLabel(scroll_frame, text=emp["data_emprestimo"]).grid(row=row, column=2, padx=10, pady=5)
                ctk.CTkLabel(
                    scroll_frame, 
                    text=f"{info_livro['copias_disponiveis']}/{info_livro['copias_totais']}"
                ).grid(row=row, column=3, padx=10, pady=5)
                row += 1
    
    def mostrar_historico(self):
        """Mostra tela de histórico de operações"""
        self.limpar_conteudo()
        
        # Título
        ctk.CTkLabel(
            self.conteudo_frame,
            text="Histórico de Operações",
            font=("Arial", 20, "bold")
        ).pack(pady=20)
        
        if not os.path.exists(LOG_FILE):
            ctk.CTkLabel(
                self.conteudo_frame,
                text="Nenhum histórico disponível!",
                font=("Arial", 16)
            ).pack(expand=True)
            return
        
        # Frame para o histórico
        historico_frame = ctk.CTkTextbox(
            self.conteudo_frame,
            width=700,
            height=400
        )
        historico_frame.pack(padx=20, pady=20, fill="both", expand=True)
        
        # Carrega e mostra o histórico
        with open(LOG_FILE, "r", encoding="utf-8") as f:
            historico_frame.insert("1.0", f.read())
        
        # Torna o texto não editável
        historico_frame.configure(state="disabled")
    
    def mostrar_editar_livro(self):
        """Mostra tela de edição de livro"""
        self.limpar_conteudo()
        
        # Título
        ctk.CTkLabel(
            self.conteudo_frame,
            text="Editar Livro",
            font=("Arial", 20, "bold")
        ).pack(pady=20)
        
        if not self.livros:
            ctk.CTkLabel(
                self.conteudo_frame,
                text="Não há livros para editar!",
                font=("Arial", 16)
            ).pack(expand=True)
            return
        
        # Frame para seleção do livro
        selecao_frame = ctk.CTkFrame(self.conteudo_frame)
        selecao_frame.pack(fill="x", padx=20, pady=20)
        
        ctk.CTkLabel(selecao_frame, text="Selecione o livro:").pack(pady=5)
        
        # ComboBox para selecionar o livro
        livro_selecionado = ctk.StringVar()
        livro_combo = ctk.CTkComboBox(
            selecao_frame,
            values=list(self.livros.keys()),
            variable=livro_selecionado,
            width=300
        )
        livro_combo.pack(pady=5)
        
        # Frame para o formulário de edição (inicialmente oculto)
        form_frame = ctk.CTkFrame(self.conteudo_frame)
        
        def mostrar_formulario():
            titulo_atual = livro_selecionado.get()
            if not titulo_atual:
                self.mostrar_mensagem("Selecione um livro!", "erro")
                return
            
            info = self.livros[titulo_atual]
            
            # Limpa o frame de conteúdo mantendo apenas a seleção
            for widget in self.conteudo_frame.winfo_children():
                if widget != selecao_frame:
                    widget.destroy()
            
            # Recria o frame do formulário
            form_frame = ctk.CTkFrame(self.conteudo_frame)
            form_frame.pack(padx=20, pady=20)
            
            campos = {}
            
            # Título
            ctk.CTkLabel(form_frame, text="Título:").pack(pady=5)
            campos["titulo"] = ctk.CTkEntry(form_frame, width=300)
            campos["titulo"].insert(0, titulo_atual)
            campos["titulo"].pack(pady=5)
            
            # Categoria
            ctk.CTkLabel(form_frame, text="Categoria:").pack(pady=5)
            campos["categoria"] = ctk.CTkComboBox(
                form_frame, 
                values=self.config["categorias"],
                width=300
            )
            campos["categoria"].set(info["categoria"])
            campos["categoria"].pack(pady=5)
            
            # Autor
            ctk.CTkLabel(form_frame, text="Autor:").pack(pady=5)
            campos["autor"] = ctk.CTkEntry(form_frame, width=300)
            campos["autor"].insert(0, info["autor"])
            campos["autor"].pack(pady=5)
            
            # Cópias totais
            ctk.CTkLabel(form_frame, text="Número total de cópias:").pack(pady=5)
            campos["copias_totais"] = ctk.CTkEntry(form_frame, width=300)
            campos["copias_totais"].insert(0, str(info["copias_totais"]))
            campos["copias_totais"].pack(pady=5)
            
            # Cópias disponíveis
            ctk.CTkLabel(form_frame, text="Número de cópias disponíveis:").pack(pady=5)
            campos["copias_disponiveis"] = ctk.CTkEntry(form_frame, width=300)
            campos["copias_disponiveis"].insert(0, str(info["copias_disponiveis"]))
            campos["copias_disponiveis"].pack(pady=5)
            
            def salvar_alteracoes():
                novo_titulo = campos["titulo"].get().strip()
                categoria = campos["categoria"].get()
                autor = campos["autor"].get().strip()
                
                try:
                    copias_totais = int(campos["copias_totais"].get())
                    copias_disponiveis = int(campos["copias_disponiveis"].get())
                    
                    if copias_totais <= 0 or copias_disponiveis < 0:
                        raise ValueError("Números inválidos")
                    
                    if copias_disponiveis > copias_totais:
                        self.mostrar_mensagem("Cópias disponíveis não pode ser maior que o total!", "erro")
                        return
                    
                    # Verifica empréstimos ativos
                    if titulo_atual in self.emprestimos:
                        emprestimos_ativos = sum(1 for emp in self.emprestimos[titulo_atual] 
                                               if emp["status"] == "emprestado")
                        if (copias_totais - copias_disponiveis) < emprestimos_ativos:
                            self.mostrar_mensagem(
                                f"Não é possível reduzir para {copias_totais} cópias! "
                                f"Existem {emprestimos_ativos} empréstimos ativos.",
                                "erro"
                            )
                            return
                    
                except ValueError:
                    self.mostrar_mensagem("Números de cópias inválidos!", "erro")
                    return
                
                # Validações adicionais
                if not all([novo_titulo, categoria, autor]):
                    self.mostrar_mensagem("Todos os campos são obrigatórios!", "erro")
                    return
                
                if novo_titulo != titulo_atual and novo_titulo in self.livros:
                    self.mostrar_mensagem("Já existe um livro com este título!", "erro")
                    return
                
                # Atualiza o livro
                novo_livro = {
                    "categoria": categoria,
                    "autor": autor,
                    "copias_totais": copias_totais,
                    "copias_disponiveis": copias_disponiveis
                }
                
                # Se mudou o título, remove o antigo e adiciona o novo
                if novo_titulo != titulo_atual:
                    self.livros.pop(titulo_atual)
                    if titulo_atual in self.emprestimos:
                        self.emprestimos[novo_titulo] = self.emprestimos.pop(titulo_atual)
                
                self.livros[novo_titulo] = novo_livro
                
                self.salvar_livros()
                self.salvar_emprestimos()
                self.registrar_log(f"Livro '{titulo_atual}' editado para '{novo_titulo}'")
                self.mostrar_mensagem("Livro atualizado com sucesso!", "sucesso")
                
                # Volta para a tela de edição
                self.mostrar_editar_livro()
            
            # Botão de salvar
            ctk.CTkButton(
                form_frame,
                text="Salvar Alterações",
                command=salvar_alteracoes,
                width=300
            ).pack(pady=20)
        
        # Botão de editar
        ctk.CTkButton(
            selecao_frame,
            text="Editar Livro Selecionado",
            command=mostrar_formulario,
            width=300
        ).pack(pady=20)
        
        # Mostra o primeiro livro na lista
        if self.livros:
            livro_combo.set(list(self.livros.keys())[0])
    
    def mostrar_descartar_livro(self):
        """Mostra tela de descarte de livro"""
        self.limpar_conteudo()
        
        # Título
        ctk.CTkLabel(
            self.conteudo_frame,
            text="Descartar Livro",
            font=("Arial", 20, "bold")
        ).pack(pady=20)
        
        # Filtra apenas livros com cópias disponíveis
        livros_disponiveis = {titulo: info for titulo, info in self.livros.items() 
                             if info["copias_disponiveis"] > 0}
        
        if not livros_disponiveis:
            ctk.CTkLabel(
                self.conteudo_frame,
                text="Não há livros disponíveis para descarte!",
                font=("Arial", 16)
            ).pack(expand=True)
            return
        
        # Frame para seleção do livro
        livro_frame = ctk.CTkFrame(self.conteudo_frame)
        livro_frame.pack(fill="x", padx=20, pady=20)
        
        ctk.CTkLabel(livro_frame, text="Selecione o livro:").pack(pady=5)
        
        # ComboBox para selecionar o livro
        livro_selecionado = ctk.StringVar()
        livro_combo = ctk.CTkComboBox(
            livro_frame,
            values=list(livros_disponiveis.keys()),
            variable=livro_selecionado,
            width=300
        )
        livro_combo.pack(pady=5)
        
        # Frame para opções de descarte
        opcoes_frame = ctk.CTkFrame(self.conteudo_frame)
        opcoes_frame.pack(fill="x", padx=20, pady=20)
        
        def atualizar_opcoes(*args):
            # Limpa o frame de opções
            for widget in opcoes_frame.winfo_children():
                widget.destroy()
            
            titulo = livro_selecionado.get()
            if not titulo:
                return
            
            info = self.livros[titulo]
            
            # Mostra informações do livro
            ctk.CTkLabel(
                opcoes_frame,
                text=f"Cópias totais: {info['copias_totais']}",
                font=("Arial", 12)
            ).pack(pady=5)
            ctk.CTkLabel(
                opcoes_frame,
                text=f"Cópias disponíveis: {info['copias_disponiveis']}",
                font=("Arial", 12)
            ).pack(pady=5)
            
            # Opções de descarte
            opcao = ctk.StringVar(value="parcial")
            
            # Frame para as opções
            radio_frame = ctk.CTkFrame(opcoes_frame)
            radio_frame.pack(pady=10)
            
            ctk.CTkRadioButton(
                radio_frame,
                text="Descartar todas as cópias",
                variable=opcao,
                value="total"
            ).pack(side="left", padx=10)
            
            ctk.CTkRadioButton(
                radio_frame,
                text="Descartar quantidade específica",
                variable=opcao,
                value="parcial"
            ).pack(side="left", padx=10)
            
            # Frame para quantidade específica
            qtd_frame = ctk.CTkFrame(opcoes_frame)
            qtd_frame.pack(pady=10)
            
            ctk.CTkLabel(qtd_frame, text="Quantidade:").pack(side="left", padx=5)
            qtd_entry = ctk.CTkEntry(qtd_frame, width=100)
            qtd_entry.pack(side="left", padx=5)
            
            def descartar():
                if opcao.get() == "total":
                    # Verifica se há empréstimos ativos
                    if titulo in self.emprestimos:
                        emprestimos_ativos = sum(1 for emp in self.emprestimos[titulo] 
                                               if emp["status"] == "emprestado")
                        if emprestimos_ativos > 0:
                            self.mostrar_mensagem(
                                f"Não é possível descartar todas as cópias! "
                                f"Existem {emprestimos_ativos} empréstimos ativos.",
                                "erro"
                            )
                            return
                    
                    # Remove o livro e seus empréstimos
                    self.livros.pop(titulo)
                    if titulo in self.emprestimos:
                        self.emprestimos.pop(titulo)
                    
                    self.salvar_livros()
                    self.salvar_emprestimos()
                    self.registrar_log(f"Livro '{titulo}' completamente descartado")
                    self.mostrar_mensagem("Livro completamente descartado!", "sucesso")
                    
                else:  # descarte parcial
                    try:
                        qtd = int(qtd_entry.get())
                        if qtd <= 0:
                            raise ValueError("Quantidade deve ser maior que zero")
                        
                        if qtd > info["copias_disponiveis"]:
                            self.mostrar_mensagem(
                                f"Só é possível descartar até {info['copias_disponiveis']} cópias!",
                                "erro"
                            )
                            return
                        
                        # Atualiza as quantidades
                        info["copias_totais"] -= qtd
                        info["copias_disponiveis"] -= qtd
                        
                        # Se não sobrou nenhuma cópia, remove o livro
                        if info["copias_totais"] == 0:
                            self.livros.pop(titulo)
                            if titulo in self.emprestimos:
                                self.emprestimos.pop(titulo)
                            self.registrar_log(f"Livro '{titulo}' completamente descartado após remover últimas {qtd} cópias")
                            self.mostrar_mensagem("Livro completamente descartado!", "sucesso")
                        else:
                            self.registrar_log(f"{qtd} cópias do livro '{titulo}' foram descartadas")
                            self.mostrar_mensagem(f"{qtd} cópias descartadas com sucesso!", "sucesso")
                        
                        self.salvar_livros()
                        self.salvar_emprestimos()
                        
                    except ValueError as e:
                        self.mostrar_mensagem("Quantidade inválida!", "erro")
                        return
                
                # Atualiza a tela
                self.mostrar_descartar_livro()
            
            # Botão de descartar
            ctk.CTkButton(
                opcoes_frame,
                text="Descartar",
                command=descartar,
                width=200
            ).pack(pady=20)
        
        # Atualiza as opções quando um livro é selecionado
        livro_selecionado.trace_add("write", atualizar_opcoes)
        
        # Mostra opções do primeiro livro
        if livros_disponiveis:
            livro_combo.set(list(livros_disponiveis.keys())[0])

# ... Continua com as outras funções de interface ...

if __name__ == "__main__":
    app = BibliotecaApp()
    app.mainloop() 