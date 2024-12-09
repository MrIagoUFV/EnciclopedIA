# Importação das bibliotecas necessárias
import sqlite3                                    # Biblioteca para trabalhar com SQLite
from datetime import datetime                     # Biblioteca para manipular datas

# Configuração inicial do banco de dados
conexao = sqlite3.connect('biblioteca.db')        # Cria/conecta ao arquivo do banco
cursor = conexao.cursor()                        # Cria um cursor para executar comandos

# Criação da tabela de livros
cursor.execute('''
    CREATE TABLE IF NOT EXISTS livros (           
        id INTEGER PRIMARY KEY,                   
        titulo TEXT NOT NULL,                     
        autor TEXT,                              
        quantidade INTEGER DEFAULT 1              
    )
''')

# Criação da tabela de empréstimos
cursor.execute('''
    CREATE TABLE IF NOT EXISTS emprestimos (      
        id INTEGER PRIMARY KEY,                   
        livro_id INTEGER,                        
        data_emprestimo TEXT,                    
        data_devolucao TEXT,                     
        FOREIGN KEY (livro_id) REFERENCES livros (id)  
    )
''')

# Função para adicionar novo livro
def adicionar_livro(titulo, autor, quantidade=1):     # Função com parâmetro opcional
    try:
        cursor.execute('''
            INSERT INTO livros (titulo, autor, quantidade)  
            VALUES (?, ?, ?)                               
        ''', (titulo, autor, quantidade))                  # Valores a serem inseridos
        conexao.commit()                                   # Confirma a operação
        print("Livro adicionado com sucesso!")            # Mensagem de sucesso
    except sqlite3.Error as erro:                         # Captura erros do SQLite
        print(f"Erro ao adicionar livro: {erro}")         # Exibe mensagem de erro

# Função para realizar empréstimo
def emprestar_livro(livro_id):                           # Função para empréstimo
    try:
        # Consulta quantidade disponível
        cursor.execute('SELECT quantidade FROM livros WHERE id = ?', (livro_id,))  # Verifica estoque
        quantidade = cursor.fetchone()[0]                 # Obtém resultado da consulta
        
        if quantidade > 0:                                # Verifica se há livros disponíveis
            # Atualiza o estoque
            cursor.execute('''
                UPDATE livros 
                SET quantidade = quantidade - 1           
                WHERE id = ?                             
            ''', (livro_id,))
            
            # Registra o empréstimo
            data_atual = datetime.now().strftime('%Y-%m-%d')  # Formata data atual
            cursor.execute('''
                INSERT INTO emprestimos (livro_id, data_emprestimo)  
                VALUES (?, ?)                                        
            ''', (livro_id, data_atual))
            
            conexao.commit()                             # Confirma as alterações
            print("Empréstimo realizado com sucesso!")   # Mensagem de sucesso
        else:
            print("Livro não disponível!")               # Mensagem de indisponibilidade
            
    except sqlite3.Error as erro:                        # Captura erros do SQLite
        conexao.rollback()                               # Desfaz alterações em caso de erro
        print(f"Erro na operação: {erro}")               # Exibe mensagem de erro

# Exemplos de uso do sistema
adicionar_livro("Dom Casmurro", "Machado de Assis", 3)  # Adiciona livro com 3 cópias
emprestar_livro(1)                                       # Empresta o livro ID 1

# Consulta de empréstimos ativos
cursor.execute('''
    SELECT l.titulo, e.data_emprestimo              
    FROM emprestimos e                              
    JOIN livros l ON e.livro_id = l.id             
''')

print("\nEmpréstimos ativos:")                          # Título da listagem
for registro in cursor.fetchall():                      # Percorre resultados
    print(f"Livro: {registro[0]} - Data: {registro[1]}")  # Exibe cada empréstimo

conexao.close()                                         # Encerra conexão com o banco

