import os

# Classe base para itens da biblioteca
class Item:
    def __init__(self, titulo, codigo):
        self.titulo = titulo
        self.codigo = codigo
        self.copias_totais = 0
        self.copias_disponiveis = 0
        self.emprestado = False
    
    def definir_copias(self, quantidade):
        self.copias_totais = quantidade
        self.copias_disponiveis = quantidade
    
    def emprestar(self):
        if self.copias_disponiveis > 0:
            self.copias_disponiveis -= 1
            if self.copias_disponiveis == 0:
                self.emprestado = True
            return f"{self.titulo} foi emprestado com sucesso! ({self.copias_disponiveis} cópias disponíveis)"
        return f"{self.titulo} não possui cópias disponíveis!"
        
    def devolver(self):
        if self.copias_disponiveis < self.copias_totais:
            self.copias_disponiveis += 1
            self.emprestado = False
            return f"{self.titulo} foi devolvido com sucesso! ({self.copias_disponiveis} cópias disponíveis)"
        return f"{self.titulo} já está com todas as cópias disponíveis!"

# Classe para livros, herda de Item
class Livro(Item):
    def __init__(self, titulo, codigo, autor, paginas):
        super().__init__(titulo, codigo)
        self.autor = autor
        self.paginas = paginas
    
    def __str__(self):
        status = f"(INDISPONÍVEL - {self.copias_disponiveis}/{self.copias_totais} cópias)" if self.emprestado else f"(DISPONÍVEL - {self.copias_disponiveis}/{self.copias_totais} cópias)"
        return f"Livro: {self.titulo} por {self.autor} {status}"

# Classe para revistas, herda de Item  
class Revista(Item):
    def __init__(self, titulo, codigo, edicao):
        super().__init__(titulo, codigo)
        self.edicao = edicao
    
    def __str__(self):
        status = f"(INDISPONÍVEL - {self.copias_disponiveis}/{self.copias_totais} cópias)" if self.emprestado else f"(DISPONÍVEL - {self.copias_disponiveis}/{self.copias_totais} cópias)"
        return f"Revista: {self.titulo} - Edição {self.edicao} {status}"

# Classe que gerencia a biblioteca
class Biblioteca:
    def __init__(self, nome):
        self.nome = nome
        self.itens = []
    
    def adicionar_item(self, item):
        self.itens.append(item)
        
    def descartar_item(self, indice, quantidade=None):
        if 0 <= indice < len(self.itens):
            item = self.itens[indice]
            if quantidade is None or quantidade >= item.copias_totais:
                self.itens.pop(indice)
                return f"Todas as cópias de {item.titulo} foram descartadas com sucesso!"
            else:
                if quantidade > 0:
                    item.copias_totais -= quantidade
                    item.copias_disponiveis = min(item.copias_disponiveis, item.copias_totais)
                    return f"{quantidade} cópia(s) de {item.titulo} foi(foram) descartada(s) com sucesso! ({item.copias_totais} cópias restantes)"
                return "Quantidade inválida!"
        return "Item inválido!"
    
    def listar_itens(self):
        for i, item in enumerate(self.itens, 1):
            print(f"{i} - {item}")

def criar_ascii_art(texto):
    # Dicionário para normalizar caracteres especiais
    normalize = {
        'Á': 'A', 'À': 'A', 'Ã': 'A', 'Â': 'A', 'Ä': 'A',
        'É': 'E', 'È': 'E', 'Ê': 'E', 'Ë': 'E',
        'Í': 'I', 'Ì': 'I', 'Î': 'I', 'Ï': 'I',
        'Ó': 'O', 'Ò': 'O', 'Õ': 'O', 'Ô': 'O', 'Ö': 'O',
        'Ú': 'U', 'Ù': 'U', 'Û': 'U', 'Ü': 'U',
        'Ý': 'Y', 'Ÿ': 'Y',
        'Ñ': 'N',
        'Ç': 'C',
        # Adicione outros caracteres especiais conforme necessário
    }
    
    # Normaliza o texto antes de processar
    texto_normalizado = ''
    for char in texto.upper():
        texto_normalizado += normalize.get(char, char)
    
    # Definindo a arte ASCII para cada letra
    letras = {
        'A': [
            "      /\\      ",
            "     /  \\     ",
            "    / /\\ \\    ",
            "   / ____ \\   ",
            "  /_/    \\_\\  ",
            "              "
        ],
        'B': [
            "   ______     ",
            "  |  __  \\    ",
            "  | |__) |    ",
            "  |  _  /     ",
            "  | |_) |     ",
            "  |____/      "
        ],
        'C': [
            "   _____     ",
            "  / ____|    ",
            " | |         ",
            " | |         ",
            " | |____     ",
            "  \\_____|    "
        ],
        'D': [
            "  _____      ",
            " |  __ \\     ",
            " | |  | |    ",
            " | |  | |    ",
            " | |__| |    ",
            " |_____/     "
        ],
        'E': [
            "  ______     ",
            " |  ____|    ",
            " | |__       ",
            " |  __|      ",
            " | |____     ",
            " |______|    "
        ],
        'F': [
            "  ______     ",
            " |  ____|    ",
            " | |__       ",
            " |  __|      ",
            " | |         ",
            " |_|         "
        ],
        'G': [
            "   _____     ",
            "  / ____|    ",
            " | |  __     ",
            " | | |_ |    ",
            " | |__| |    ",
            "  \\_____|    "
        ],
        'H': [
            "  _    _     ",
            " | |  | |    ",
            " | |__| |    ",
            " |  __  |    ",
            " | |  | |    ",
            " |_|  |_|    "
        ],
        'I': [
            "  _____     ",
            " |_   _|    ",
            "   | |      ",
            "   | |      ",
            "  _| |_     ",
            " |_____|    "
        ],
        'J': [
            "       _    ",
            "      | |   ",
            "      | |   ",
            "  _   | |   ",
            " | |__| |   ",
            "  \\____/    "
        ],
        'K': [
            "  _  __     ",
            " | |/ /     ",
            " | ' /      ",
            " |  <       ",
            " | . \\      ",
            " |_|\\_\\     "
        ],
        'L': [
            "  _         ",
            " | |        ",
            " | |        ",
            " | |        ",
            " | |____    ",
            " |______|   "
        ],
        'M': [
            "  __  __    ",
            " |  \\/  |   ",
            " | \\  / |   ",
            " | |\\/| |   ",
            " | |  | |   ",
            " |_|  |_|   "
        ],
        'N': [
            "  _   _     ",
            " | \\ | |    ",
            " |  \\| |    ",
            " | . ` |    ",
            " | |\\  |    ",
            " |_| \\_|    "
        ],
        'O': [
            "   ____     ",
            "  / __ \\    ",
            " | |  | |   ",
            " | |  | |   ",
            " | |__| |   ",
            "  \\____/    "
        ],
        'P': [
            "  _____     ",
            " |  __ \\    ",
            " | |__) |   ",
            " |  ___/    ",
            " | |        ",
            " |_|        "
        ],
        'Q': [
            "   ____     ",
            "  / __ \\    ",
            " | |  | |   ",
            " | |  | |   ",
            " | |__| |   ",
            "  \\___\\_\\   "
        ],
        'R': [
            "  _____     ",
            " |  __ \\    ",
            " | |__) |   ",
            " |  _  /    ",
            " | | \\ \\    ",
            " |_|  \\_\\   "
        ],
        'S': [
            "   _____    ",
            "  / ____|   ",
            " | (___     ",
            "  \\___ \\    ",
            "  ____) |   ",
            " |_____/    "
        ],
        'T': [
            "  _______   ",
            " |__   __|  ",
            "    | |     ",
            "    | |     ",
            "    | |     ",
            "    |_|     "
        ],
        'U': [
            "  _    _    ",
            " | |  | |   ",
            " | |  | |   ",
            " | |  | |   ",
            " | |__| |   ",
            "  \\____/    "
        ],
        'V': [
            " __      __ ",
            " \\ \\    / / ",
            "  \\ \\  / /  ",
            "   \\ \\/ /   ",
            "    \\  /    ",
            "     \\/     "
        ],
        'W': [
            " __          __ ",
            " \\ \\        / / ",
            "  \\ \\  /\\  / /  ",
            "   \\ \\/  \\/ /   ",
            "    \\  /\\  /    ",
            "     \\/  \\/     "
        ],
        'X': [
            " __   __   ",
            " \\ \\ / /   ",
            "  \\ V /    ",
            "   > <     ",
            "  / . \\    ",
            " /_/ \\_\\   "
        ],
        'Y': [
            " __   __   ",
            " \\ \\ / /   ",
            "  \\ V /    ",
            "   | |     ",
            "   | |     ",
            "   |_|     "
        ],
        'Z': [
            "  ______   ",
            " |___  /   ",
            "    / /    ",
            "   / /     ",
            "  / /__    ",
            " /_____|   "
        ],
        ' ': [
            "           ",
            "           ",
            "           ",
            "           ",
            "           ",
            "           "
        ]
    }
    
    # Inicializa as linhas da arte
    linhas_arte = ["", "", "", "", "", ""]
    
    # Para cada letra no texto normalizado
    for letra in texto_normalizado:
        # Se a letra existe no dicionário
        if letra in letras:
            # Adiciona cada linha da letra à linha correspondente da arte
            for i in range(6):
                linhas_arte[i] += letras[letra][i]
        else:
            # Para caracteres não suportados, adiciona espaço
            for i in range(6):
                linhas_arte[i] += letras[' '][i]
    
    return "\n".join(linhas_arte)

def input_com_cancelamento(mensagem):
    valor = input(f"{mensagem} (ou 'c' para cancelar): ")
    if valor.lower() == 'c':
        return None
    return valor

def main():
    nome_biblioteca = input("Digite o nome da biblioteca: ")
    biblioteca = Biblioteca(nome_biblioteca)
    
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("\n" + criar_ascii_art(biblioteca.nome))
        print("\n=== MENU DA BIBLIOTECA ===")
        print("1 - Adicionar livro")
        print("2 - Adicionar revista")
        print("3 - Listar itens")
        print("4 - Emprestar item")
        print("5 - Devolver item")
        print("6 - Descartar item")
        print("0 - Sair")
        
        opcao = input("\nEscolha uma opção: ")
        
        if opcao == "0":
            print("\n" + criar_ascii_art("Até Logo!"))
            break
            
        elif opcao == "1":
            print("\nAdicionando novo livro (Digite 'c' para cancelar em qualquer momento)")
            titulo = input_com_cancelamento("Digite o título do livro")
            if titulo is None:
                print("Operação cancelada!")
                continue
                
            codigo = input_com_cancelamento("Digite o código do livro")
            if codigo is None:
                print("Operação cancelada!")
                continue
                
            autor = input_com_cancelamento("Digite o autor do livro")
            if autor is None:
                print("Operação cancelada!")
                continue
                
            try:
                paginas = input_com_cancelamento("Digite o número de páginas")
                if paginas is None:
                    print("Operação cancelada!")
                    continue
                paginas = int(paginas)
                
                copias = input_com_cancelamento("Digite o número de cópias disponíveis")
                if copias is None:
                    print("Operação cancelada!")
                    continue
                copias = int(copias)
                
                livro = Livro(titulo, codigo, autor, paginas)
                livro.definir_copias(copias)
                biblioteca.adicionar_item(livro)
                print("\nLivro adicionado com sucesso!")
            except ValueError:
                print("Valor inválido inserido. Operação cancelada!")
            
        elif opcao == "2":
            print("\nAdicionando nova revista (Digite 'c' para cancelar em qualquer momento)")
            titulo = input_com_cancelamento("Digite o título da revista")
            if titulo is None:
                print("Operação cancelada!")
                continue
                
            codigo = input_com_cancelamento("Digite o código da revista")
            if codigo is None:
                print("Operação cancelada!")
                continue
                
            edicao = input_com_cancelamento("Digite a edição da revista")
            if edicao is None:
                print("Operação cancelada!")
                continue
                
            try:
                copias = input_com_cancelamento("Digite o número de cópias disponíveis")
                if copias is None:
                    print("Operação cancelada!")
                    continue
                copias = int(copias)
                
                revista = Revista(titulo, codigo, edicao)
                revista.definir_copias(copias)
                biblioteca.adicionar_item(revista)
                print("\nRevista adicionada com sucesso!")
            except ValueError:
                print("Valor inválido inserido. Operação cancelada!")
            
        elif opcao == "3":
            print("\nItens na biblioteca:")
            biblioteca.listar_itens()
            
        elif opcao == "4":
            print("\nItens disponíveis:")
            biblioteca.listar_itens()
            try:
                entrada = input_com_cancelamento("\nDigite o número do item para emprestar")
                if entrada is None:
                    print("Operação cancelada!")
                    continue
                indice = int(entrada) - 1
                if 0 <= indice < len(biblioteca.itens):
                    print(biblioteca.itens[indice].emprestar())
                else:
                    print("Item inválido!")
            except ValueError:
                print("Por favor, digite um número válido!")
                
        elif opcao == "5":
            print("\nItens emprestados:")
            biblioteca.listar_itens()
            try:
                entrada = input_com_cancelamento("\nDigite o número do item para devolver")
                if entrada is None:
                    print("Operação cancelada!")
                    continue
                indice = int(entrada) - 1
                if 0 <= indice < len(biblioteca.itens):
                    print(biblioteca.itens[indice].devolver())
                else:
                    print("Item inválido!")
            except ValueError:
                print("Por favor, digite um número válido!")
                
        elif opcao == "6":
            print("\nItens na biblioteca:")
            biblioteca.listar_itens()
            try:
                entrada = input_com_cancelamento("\nDigite o número do item para descartar")
                if entrada is None:
                    print("Operação cancelada!")
                    continue
                indice = int(entrada) - 1
                
                if 0 <= indice < len(biblioteca.itens):
                    item = biblioteca.itens[indice]
                    print(f"\nO item possui {item.copias_totais} cópias no total")
                    tipo_descarte = input_com_cancelamento("Deseja descartar todas as cópias? (S/N)")
                    if tipo_descarte is None:
                        print("Operação cancelada!")
                        continue
                        
                    if tipo_descarte.upper() == 'S':
                        print(biblioteca.descartar_item(indice))
                    else:
                        qtd = input_com_cancelamento("Quantas cópias deseja descartar?")
                        if qtd is None:
                            print("Operação cancelada!")
                            continue
                        try:
                            qtd = int(qtd)
                            if qtd <= 0:
                                print("Por favor, digite um número maior que zero!")
                                continue
                            print(biblioteca.descartar_item(indice, qtd))
                        except ValueError:
                            print("Por favor, digite um número válido!")
                else:
                    print("Item inválido!")
            except ValueError:
                print("Por favor, digite um número válido!")
        
        else:
            print("Opção inválida!")
            
        input("\nPressione ENTER para continuar...")

if __name__ == "__main__":
    main()
