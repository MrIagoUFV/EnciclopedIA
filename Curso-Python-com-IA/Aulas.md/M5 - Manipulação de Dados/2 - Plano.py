"""
plano das funcionalidades:
    - o usuário pode ver o menu inicial
        - 1. Adicionar um novo livro
        - 2. Ver os livros disponíveis
        - 3. Emprestar um livro
        - 4. Devolver um livro
        - 5. Descartar um livro
        - 6. Ver empréstimos ativos
        - 7. Ver histórico de empréstimos
        - 8. Sair

# definindo os livros:
    - cada livro tem um título, uma categoria, um autor e um número de cópias
    - o número de cópias é o número de vezes que o livro pode ser emprestado
    - o número de cópias disponíveis é o número de vezes que o livro pode ser emprestado no momento
    - categorias disponíveis:
        - Ler o arquivo config.json para pegar as categorias disponíveis (se não existir, crie o arquivo com as categorias padrão "Ficção", "Não-Ficção" e "Técnico")
    - para adicionar um novo livro, peça para o usuário digitar o título, a categoria, o autor e o número de cópias
        - Adicione as informações em um arquivo chamado "livros.json" (crie o arquivo se não existir)
    - para ver os livros disponíveis, mostre todos os livros com as informações detalhadas
        - Leia o arquivo "livros.json" para pegar os livros disponíveis
    - para emprestar um livro, peça para o usuário digitar o título do livro que ele quer emprestar
        - se o livro existir, empreste um exemplar e atualize o número de cópias disponíveis
        - se não existir, mostre uma mensagem de erro
        - Atualize as informações em um arquivo chamado "emprestimos.json" (crie o arquivo se não existir)
    - para devolver um livro, peça para o usuário digitar o título do livro que ele quer devolver
        - se o livro existir, devolva um exemplar e atualize o número de cópias disponíveis
        - se não existir, mostre uma mensagem de erro
        - Atualize as informações em um arquivo chamado "emprestimos.json" (crie o arquivo se não existir)
    - para descartar um livro, peça para o usuário digitar o título do livro que ele quer descartar
        - se o livro existir, descarte um exemplar e atualize o número de cópias disponíveis
        - se não existir, mostre uma mensagem de erro
        - Atualize as informações em um arquivo chamado "livros.json" (e "emprestimos.json" se o livro estiver emprestado e tiver acabado os livros não emprestados)
    - para ver os empréstimos ativos, mostre todos os empréstimos ativos com as informações detalhadas
        - Leia o arquivo "emprestimos.json" para pegar os empréstimos ativos
    - para ver o histórico de empréstimos, mostre todos os empréstimos com as informações detalhadas
        - Leia o arquivo "log.txt" para pegar o histórico de empréstimos
    
    Pontos de atenção:
        - Sempre que for atualizar um arquivo, lembre-se de salvar as atualizações feitas no log.txt

"""