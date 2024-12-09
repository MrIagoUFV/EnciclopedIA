# CLASSE: É um modelo/template que define a estrutura de objetos
# Define atributos (características) e métodos (comportamentos)
class Item:
    # CONSTRUTOR: Método especial que inicializa um novo objeto
    # self representa a própria instância do objeto sendo criado
    def __init__(self, titulo, codigo):
        # ATRIBUTOS: Características do objeto
        self.titulo = titulo
        self.codigo = codigo
        self.emprestado = False
    
    # MÉTODO: Função que define um comportamento do objeto
    def emprestar(self):
        if not self.emprestado:
            self.emprestado = True
            return f"{self.titulo} foi emprestado com sucesso!"
        return f"{self.titulo} já está emprestado!"

# HERANÇA: Livro herda de Item (reusa código da classe pai)
# Livro é uma SUBCLASSE de Item (classe pai)
class Livro(Item):
    def __init__(self, titulo, codigo, autor, paginas):
        # super() permite acessar métodos da classe pai
        super().__init__(titulo, codigo)
        self.autor = autor
        self.paginas = paginas
    
    # MÉTODO ESPECIAL: Define como o objeto será convertido para string
    # Exemplo de POLIMORFISMO - cada classe pode implementar seu próprio __str__
    def __str__(self):
        return f"Livro: {self.titulo} por {self.autor}"

# Outra classe que herda de Item
class Revista(Item):
    def __init__(self, titulo, codigo, edicao):
        super().__init__(titulo, codigo)
        self.edicao = edicao
    
    def __str__(self):
        return f"Revista: {self.titulo} - Edição {self.edicao}"

# COMPOSIÇÃO: Biblioteca contém (tem) vários itens
# Relacionamento "tem um" ou "tem vários"
class Biblioteca:
    def __init__(self, nome):
        self.nome = nome
        # Lista que armazena os objetos - exemplo de composição
        self.itens = []
    
    def adicionar_item(self, item):
        self.itens.append(item)
    
    # POLIMORFISMO: Mesmo método funciona para diferentes tipos (Livro/Revista)
    # O Python chama automaticamente o __str__ apropriado para cada tipo
    def listar_itens(self):
        for item in self.itens:
            print(item)

# Programa principal
def main():
    # Criando a biblioteca
    nome_biblioteca = input("Digite o nome da biblioteca: ")
    biblioteca = Biblioteca(nome_biblioteca)
    
    while True:
        print("\n=== MENU DA BIBLIOTECA ===")
        print("1 - Adicionar livro")
        print("2 - Adicionar revista") 
        print("3 - Listar itens")
        print("4 - Emprestar item")
        print("0 - Sair")
        
        opcao = input("\nEscolha uma opção: ")
        
        if opcao == "0":
            break
            
        elif opcao == "1":
            titulo = input("Digite o título do livro: ")
            codigo = input("Digite o código do livro: ")
            autor = input("Digite o autor do livro: ")
            paginas = int(input("Digite o número de páginas: "))
            livro = Livro(titulo, codigo, autor, paginas)
            biblioteca.adicionar_item(livro)
            print("\nLivro adicionado com sucesso!")
            
        elif opcao == "2":
            titulo = input("Digite o título da revista: ")
            codigo = input("Digite o código da revista: ")
            edicao = input("Digite a edição da revista: ")
            revista = Revista(titulo, codigo, edicao)
            biblioteca.adicionar_item(revista)
            print("\nRevista adicionada com sucesso!")
            
        elif opcao == "3":
            print("\nItens na biblioteca:")
            biblioteca.listar_itens()
            
        elif opcao == "4":
            print("\nItens disponíveis:")
            for i, item in enumerate(biblioteca.itens):
                print(f"{i+1} - {item}")
            try:
                indice = int(input("\nDigite o número do item para emprestar: ")) - 1
                if 0 <= indice < len(biblioteca.itens):
                    print(biblioteca.itens[indice].emprestar())
                else:
                    print("Item inválido!")
            except ValueError:
                print("Por favor, digite um número válido!")
        
        else:
            print("Opção inválida!")

if __name__ == "__main__":
    main()