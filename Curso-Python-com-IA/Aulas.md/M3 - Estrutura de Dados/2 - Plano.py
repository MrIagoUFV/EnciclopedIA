"""
História de Uso do Gerenciador de Cardápio

Quando inicio o programa, vejo um menu bem organizado com várias opções. Vou contar como uso cada uma delas:

1. Primeiro, quero adicionar alguns pratos:
   - Escolho a opção 1 (Adicionar item)
   - O programa me mostra que posso escolher entre Pratos, Bebidas e Sobremesas
   - Digito "Pratos" e ele aceita
   - Digito o nome "Feijoada" 
   - Coloco o preço 45.90
   - Ele me avisa que adicionou com sucesso!

2. Vou adicionar mais algumas coisas:
   - Repito o processo e adiciono uma Coca-Cola em "Bebidas" por R$ 8.00
   - Depois um Pudim em "Sobremesas" por R$ 12.50
   - Cada vez que adiciono algo, recebo a confirmação

3. Agora quero ver como ficou tudo:
   - Escolho a opção 2 (Ver cardápio)
   - O programa me mostra tudo organizado por categoria
   - Vejo a Feijoada nos Pratos
   - A Coca-Cola nas Bebidas
   - E o Pudim nas Sobremesas
   - Todos com seus preços certinhos

4. Ops, preciso remover algo:
   - Escolho a opção 3 (Remover item)
   - Digito "Bebidas" como categoria
   - Ele me mostra a Coca-Cola que está lá
   - Peço para remover a Coca-Cola
   - Ele confirma que removeu

5. Para confirmar a remoção:
   - Vejo o cardápio de novo (opção 2)
   - A Coca-Cola não está mais lá!
   - Só aparecem a Feijoada e o Pudim

6. Para finalizar:
   - Escolho a opção 0
   - O programa fecha direitinho
   - Com uma mensagem de adeus em ascii ascii art

   Pontos de atenção:
    - Sempre que voltar para o menu inicial, limpar a tela

Se eu digitar algo errado em qualquer momento, 
como uma categoria que não existe ou uma letra 
quando deveria ser número, o programa me avisa 
do erro e me deixa tentar de novo!
"""

# PSEUDO-CODIGO:

"""
INÍCIO DO PROGRAMA: GERENCIADOR DE CARDÁPIO

Criar três listas vazias:
- Uma para guardar os pratos
- Uma para guardar as bebidas
- Uma para guardar as sobremesas

Mostrar menu e repetir até a pessoa pedir para sair:
    Mostrar na tela:
    "O que você quer fazer?"
    "1 - Adicionar alguma coisa nova"
    "2 - Ver o cardápio"
    "3 - Remover alguma coisa"
    "0 - Sair"

    Esperar a pessoa escolher uma opção

    Se escolheu 0:
        Agradecer e fechar o programa

    Se escolheu 1:
        Perguntar qual categoria quer usar (Pratos, Bebidas ou Sobremesas)
        Perguntar o nome do item
        Perguntar o preço
        Guardar tudo na lista certa
        Avisar que deu certo

    Se escolheu 2:
        Para cada categoria: 
            Mostrar o nome da categoria
            Se tiver itens:
                Mostrar cada item e seu preço
            Se não tiver nada:
                Avisar que está vazia

    Se escolheu 3:
        Perguntar qual categoria
        Mostrar o que tem nessa categoria
        Perguntar qual item quer tirar
        Se encontrar o item:
            Tirar ele da lista
            Avisar que removeu
        Se não encontrar:
            Avisar que não achou

    Se digitou algo errado:
        Avisar que a opção não existe
        Voltar para o menu

Se em qualquer momento digitar algo errado:
    Mostrar mensagem de erro amigável
    Deixar tentar de novo

Pontos de atenção:
    - Limpe a tela sempre que voltar ao menu
    - Use ascii art em todo o programa e mensagens inclusive quando sair

FIM DO PROGRAMA
"""
