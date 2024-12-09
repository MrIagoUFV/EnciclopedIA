# Importação das bibliotecas necessárias para manipulação de arquivos
import json         # Biblioteca para trabalhar com arquivos JSON
import csv          # Biblioteca para trabalhar com arquivos CSV
import os          # Biblioteca para operações do sistema operacional

# Função principal que gerencia toda a biblioteca
def gerenciar_biblioteca():
    """
    Sistema simples de gerenciamento de biblioteca pessoal
    usando diferentes tipos de arquivos para diferentes propósitos
    """
    
    # Definição das configurações iniciais
    CONFIG_FILE = "config.json"                                           # Nome do arquivo de configuração
    if not os.path.exists(CONFIG_FILE):                                  # Verifica se o arquivo existe
        config = {                                                       # Dicionário com configurações padrão
            "nome_biblioteca": "Minha Biblioteca",                       # Nome padrão da biblioteca
            "categorias": ["Ficção", "Não-Ficção", "Técnico"],         # Categorias disponíveis
            "versao": "1.0"                                            # Versão do sistema
        }
        with open(CONFIG_FILE, "w", encoding="utf-8") as f:            # Abre arquivo para escrita
            json.dump(config, f, indent=4, ensure_ascii=False)         # Salva configurações formatadas

    # Função interna para registrar logs
    def registrar_log(mensagem):                                       # Função que registra atividades
        with open("biblioteca_log.txt", "a", encoding="utf-8") as f:   # Abre arquivo de log em modo append
            f.write(f"{mensagem}\n")                                   # Escreve a mensagem com quebra de linha

    # Função interna para adicionar novos livros
    def adicionar_livro(titulo, autor, categoria):                     # Função que adiciona um novo livro
        novo_livro = [titulo, autor, categoria]                        # Lista com dados do livro
        with open("livros.csv", "a", newline="", encoding="utf-8") as f:  # Abre CSV em modo append
            writer = csv.writer(f)                                     # Cria objeto escritor CSV
            writer.writerow(novo_livro)                               # Escreve nova linha no CSV
        registrar_log(f"Novo livro adicionado: {titulo}")            # Registra a adição no log

    # Criação inicial do arquivo CSV se não existir
    if not os.path.exists("livros.csv"):                              # Verifica se arquivo CSV existe
        with open("livros.csv", "w", newline="", encoding="utf-8") as f:  # Cria novo arquivo CSV
            writer = csv.writer(f)                                     # Cria objeto escritor CSV
            writer.writerow(["Título", "Autor", "Categoria"])         # Escreve cabeçalho do CSV

    # Loop principal do programa
    while True:                                                        # Loop infinito do menu
        print("\n=== Gerenciador de Biblioteca ===")                   # Título do menu
        print("1. Adicionar livro")                                   # Opção 1
        print("2. Listar livros")                                     # Opção 2
        print("3. Ver configurações")                                 # Opção 3
        print("4. Sair")                                             # Opção 4
        
        opcao = input("\nEscolha uma opção: ")                        # Recebe escolha do usuário

        if opcao == "1":                                              # Se escolheu adicionar livro
            titulo = input("Título: ")                                # Recebe título do livro
            autor = input("Autor: ")                                  # Recebe autor do livro
            categoria = input("Categoria: ")                          # Recebe categoria do livro
            adicionar_livro(titulo, autor, categoria)                # Chama função de adicionar

        elif opcao == "2":                                            # Se escolheu listar livros
            with open("livros.csv", "r", encoding="utf-8") as f:      # Abre CSV para leitura
                reader = csv.reader(f)                                # Cria objeto leitor CSV
                next(reader)                                          # Pula linha do cabeçalho
                for livro in reader:                                  # Para cada livro no CSV
                    print(f"\nTítulo: {livro[0]}")                   # Mostra título
                    print(f"Autor: {livro[1]}")                      # Mostra autor
                    print(f"Categoria: {livro[2]}")                  # Mostra categoria
                    print("-" * 30)                                  # Linha separadora

        elif opcao == "3":                                            # Se escolheu ver configurações
            with open(CONFIG_FILE, "r", encoding="utf-8") as f:       # Abre arquivo JSON
                config = json.load(f)                                 # Carrega configurações
                print("\nConfigurações:")                            # Título da seção
                for chave, valor in config.items():                  # Para cada configuração
                    print(f"{chave}: {valor}")                       # Mostra chave e valor

        elif opcao == "4":                                            # Se escolheu sair
            registrar_log("Programa encerrado")                      # Registra encerramento
            break                                                    # Encerra o programa

# Ponto de entrada do programa
if __name__ == "__main__":                                           # Se executado diretamente
    gerenciar_biblioteca()                                          # Inicia o programa