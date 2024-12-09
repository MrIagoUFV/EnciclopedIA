
"""
História de Uso do sistema de Biblioteca

Como usuário da biblioteca, quando inicio o programa...

1. Primeiro me pedem para dar um nome para a biblioteca
   "Digite o nome da biblioteca: " → Digite "Biblioteca Municipal"

2. Aparece um menu com várias opções:
   === MENU DA BIBLIOTECA ===
   1 - Adicionar livro
   2 - Adicionar revista
   3 - Listar itens 
   4 - Emprestar item
   0 - Sair

3. Se escolho adicionar um livro (opção 1):
   - Digito o título do livro: "O Senhor dos Anéis"
   - Digito o código: "L001" 
   - Digito o autor: "J.R.R. Tolkien"
   - Digito número de páginas: "1200"
   → Recebo mensagem "Livro adicionado com sucesso!"

4. Se escolho adicionar uma revista (opção 2):
   - Digito o título: "Superinteressante"
   - Digito o código: "R001"
   - Digito a edição: "405"
   → Recebo mensagem "Revista adicionada com sucesso!"

5. Se quero ver o que tem na biblioteca (opção 3):
   → Vejo lista:
   Livro: O Senhor dos Anéis por J.R.R. Tolkien
   Revista: Superinteressante - Edição 405

6. Se quero emprestar algo (opção 4):
   - Vejo lista numerada dos itens disponíveis
   - Escolho o número do item que quero
   → Se item disponível: "O Senhor dos Anéis foi emprestado com sucesso!"
   → Se já emprestado: "O Senhor dos Anéis já está emprestado!"

7. Posso continuar usando o menu até decidir sair (opção 0)

Em caso de erros:
- Se digito opção inválida → "Opção inválida!"
- Se digito número errado ao emprestar → "Item inválido!"
- Se digito letra em vez de número → "Por favor, digite um número válido!"
"""

"""
Plano para Criar um Sistema de Biblioteca

1. Primeiro, vamos criar um item básico que toda biblioteca tem:
   - Criar classe Item com título e código
   - Adicionar sistema de empréstimo (emprestado sim/não)
   - Fazer função para emprestar item

2. Agora vamos criar tipos específicos de itens:
   - Criar Livro que é um tipo de Item
     * Adicionar autor e número de páginas
     * Fazer aparecer bonito quando imprimir
   
   - Criar Revista que é outro tipo de Item
     * Adicionar número da edição
     * Fazer aparecer bonito quando imprimir

3. Criar a Biblioteca em si:
   - Dar um nome para biblioteca
   - Fazer lista para guardar os itens
   - Criar função para adicionar novos itens
   - Criar função para mostrar todos os itens

4. Criar o programa principal com menu:
   - Mostrar opções para o usuário
   - Opção de adicionar livro novo
   - Opção de adicionar revista nova
   - Opção de ver lista de itens
   - Opção de emprestar um item
   - Opção de sair do programa

5. Fazer o programa funcionar:
   - Pedir nome da biblioteca
   - Mostrar menu e esperar escolha
   - Tratar cada opção do menu
   - Continuar até usuário querer sair
"""




# PSEUDOCODIGO

"""
MODELO DE ITEM BÁSICO:
    Quando criar novo item:
        Guarde o título do item
        Guarde o código do item
        Marque como não emprestado
    
    Quando alguém pedir emprestado:
        Se não estiver emprestado:
            Marque como emprestado
            Avise que empréstimo deu certo
        Senão:
            Avise que já está emprestado

    Quando alguém pedir para devolver:
        Marque como não emprestado
        Avise que devolução foi feita

MODELO DE LIVRO (é um tipo de item):
    Quando criar novo livro:
        Crie como item normal
        Guarde também o autor
        Guarde também número de páginas
    
    Quando precisar mostrar o livro:
        Mostre: "Livro: [título] por [autor]"

MODELO DE REVISTA (é um tipo de item):
    Quando criar nova revista:
        Crie como item normal
        Guarde também o número da edição
    
    Quando precisar mostrar a revista:
        Mostre: "Revista: [título] - Edição [edição]"

MODELO DA BIBLIOTECA:
    Quando criar nova biblioteca:
        Guarde o nome dela
        Crie uma lista vazia para os itens
    
    Para guardar novo item:
        Coloque o item na lista
    
    Para descartar um item:
        Remova o item da lista
    
    Para mostrar todos os itens:
        Para cada item na lista:
            Mostre o item

PROGRAMA PRINCIPAL:
    Pergunte o nome da biblioteca
    Crie uma biblioteca com este nome
    
    Faça sempre:
        Sempre que voltar ao menu, limpe a tela
        Mostre o menu de opções com o nome da biblioteca no topo em ascii art (crie um função para definir o ascii art de cada letra com o caractere de quadradinho)
        Espere a escolha do usuário
        
        Se escolheu sair:
            Termine o programa e mostre um mensagem em ascii art
        
        Se escolheu adicionar livro:
            Pergunte os dados do livro
            Crie o livro
            Guarde na biblioteca
            Avise que deu certo
        
        Se escolheu adicionar revista:
            Pergunte os dados da revista
            Crie a revista
            Guarde na biblioteca
            Avise que deu certo
        
        Se escolheu listar itens:
            Mostre todos os itens da biblioteca
        
        Se escolheu devolver:
            Mostre lista numerada dos itens
            Pergunte qual quer devolver
            Se número válido:
                Tente devolver e mostre resultado
            Senão:
                Avise que número é inválido
        
        Se escolheu emprestar:
            Mostre lista numerada dos itens
            Pergunte qual quer emprestar
            Se número válido:
                Tente emprestar e mostre resultado
            Senão:
                Avise que número é inválido

        Se escolheu descarte:
            Mostre lista numerada dos itens
            Pergunte qual quer descartar
            Se número válido:
                Tente descartar e mostre resultado
            Senão:
                Avise que número é inválido
        
        Se escolheu opção que não existe:
            Avise que opção é inválida
        
Sempre que voltar ao menu, limpe a tela
"""
