import os
from time import sleep

# Criando as listas vazias para cada categoria
pratos = []
bebidas = []
sobremesas = []

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def mostrar_ascii_art():
    print("""
    __  ____      __            __  ____                    
   /  |/  (_)____/ /____  _____/ / / / /_  ____ ___  ____ ___
  / /|_/ / / ___/ __/ _ \/ ___/ / / / __ \/ __ `__ \/ __ `__ \\
 / /  / / (__  ) /_/  __/ /  / /_/ / / / / / / / / / / / / / /
/_/  /_/_/____/\__/\___/_/   \____/_/ /_/_/ /_/ /_/_/ /_/ /_/ 
    """)

def mostrar_ascii_tchau():
    print("""
     _______ _____ _    _          _    _ _ 
    |__   __/ ____| |  | |   /\   | |  | | |
       | | | |    | |__| |  /  \  | |  | | |
       | | | |    |  __  | / /\ \ | |  | | |
       | | | |____| |  | |/ ____ \| |__| |_|
       |_|  \_____|_|  |_/_/    \_\\____/(_)
                                            
    .--.      .-'.      .--.      .--.      .--.      .--.      .`-.      .--.
:::::.\::::::::.\::::::::.\::::::::.\::::::::.\::::::::.\::::::::.\::::::::.\
'      `--'      `.-'      `--'      `--'      `--'      `-.'      `--'      `
    """)

while True:
    try:
        limpar_tela()
        mostrar_ascii_art()
        print("\nO que você quer fazer?")
        print("1 - Adicionar alguma coisa nova")
        print("2 - Ver o cardápio")
        print("3 - Remover alguma coisa")
        print("0 - Sair")

        opcao = int(input("\nEscolha uma opção: "))

        if opcao == 0:
            limpar_tela()
            mostrar_ascii_tchau()
            print("\nObrigado por usar nosso sistema!")
            sleep(2)
            break

        elif opcao == 1:
            print("\nQual categoria? (Pratos/Bebidas/Sobremesas)")
            categoria = input().strip().capitalize()
            
            if categoria in ["Pratos", "Bebidas", "Sobremesas"]:
                nome = input("Nome do item: ")
                preco = float(input("Preço: R$"))
                
                if categoria == "Pratos":
                    pratos.append((nome, preco))
                elif categoria == "Bebidas":
                    bebidas.append((nome, preco))
                else:
                    sobremesas.append((nome, preco))
                    
                print(f"\n{nome} adicionado com sucesso!")
                sleep(2)
            else:
                print("\nCategoria inválida!")
                sleep(2)

        elif opcao == 2:
            print("\n=== CARDÁPIO ===")
            
            print("\nPRATOS:")
            if pratos:
                for nome, preco in pratos:
                    print(f"{nome}: R${preco:.2f}")
            else:
                print("Nenhum prato cadastrado")
                
            print("\nBEBIDAS:")
            if bebidas:
                for nome, preco in bebidas:
                    print(f"{nome}: R${preco:.2f}")
            else:
                print("Nenhuma bebida cadastrada")
                
            print("\nSOBREMESAS:")
            if sobremesas:
                for nome, preco in sobremesas:
                    print(f"{nome}: R${preco:.2f}")
            else:
                print("Nenhuma sobremesa cadastrada")
                
            input("\nPressione ENTER para continuar...")

        elif opcao == 3:
            print("\nDe qual categoria deseja remover? (Pratos/Bebidas/Sobremesas)")
            categoria = input().strip().capitalize()
            
            if categoria == "Pratos":
                lista = pratos
            elif categoria == "Bebidas":
                lista = bebidas
            elif categoria == "Sobremesas":
                lista = sobremesas
            else:
                print("Categoria inválida!")
                sleep(2)
                continue
                
            if not lista:
                print(f"\nNão há itens em {categoria}")
                sleep(2)
                continue
                
            print(f"\nItens em {categoria}:")
            for nome, _ in lista:
                print(nome)
                
            item = input("\nQual item deseja remover? ")
            
            for i, (nome, _) in enumerate(lista):
                if nome.lower() == item.lower():
                    lista.pop(i)
                    print(f"\n{nome} removido com sucesso!")
                    sleep(2)
                    break
            else:
                print("\nItem não encontrado!")
                sleep(2)

        else:
            print("\nOpção inválida!")
            sleep(2)

    except ValueError:
        print("\nPor favor, digite uma opção válida!")
        sleep(2)


