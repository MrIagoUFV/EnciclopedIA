# Vamos criar um programa para gerenciar um cardápio de restaurante!

# Dicionário para armazenar as categorias e seus pratos
# Dicionários são como gavetas organizadas por nomes (chaves)
cardapio = {
    "Pratos": [],      # Lista vazia para guardar os pratos
    "Bebidas": [],     # Lista vazia para guardar as bebidas
    "Sobremesas": []   # Lista vazia para guardar as sobremesas
}

# Tupla com as categorias disponíveis
# Tuplas são como listas, mas não podem ser alteradas depois de criadas
categorias = ("Pratos", "Bebidas", "Sobremesas")

while True:
    try:
        print("\n=== GERENCIADOR DE CARDÁPIO ===")
        print("1 - Adicionar item")
        print("2 - Ver cardápio")
        print("3 - Remover item")
        print("0 - Sair")
        
        opcao = int(input("\nEscolha uma opção: "))
        
        if opcao == 0:
            break
            
        elif opcao == 1:
            # Usando tupla para mostrar opções válidas
            print("\nCategorias:", categorias)
            categoria = input("Digite a categoria: ")
            
            # Verificando se a categoria existe no dicionário
            if categoria in cardapio:
                item = input("Digite o nome do item: ")
                preco = float(input("Digite o preço: "))
                
                # Adicionando item como tupla (nome, preço) na lista da categoria
                cardapio[categoria].append((item, preco))
                print(f"\n{item} adicionado com sucesso!")
            else:
                print("\nCategoria inválida!")
                
        elif opcao == 2:
            # Percorrendo o dicionário e mostrando todos os itens
            for categoria in cardapio:
                print(f"\n=== {categoria} ===")
                for item, preco in cardapio[categoria]:
                    print(f"{item}: R${preco:.2f}")
                    
        elif opcao == 3:
            categoria = input("\nDigite a categoria do item: ")
            if categoria in cardapio:
                # Criando lista de apenas os nomes dos itens
                itens = [item[0] for item in cardapio[categoria]]
                print(f"\nItens em {categoria}:", itens)
                
                item = input("Digite o nome do item para remover: ")
                
                # Procurando o item na lista da categoria
                for i, (nome, _) in enumerate(cardapio[categoria]):
                    if nome == item:
                        # Removendo item da lista usando seu índice
                        cardapio[categoria].pop(i)
                        print(f"\n{item} removido com sucesso!")
                        break
                else:
                    print("\nItem não encontrado!")
            else:
                print("\nCategoria inválida!")
                
    except ValueError:
        print("\nPor favor, digite uma opção válida!")
        continue
