# v5.0.0

"""
Notas para a próxima versão:
    

"""

import json
import os
from datetime import datetime

# Arquivos utilizados
CONFIG_FILE = "config.json"
LIVROS_FILE = "livros.json" 
EMPRESTIMOS_FILE = "emprestimos.json"
LOG_FILE = "log.txt"

def limpar_tela():
    """Limpa a tela do console"""
    os.system('cls' if os.name == 'nt' else 'clear')

def criar_config_padrao():
    """Cria arquivo de configuração com valores padrão"""
    config = {
        "categorias": ["Ficção", "Não-Ficção", "Técnico"]
    }
    with open(CONFIG_FILE, "w", encoding="utf-8") as f:
        json.dump(config, f, indent=4, ensure_ascii=False)
    registrar_log("Arquivo de configuração criado com valores padrão")
    return config

def carregar_config():
    """Carrega configurações do arquivo, criando se não existir"""
    if not os.path.exists(CONFIG_FILE):
        return criar_config_padrao()
    with open(CONFIG_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

def registrar_log(mensagem):
    """Registra mensagem no arquivo de log"""
    data = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(f"[{data}] {mensagem}\n")

def carregar_livros():
    """Carrega lista de livros do arquivo"""
    if not os.path.exists(LIVROS_FILE):
        return {}
    with open(LIVROS_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

def salvar_livros(livros):
    """Salva lista de livros no arquivo"""
    with open(LIVROS_FILE, "w", encoding="utf-8") as f:
        json.dump(livros, f, indent=4, ensure_ascii=False)

def carregar_emprestimos():
    """Carrega lista de empréstimos do arquivo"""
    if not os.path.exists(EMPRESTIMOS_FILE):
        return {}
    with open(EMPRESTIMOS_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

def salvar_emprestimos(emprestimos):
    """Salva lista de empréstimos no arquivo"""
    with open(EMPRESTIMOS_FILE, "w", encoding="utf-8") as f:
        json.dump(emprestimos, f, indent=4, ensure_ascii=False)

def adicionar_livro():
    """Adiciona um novo livro ao sistema"""
    config = carregar_config()
    livros = carregar_livros()
    
    titulo = input_com_cancelamento("Digite o título do livro")
    if titulo is None:
        return
        
    # Verifica se o título já existe
    if titulo in livros:
        print("\nJá existe um livro cadastrado com este título!")
        input("\nPressione Enter para continuar...")
        return
        
    print("\nCategorias disponíveis:")
    for i, cat in enumerate(config["categorias"], 1):
        print(f"{i}. {cat}")
    
    cat_idx = escolher_numero_com_cancelamento("\nEscolha o número da categoria", len(config["categorias"]))
    if cat_idx is None:
        return
    categoria = config["categorias"][cat_idx]
            
    autor = input_com_cancelamento("Digite o nome do autor")
    if autor is None:
        return
        
    while True:
        copias = input_com_cancelamento("Digite o número de cópias")
        if copias is None:
            return
        try:
            copias = int(copias)
            if copias > 0:
                break
            print("O número de cópias deve ser maior que zero!")
        except ValueError:
            print("Por favor digite um número válido!")

    livros[titulo] = {
        "categoria": categoria,
        "autor": autor,
        "copias_totais": copias,
        "copias_disponiveis": copias
    }
    
    salvar_livros(livros)
    registrar_log(f"Livro '{titulo}' adicionado com {copias} cópias")
    print("\nLivro adicionado com sucesso!")

def listar_livros():
    """Lista todos os livros cadastrados"""
    livros = carregar_livros()
    
    if not livros:
        print("\nNenhum livro cadastrado!")
        input("\nPressione Enter para voltar ao menu principal...")
        return
        
    print("\n=== LIVROS DISPONÍVEIS ===")
    for titulo, info in livros.items():
        print(f"\nTítulo: {titulo}")
        print(f"Autor: {info['autor']}")
        print(f"Categoria: {info['categoria']}")
        print(f"Cópias disponíveis: {info['copias_disponiveis']}/{info['copias_totais']}")
    
    input("\nPressione Enter para voltar ao menu principal...")

def emprestar_livro():
    """Registra o empréstimo de um livro"""
    livros = carregar_livros()
    emprestimos = carregar_emprestimos()
    
    livros_disponiveis = {titulo: info for titulo, info in livros.items() 
                         if info["copias_disponiveis"] > 0}
    
    if not livros_disponiveis:
        print("\nNão há livros disponíveis para empréstimo!")
        input("\nPressione Enter para continuar...")
        return
        
    print("\n=== LIVROS DISPONÍVEIS ===")
    for i, (titulo, info) in enumerate(livros_disponiveis.items(), 1):
        print(f"\n{i}. {titulo}")
        print(f"   Autor: {info['autor']}")
        print(f"   Categoria: {info['categoria']}")
        print(f"   Cópias disponíveis: {info['copias_disponiveis']}")
    
    escolha = escolher_numero_com_cancelamento("\nEscolha o número do livro para emprestar", len(livros_disponiveis))
    if escolha is None:
        return
        
    titulo = list(livros_disponiveis.keys())[escolha]
    
    # Atualiza o número de cópias disponíveis
    livros[titulo]["copias_disponiveis"] -= 1
    
    # Cria lista de empréstimos para o livro se não existir
    if titulo not in emprestimos:
        emprestimos[titulo] = []
    
    # Adiciona novo empréstimo com ID único baseado no número de empréstimos anteriores
    emprestimo_id = len(emprestimos[titulo]) + 1
    emprestimos[titulo].append({
        "id": emprestimo_id,
        "data_emprestimo": datetime.now().strftime("%d/%m/%Y %H:%M:%S"),
        "status": "emprestado"
    })
    
    salvar_livros(livros)
    salvar_emprestimos(emprestimos)
    registrar_log(f"Livro '{titulo}' emprestado (ID: {emprestimo_id})")
    print(f"\nLivro emprestado com sucesso! ID do empréstimo: {emprestimo_id}")

def devolver_livro():
    """Registra a devolução de um livro"""
    livros = carregar_livros()
    emprestimos = carregar_emprestimos()
    
    # Lista apenas livros com empréstimos ativos
    livros_emprestados = {titulo: info for titulo, info in livros.items() 
                         if titulo in emprestimos and 
                         any(emp["status"] == "emprestado" for emp in emprestimos[titulo])}
    
    if not livros_emprestados:
        print("\nNão há livros para devolver!")
        input("\nPressione Enter para continuar...")
        return
        
    print("\n=== LIVROS EMPRESTADOS ===")
    for i, (titulo, info) in enumerate(livros_emprestados.items(), 1):
        print(f"\n{i}. {titulo}")
        print(f"   Autor: {info['autor']}")
        emprestimos_ativos = [emp for emp in emprestimos[titulo] if emp["status"] == "emprestado"]
        print(f"   Empréstimos ativos: {len(emprestimos_ativos)}")
        for emp in emprestimos_ativos:
            print(f"      ID: {emp['id']} - Data: {emp['data_emprestimo']}")
    
    escolha = escolher_numero_com_cancelamento("\nEscolha o número do livro para devolver", len(livros_emprestados))
    if escolha is None:
        return
        
    titulo = list(livros_emprestados.keys())[escolha]
    emprestimos_ativos = [emp for emp in emprestimos[titulo] if emp["status"] == "emprestado"]
    
    # Se houver mais de um empréstimo ativo, pede o ID
    if len(emprestimos_ativos) > 1:
        print("\nEmpréstimos ativos deste livro:")
        for emp in emprestimos_ativos:
            print(f"ID: {emp['id']} - Data: {emp['data_emprestimo']}")
        
        while True:
            id_str = input_com_cancelamento("\nDigite o ID do empréstimo que deseja devolver")
            if id_str is None:
                return
            try:
                id_devolver = int(id_str)
                if any(emp["id"] == id_devolver for emp in emprestimos_ativos):
                    break
                print("ID inválido!")
            except ValueError:
                print("Por favor, digite um número válido!")
    else:
        id_devolver = emprestimos_ativos[0]["id"]
    
    # Remove o empréstimo da lista
    emprestimos[titulo] = [emp for emp in emprestimos[titulo] if emp["id"] != id_devolver]
    
    # Se não houver mais empréstimos para este livro, remove a entrada completamente
    if not emprestimos[titulo]:
        emprestimos.pop(titulo)
    
    # Atualiza o número de cópias disponíveis
    livros[titulo]["copias_disponiveis"] += 1
    
    salvar_livros(livros)
    salvar_emprestimos(emprestimos)
    registrar_log(f"Livro '{titulo}' devolvido (ID: {id_devolver})")
    print("\nLivro devolvido com sucesso!")

def descartar_livro():
    """Remove uma ou mais cópias de um livro do sistema"""
    livros = carregar_livros()
    emprestimos = carregar_emprestimos()
    
    # Filtra apenas livros com cópias disponíveis
    livros_disponiveis = {titulo: info for titulo, info in livros.items() 
                         if info["copias_disponiveis"] > 0}
    
    if not livros_disponiveis:
        print("\nNão há livros disponíveis para descarte!")
        input("\nPressione Enter para continuar...")
        return
        
    print("\n=== LIVROS DISPONÍVEIS PARA DESCARTE ===")
    for i, (titulo, info) in enumerate(livros_disponiveis.items(), 1):
        print(f"\n{i}. {titulo}")
        print(f"   Autor: {info['autor']}")
        print(f"   Cópias totais: {info['copias_totais']}")
        print(f"   Cópias disponíveis: {info['copias_disponiveis']}")
    
    escolha = escolher_numero_com_cancelamento("\nEscolha o número do livro para descartar", len(livros_disponiveis))
    if escolha is None:
        return
        
    titulo = list(livros_disponiveis.keys())[escolha]
    info_livro = livros[titulo]
    
    print("\nOpções de descarte:")
    print("1. Descartar todas as cópias")
    print("2. Descartar quantidade específica")
    
    opcao = input_com_cancelamento("\nEscolha uma opção")
    if opcao is None:
        return
        
    if opcao == "1":
        # Verifica se há empréstimos ativos
        if titulo in emprestimos:
            emprestimos_ativos = sum(1 for emp in emprestimos[titulo] 
                                   if emp["status"] == "emprestado")
            if emprestimos_ativos > 0:
                print(f"\nNão é possível descartar todas as cópias!")
                print(f"Existem {emprestimos_ativos} empréstimos ativos atualmente.")
                input("\nPressione Enter para continuar...")
                return
        
        # Remove o livro e seus empréstimos
        livros.pop(titulo)
        if titulo in emprestimos:
            emprestimos.pop(titulo)
        
        registrar_log(f"Livro '{titulo}' completamente descartado")
        print("\nLivro completamente descartado com sucesso!")
        
    elif opcao == "2":
        while True:
            qtd_str = input_com_cancelamento("\nQuantas cópias deseja descartar")
            if qtd_str is None:
                return
            try:
                qtd = int(qtd_str)
                if qtd <= 0:
                    print("A quantidade deve ser maior que zero!")
                    continue
                if qtd > info_livro["copias_disponiveis"]:
                    print(f"\nSó é possível descartar até {info_livro['copias_disponiveis']} cópias!")
                    print("(Não é possível descartar cópias que estão emprestadas)")
                    input("\nPressione Enter para continuar...")
                    continue
                
                # Atualiza as quantidades
                info_livro["copias_totais"] -= qtd
                info_livro["copias_disponiveis"] -= qtd
                
                # Se não sobrou nenhuma cópia, remove o livro completamente
                if info_livro["copias_totais"] == 0:
                    livros.pop(titulo)
                    if titulo in emprestimos:
                        emprestimos.pop(titulo)
                    registrar_log(f"Livro '{titulo}' completamente descartado após remover últimas {qtd} cópias")
                    print("\nLivro completamente descartado após remover as últimas cópias!")
                else:
                    registrar_log(f"{qtd} cópias do livro '{titulo}' foram descartadas")
                    print(f"\n{qtd} cópias foram descartadas com sucesso!")
                break
            except ValueError:
                print("Por favor digite um número válido!")
    else:
        print("\nOpção inválida!")
        input("\nPressione Enter para continuar...")
        return
    
    # Salva as alterações
    salvar_livros(livros)
    salvar_emprestimos(emprestimos)

def ver_emprestimos_ativos():
    """Mostra todos os empréstimos ativos"""
    emprestimos = carregar_emprestimos()
    
    if not emprestimos:
        print("\nNenhum empréstimo registrado!")
        input("\nPressione Enter para continuar...")
        return
        
    print("\n=== EMPRÉSTIMOS ATIVOS ===")
    for titulo, lista in emprestimos.items():
        if lista:  # se há empréstimos ativos
            print(f"\nLivro: {titulo}")
            print(f"Quantidade: {len(lista)}")
            for emp in lista:
                print(f"Data do empréstimo: {emp['data_emprestimo']}")
    input("\nPressione Enter para continuar...")

def ver_historico():
    """Mostra o histórico completo de operações"""
    limpar_tela()
    if not os.path.exists(LOG_FILE):
        print("\nNenhum histórico disponível!")
        input("\nPressione Enter para continuar...")
        return
        
    print("\n=== HISTÓRICO DE OPERAÇÕES ===\n")
    with open(LOG_FILE, "r", encoding="utf-8") as f:
        print(f.read())
    input("\nPressione Enter para continuar...")

def menu_principal():
    """Exibe e gerencia o menu principal"""
    while True:
        limpar_tela()
        print("\n=== SISTEMA DE BIBLIOTECA ===")
        print("1. Adicionar novo livro")
        print("2. Listar livros")
        print("3. Emprestar livro")
        print("4. Devolver livro")
        print("5. Descartar livro")
        print("6. Ver empréstimos ativos")
        print("7. Ver histórico")
        print("8. Editar livro")
        print("9. Sair")
        
        opcao = input("\nEscolha uma opção: ")
        
        if opcao == "1":
            adicionar_livro()
        elif opcao == "2":
            listar_livros()
        elif opcao == "3":
            emprestar_livro()
        elif opcao == "4":
            devolver_livro()
        elif opcao == "5":
            descartar_livro()
        elif opcao == "6":
            ver_emprestimos_ativos()
        elif opcao == "7":
            ver_historico()
        elif opcao == "8":
            editar_livro()
        elif opcao == "9":
            registrar_log("Sistema encerrado")
            print("\nSistema encerrado!")
            break
        else:
            print("\nOpção inválida!")
            input("\nPressione Enter para continuar...")

def input_com_cancelamento(mensagem):
    """Lê entrada do usuário com opção de cancelamento"""
    entrada = input(f"{mensagem} (ou 'c' para cancelar): ")
    if entrada.lower() == 'c':
        print("\nOperação cancelada!")
        return None
    return entrada

def escolher_numero_com_cancelamento(mensagem, max_valor):
    """Lê um número com opção de cancelamento"""
    while True:
        entrada = input_com_cancelamento(mensagem)
        if entrada is None:
            return None
        try:
            escolha = int(entrada) - 1
            if 0 <= escolha < max_valor:
                return escolha
            print("Número inválido!")
        except ValueError:
            print("Por favor, digite um número válido!")

def editar_livro():
    """Edita informações de um livro"""
    config = carregar_config()
    livros = carregar_livros()
    emprestimos = carregar_emprestimos()
    
    if not livros:
        print("\nNão há livros cadastrados!")
        input("\nPressione Enter para continuar...")
        return
        
    print("\n=== LIVROS CADASTRADOS ===")
    for i, (titulo, info) in enumerate(livros.items(), 1):
        print(f"\n{i}. {titulo}")
        print(f"   Autor: {info['autor']}")
        print(f"   Categoria: {info['categoria']}")
        print(f"   Cópias: {info['copias_disponiveis']}/{info['copias_totais']}")
    
    escolha = escolher_numero_com_cancelamento("\nEscolha o número do livro para editar", len(livros))
    if escolha is None:
        return
        
    titulo_original = list(livros.keys())[escolha]
    info_livro = livros[titulo_original]
    
    while True:
        limpar_tela()
        print(f"\n=== EDITANDO: {titulo_original} ===")
        print(f"1. Título: {titulo_original}")
        print(f"2. Autor: {info_livro['autor']}")
        print(f"3. Categoria: {info_livro['categoria']}")
        print(f"4. Número total de cópias: {info_livro['copias_totais']}")
        print(f"5. Número de cópias disponíveis: {info_livro['copias_disponiveis']}")
        print("6. Voltar ao menu principal")
        
        opcao = input("\nEscolha o que deseja editar: ")
        
        if opcao == "1":
            novo_titulo = input_com_cancelamento("\nDigite o novo título")
            if novo_titulo is None:
                continue
            if novo_titulo in livros and novo_titulo != titulo_original:
                print("\nJá existe um livro com este título!")
                input("\nPressione Enter para continuar...")
                continue
            
            # Atualiza o título
            livros[novo_titulo] = livros.pop(titulo_original)
            if titulo_original in emprestimos:
                emprestimos[novo_titulo] = emprestimos.pop(titulo_original)
            titulo_original = novo_titulo
            registrar_log(f"Título do livro alterado de '{titulo_original}' para '{novo_titulo}'")
            
        elif opcao == "2":
            novo_autor = input_com_cancelamento("\nDigite o novo autor")
            if novo_autor is None:
                continue
            info_livro['autor'] = novo_autor
            registrar_log(f"Autor do livro '{titulo_original}' alterado para '{novo_autor}'")
            
        elif opcao == "3":
            print("\nCategorias disponíveis:")
            for i, cat in enumerate(config["categorias"], 1):
                print(f"{i}. {cat}")
            
            cat_idx = escolher_numero_com_cancelamento("\nEscolha o número da nova categoria", len(config["categorias"]))
            if cat_idx is None:
                continue
            nova_categoria = config["categorias"][cat_idx]
            info_livro['categoria'] = nova_categoria
            registrar_log(f"Categoria do livro '{titulo_original}' alterada para '{nova_categoria}'")
            
        elif opcao == "4":
            while True:
                novas_copias = input_com_cancelamento("\nDigite o novo número total de cópias")
                if novas_copias is None:
                    break
                try:
                    novas_copias = int(novas_copias)
                    if novas_copias <= 0:
                        print("O número de cópias deve ser maior que zero!")
                        continue
                        
                    # Calcula quantas cópias estão emprestadas
                    copias_emprestadas = info_livro['copias_totais'] - info_livro['copias_disponiveis']
                    if novas_copias < copias_emprestadas:
                        print(f"\nNão é possível reduzir para {novas_copias} cópias!")
                        print(f"Existem {copias_emprestadas} cópias emprestadas atualmente.")
                        input("\nPressione Enter para continuar...")
                        break
                        
                    # Ajusta as cópias disponíveis proporcionalmente
                    diferenca = novas_copias - info_livro['copias_totais']
                    info_livro['copias_totais'] = novas_copias
                    info_livro['copias_disponiveis'] += diferenca
                    registrar_log(f"Número total de cópias do livro '{titulo_original}' alterado para {novas_copias}")
                    break
                except ValueError:
                    print("Por favor digite um número válido!")
                    
        elif opcao == "5":
            while True:
                novas_disponiveis = input_com_cancelamento("\nDigite o novo número de cópias disponíveis")
                if novas_disponiveis is None:
                    break
                try:
                    novas_disponiveis = int(novas_disponiveis)
                    if novas_disponiveis < 0:
                        print("O número de cópias disponíveis não pode ser negativo!")
                        continue
                    if novas_disponiveis > info_livro['copias_totais']:
                        print("O número de cópias disponíveis não pode ser maior que o total!")
                        continue
                        
                    # Verifica se há empréstimos ativos
                    if titulo_original in emprestimos:
                        emprestimos_ativos = sum(1 for emp in emprestimos[titulo_original] 
                                               if emp["status"] == "emprestado")
                        copias_necessarias = info_livro['copias_totais'] - novas_disponiveis
                        if emprestimos_ativos > copias_necessarias:
                            print(f"\nNão é possível definir {novas_disponiveis} cópias disponíveis!")
                            print(f"Existem {emprestimos_ativos} empréstimos ativos atualmente.")
                            input("\nPressione Enter para continuar...")
                            break
                    
                    info_livro['copias_disponiveis'] = novas_disponiveis
                    registrar_log(f"Número de cópias disponíveis do livro '{titulo_original}' alterado para {novas_disponiveis}")
                    break
                except ValueError:
                    print("Por favor digite um número válido!")
                    
        elif opcao == "6":
            break
        else:
            print("\nOpção inválida!")
            input("\nPressione Enter para continuar...")
            continue
        
        # Salva as alterações
        salvar_livros(livros)
        salvar_emprestimos(emprestimos)

if __name__ == "__main__":
    menu_principal()
