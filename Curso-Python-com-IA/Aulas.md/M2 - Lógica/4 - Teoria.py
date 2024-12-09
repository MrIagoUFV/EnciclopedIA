# MÓDULO 2 - LÓGICA DE PROGRAMAÇÃO COM PYTHON

"""
INTRODUÇÃO À LÓGICA DE PROGRAMAÇÃO COM PYTHON

Imagine que você está ensinando uma criança a fazer um bolo:
- Você não vai começar falando sobre química molecular ou termodinâmica, 
- Você vai explicar que precisamos de ingredientes (variáveis), 
- Adicionar itens na mistura (operadores), 
- Tomar decisões como "se a massa está muito líquida, adicione farinha" (condicionais), 
- Repetir alguns passos como "mexa até ficar homogêneo" (loops), 
- Usar o forno para assar, você bota toda aquela massa lá dentro e quando for tira, aquilo se transforma no bolo (funções).
- Antes de começar a fazer o bolo, quebrar os ovos num recipiente separado, e se estiver podre, você joga fora e tenta novamente com outro ovo (tratamento de erros).
"""

"""
Programação é exatamente assim! 
São apenas instruções passo a passo para o computador, 
numa ordem e estrutura que ele entenda e possa executar,
usando as ferramentas que ele tem à disposição,
pra manipular dados que ele recebe ou tem guardado:

1. VARIÁVEIS são como potes onde guardamos coisas:
    - No armario do quarto, guardamos vestimentas
    - Na geladeira, guardamos comida
    - Nas gavetas da cozinha, guardamos talheres
"""

"""
Então, existem coisas que podemos guardar para usar,
Cada coisa tem seu tipo, e cada tipo tem seu nome e seu lugar.
Do mesmo jeito que quando você ganha uma roupa você guarda no armario,
Sempre que você da algum dado para o computador,
Ele também guarda num lugar,
Mas antes, ele também precisa avaliar o tipo, 
se é um texto, um número, uma lista, etc.
"""

"""
Muitas linguagens não fazem isso, 
e você precisa entregar o dado pra ele informando o tipo,
    tipo: "O java, eu vou precisar que tu guarde uns números 
    de telefone pra mim, guarda tudo na caixinha chamada 'telefones'"
    Agora, aquela caixinha só aceita números de telefone,
    se você tentar guardar uma roupa lá dentro, o java vai reclamar.
"""

"""
Mas o Python tem TOC, ele gosta de tudo organizado,
então na hora que você da algo para ele guardar, 
ou pede pra ele separ um espaço pra você guardar algo depois,
ele decide sozinho o tipo dele, e se for diferente do que você esperava,
você pode reclamar, e pedir pra ele mudar depois.
"""

"""
Então por exemplo, se você criar um programa que pergunta sua idade,
e você digita 24, ele vai guardar como um número texto,
Você pode ficar até tipo "mas como assim é um texto?!"
Mas o Python já tá ficando velhinho, e todo velho tem suas manias.
Então faz parte, tem coisa q você tem q aprender a lidar,
Sempre então que você salvar algo no python digitando durante o programa,
você vai usar um input, que é sempre uma entrada de texto pro Python.
Aí depois, se você quiser transformar num número, 
você precisa pedir pra ele converter pro tipo que você quer.
"""

"""
Pode parecer chato, mas na prática é bem tranquilo,
e eu acho bem útil não ter que ficar declarando o tipo de cada coisa.
Na maioria das vezes, você nem vai bater cabeça com isso,
e o python vai descobrir o tipo certo 
das coisas que você der pra ele guardar.
"""

"""
2. OPERADORES permitem a gente fazer ações básicas com os dados
   - Contas: somar, subtrair, multiplicar, dividir
   - Comparações: se um número é maior que outro, etc

   Então por exemplo, se você quer somar dois números,
   você usa o operador de soma (+), 
   e o Python faz a conta pra você.
   
   É bem simples, a gente vai aprendendo eles na prática.
"""

"""
3. CONDICIONAIS são decisões baseadas em "se isso, então aquilo"
   - Na hora de sair: SE está frio, ENTÃO pego um casaco
   - Na rua: SE sinal verde, ENTÃO atravessa

   E eles podem usar os operadores que vimos antes,
   e podem ter mais de uma condição, usando o OU:

   - No mercado: 
        Eu quero comprar tal coisa, e quero pagar = 50 reais (Salvo a variavel preco_maximo)
        SE quando eu chegar num mercado, o preco_mercado_1 <= preco_maximo,
        ENTÃO eu compro nesse mercado
        SE NÃO, eu vou pro outro mercado
        SE no outro mercado, o preco_mercado_2 <= preco_maximo,
        ENTÃO eu compro nesse outro mercado
        SE NÃO, eu desisto de comprar.
"""

"""
4. LOOPS permite a gente repetir tarefas até que um objetivo seja alcançado
   - No mercado:
        Eu quero comprar tal coisa, e quero pagar = 50 reais (Salvo a variavel preco_maximo)

        ENQUANTO eu não encontrar um mercado com preço bom ou acabe os mercados da cidade:
            VOU PARA o mercado X (Começa com X = 0, o primeiro da lista)
            SE o preço desse mercado <= preco_maximo:
                ENTÃO compro nesse mercado e PARO de procurar
            SE NÃO:
                SE esse foi o último mercado da lista:
                    ENTÃO desisto de comprar e PARO de procurar
                SE NÃO:
                    CONTINUO procurando no próximo mercado X+1

   Ou seja, o loop vai ficar repetindo até que:
   - Ou encontre um mercado com preço bom
   - Ou acabe a lista de mercados
"""

"""
E Pode ser infinito, como quando você tá procurando uma vaga pra estacionar:
   ENQUANTO não achar vaga:
       Continua dando volta no quarteirão
       SE achou vaga:
           ENTÃO estaciona e PARA de procurar
       SE NÃO:
           CONTINUA procurando
"""

"""
5. FUNÇÕES são como fábricas que produzem ou modificam coisas,
seguindo um padrão que você define e usando as coisas que você
deu para ela usar.
   - Como fazer café: você sempre segue os mesmos passos,
   mas pode usar cafés diferentes,um dia um extra forte, outro dia um gourmet.
   e você pode opcioncalmente adicionar leite, ou açucar, ou não.
   e posso te falar como eu quero que você use esses ingredientes,
   e você vai fazer o café do jeito que eu quero.
   Se eu te dei um café, um pote de açucar, e uma caixa de leite,
   Você vai pegar um cadinho do café e vai fazer o café,
   Depois vai por um pouco do leite, 
   Se eu te pedir bem doce, você vai por mais açucar,
   Se eu não especificar nada, por padrão vc pode deixar levemente adoçado.
   efim, deu pra entender né?
"""

"""
   Quando você está programando, você pode criar uma função,
   para deixar pronto uma série de instruções que você vai usar,
   dado informações que você pode receber ou não,
   e pode criar a função para transformar as coisas que você passar para ela
   do jeito que você quer, seguindo um padrão que você define.
   E o bom, você escreve uma vez, e pode usar quantas vezes quiser,
   sem precisar passar as instruções toda hora,
   vc só chama a função, dá lá o café, o açucar e o leite,
   e fala como vc quer, se quer bem doce, etc.
   e outra pessoa pode usar a mesma função, e dar só o café,
   e ela já faz o resto pra você e pra outra pessoa
   sem precisar ensinar de novo como fazer para cada situação.
"""

"""
O mais legal? Você não precisa decorar como escrever tudo isso! 
A IA está aqui para ajudar com a parte chata (sintaxe). 
Você só precisa entender O QUE cada ferramenta faz 
e QUANDO usar cada uma. 
É como ter um assistente de cozinha que sabe todos os termos técnicos 
Você só precisa saber oq fazer em cada momento
Para guiar ela para fazer o trabalho sujo para você!
"""

# AGORA NA PRÁTICA!

# 0. COMENTAR E PRINTAR

## PROMPT: mostre "Olá, mundo!" na tela

## PROMPT: Comente essa linha

## PROMPT: adicione um comentário de múltiplas linhas explicando essa linha

# 1. VARIÁVEIS

## STRING
### PROMPT: crie uma variável chamada "nome" e guarde o nome "Iago"

## Inteiro (números inteiros)
### PROMPT: crie uma variável chamada "idade" e guarde o número 24

## Float (números decimais) 
### PROMPT: crie uma variável chamada "altura" e guarde o número 1.84

## Boolean (verdadeiro ou falso)
### PROMPT: crie uma variável chamada "programador" e guarde o valor True

## None (valor nulo/vazio)
### PROMPT: crie uma variável chamada "nada" e guarde o valor None

# Operações com variáveis:

## MOSTRAR NA TELA
### PROMPT: mostre na tela a variável nome

## VERIFICAR TIPO
### PROMPT: mostre na tela o tipo da variável altura

## CONVERTER TIPOS
### PROMPT: crie uma variável chamada "numero_texto" e guarde o valor "10"
### PROMPT: converta a variável numero_texto para inteiro e guarde em uma variável chamada "numero"
### PROMPT: mostre na tela o resultado de numero + 10

## CONCATENAR STRINGS
### PROMPT: crie uma variável chamada "nome" e guarde o valor "Iago"
### PROMPT: crie uma variável chamada "nome do meio" e guarde o valor "Lima"
### PROMPT: crie uma variável chamada "ultimo nome" e guarde o valor "Toledo"
### PROMPT: concatene as três variáveis em uma variável chamada "nome completo"
### PROMPT: mostre na tela o resultado de nome_completo

## FORMATAÇÃO DE STRINGS
### PROMPT: crie uma variável chamada "apresentacao" e guarde a string "Olá, me chamo {nome}, tenho {idade} anos e {altura}m de altura"
### PROMPT: mostre na tela o resultado de apresentacao

## OPERAÇÕES MATEMÁTICAS
### PROMPT: crie uma variável chamada "dobro" e guarde o resultado de idade * 2
### PROMPT: mostre na tela o resultado de dobro

### PROMPT: crie uma variável chamada "metade" e guarde o resultado de altura / 2
### PROMPT: mostre na tela o resultado de metade


# 2. OPERADORES

## SOMA
### PROMPT: crie uma variável chamada "soma" e guarde o resultado de num1 + num2
### PROMPT: mostre na tela o resultado de soma

## SUBTRAÇÃO
### PROMPT: crie uma variável chamada "subtracao" e guarde o resultado de num1 - num2
### PROMPT: mostre na tela o resultado de subtracao

## MULTIPLICAÇÃO
### PROMPT: crie uma variável chamada "multiplicacao" e guarde o resultado de num1 * num2
### PROMPT: mostre na tela o resultado de multiplicacao

## DIVISÃO
### PROMPT: crie uma variável chamada "divisao" e guarde o resultado de num1 / num2
### PROMPT: mostre na tela o resultado de divisao

## DIVISÃO INTEIRA
### PROMPT: crie uma variável chamada "divisao_inteira" e guarde o resultado de num1 // num2
### PROMPT: mostre na tela o resultado de divisao_inteira

## RESTO DA DIVISÃO
### PROMPT: crie uma variável chamada "resto" e guarde o resultado de num1 % num2
### PROMPT: mostre na tela o resultado de resto

## POTÊNCIA
### PROMPT: crie uma variável chamada "potencia" e guarde o resultado de num1 ** num2
### PROMPT: mostre na tela o resultado de potencia

## MAIOR QUE
### PROMPT: crie uma variável chamada "maior" e guarde o resultado de num1 > num2
### PROMPT: mostre na tela o resultado de maior

## MENOR QUE
### PROMPT: crie uma variável chamada "menor" e guarde o resultado de num1 < num2
### PROMPT: mostre na tela o resultado de menor

## IGUAL A
### PROMPT: crie uma variável chamada "igual" e guarde o resultado de num1 == num2
### PROMPT: mostre na tela o resultado de igual

## DIFERENTE DE
### PROMPT: crie uma variável chamada "diferente" e guarde o resultado de num1 != num2
### PROMPT: mostre na tela o resultado de diferente

## MAIOR OU IGUAL A
### PROMPT: crie uma variável chamada "maior_igual" e guarde o resultado de num1 >= num2
### PROMPT: mostre na tela o resultado de maior_igual

## MENOR OU IGUAL A
### PROMPT: crie uma variável chamada "menor_igual" e guarde o resultado de num1 <= num2
### PROMPT: mostre na tela o resultado de menor_igual

## E OU
### PROMPT: crie uma variável chamada "ou" e guarde o resultado de num1 > num2 or num1 < num2
### PROMPT: mostre na tela o resultado de ou

## E E
### PROMPT: crie uma variável chamada "e" e guarde o resultado de num1 > num2 and num1 < num2
### PROMPT: mostre na tela o resultado de e

## NÃO
### PROMPT: crie uma variável chamada "nao" e guarde o resultado de not num1 > num2
### PROMPT: mostre na tela o resultado de nao

## PRATICANDO

## Vamos fazer uma calculadora que some dois números:
## PROMPT: crie uma variável chamada "num1" e guarde o número 10
## PROMPT: crie uma variável chamada "num2" e guarde o número 5
## PROMPT: some as duas variáveis e guarde o resultado em uma variável chamada "soma"
## PROMPT: mostre na tela o resultado

## Vamos calcular a área de um retângulo:
## PROMPT: crie uma variável chamada "base" e guarde o número 10
## PROMPT: crie uma variável chamada "altura" e guarde o número 5
## PROMPT: calcule a área multiplicando a base pela altura e guarde em uma variável chamada "area"
## PROMPT: mostre na tela o resultado

# 3. CONDICIONAIS

"""
CONDICIONAIS são como decisões no código:
- Se algo é verdadeiro, faça isso
- Se não, faça aquilo
- Podemos ter várias condições
- Usamos operadores de comparação
"""

## Operações úteis com condicionais, seguindo o modelo:

## IF SIMPLES
### PROMPT: verifique se um número é positivo

## IF/ELSE
## Vamos verificar se um número é par ou ímpar
## PROMPT: crie uma variável chamada "numero" e guarde o número 10
## PROMPT: verifique se o número é par ou ímpar e mostre na tela o resultado

## IF/ELIF/ELSE
## Vamos fazer um programa que diga se está quente ou frio ou agradável
## PROMPT: crie uma variável chamada "temperatura" e guarde o número 25
## PROMPT: classifique a temperatura entre frio, agradável e quente

## IF ANINHADO
### PROMPT: verifique idade e se for maior de 18, verifique se tem carteira de motorista, se não tem, mostre que não pode dirigir

## OPERADORES LÓGICOS
### PROMPT: verifique se um número está entre 1 e 10

# 4. LOOPS

"""
LOOPS repetem um bloco de código várias vezes no código:
- Fazem a mesma coisa várias vezes
- Úteis para tarefas repetitivas
- Dois tipos principais: while e for
- While: repete enquanto uma condição for verdadeira
- For: repete um número específico de vezes
"""


## WHILE SIMPLES
### PROMPT: conte de 1 a 5 usando while

## FOR SIMPLES
### PROMPT: conte de 1 a 5 usando for

## BREAK
### PROMPT: pare o loop quando chegar no número 3

## CONTINUE
### PROMPT: pule o número 3 no loop

## LOOP ANINHADO
### Vamos fazer uma tabuada do 1 ao 3
### PROMPT: crie uma variável chamada "numero" e guarde o número 1
### PROMPT: use um while para repetir a tabuada do número até 3

## Vamos fazer um programa que some os números de 1 a 10
## PROMPT: crie uma variável chamada "soma" e guarde o número 0
## PROMPT: use um loop para somar os números de 1 a 10 e mostre na tela o resultado

# Vamos ver um exemplo da utilidade de aprender algoritmos
# no exemplo acima, se eu quiser somar os números de 1 a 1000000,
# eu posso usar um loop, mas demora muito, e o computador fica muito ocupado
# então eu posso usar um algoritmo que é mais eficiente, e faz a mesma coisa
# em um tempo muito menor, e o computador fica mais feliz
# esse algoritmo é o "soma de Gauss", ele descobre quantos números tem na sequência
# e multiplica pelo número do meio, e divide por 2, e dá no mesmo resultado
# então aprender algoritmos é muito importante, 
# pois são soluções eficientes para problemas conhecidos
# e nos ajuda a otimizar o nosso código e não reinventar a roda
## PROMPT: crie uma variável chamada "n" e guarde o número 1000000
## PROMPT: use o algoritmo de Gauss para somar os números de 1 a n
## PROMPT: mostre na tela o resultado

# 5. FUNÇÕES

"""
FUNÇÕES são blocos de código reutilizáveis:
- Organizam o código em partes menores
- Podem receber dados (parâmetros)
- Podem retornar resultados
- Evitam repetição de código
- Tornam o código mais legível
"""

## FUNÇÃO SIMPLES
### PROMPT: crie uma função que imprime "Olá!"

## FUNÇÃO COM PARÂMETRO
### PROMPT: crie uma função que recebe um nome e imprime "Olá, nome!"

## FUNÇÃO COM RETORNO
### PROMPT: crie uma função que recebe dois números e retorna a soma

## FUNÇÃO COM MÚLTIPLOS PARÂMETROS
### PROMPT: crie uma função que recebe nome e idade e imprime "Nome tem idade anos"

## FUNÇÃO COM VALOR PADRÃO
### PROMPT: crie uma função que recebe um nome (padrão "Anônimo") e imprime "Olá, nome!"

## FUNÇÃO COM MÚLTIPLOS RETORNOS
### PROMPT: crie uma função que recebe um número e retorna seu dobro e seu triplo



## Vamos fazer uma função que calcula o desconto em uma compra
## PROMPT: crie uma função chamada "calcular_desconto" que recebe o valor total da compra
## PROMPT: aplique as regras de desconto:
##   - Compras até R$100: sem desconto
##   - Compras de R$100 até R$200: 10% de desconto
##   - Compras de R$200 até R$500: 15% de desconto
##   - Compras acima de R$500: 20% de desconto
## PROMPT: calcule e retorne o valor final com desconto
## PROMPT: mostre na tela o valor original, o desconto aplicado e o valor final
## PROMPT: use a função para calcular o desconto de uma compra de R$150

## Vamos fazer uma função que calcula a média de notas de um aluno
## PROMPT: crie uma função chamada "calcular_media" que recebe as notas de um aluno
## PROMPT: calcule e retorne a média das notas
## PROMPT: mostre na tela a média
## PROMPT: use a função para calcular a média de um aluno que tirou 10, 8, 9

# 6. TRATAMENTO DE ERROS

"""
TRATAMENTO DE ERROS ajuda a lidar com problemas:
- Previne que o programa pare de funcionar
- Permite mostrar mensagens amigáveis
- Garante que dados inválidos sejam tratados
- Torna o programa mais robusto
"""

## ERRO SIMPLES
### PROMPT: tente dividir um número por zero e trate o erro

## MÚLTIPLOS ERROS
### PROMPT: trate diferentes tipos de erro em um mesmo bloco

## ERRO ESPECÍFICO
### PROMPT: trate apenas um tipo específico de erro

## ERRO COM ELSE
### PROMPT: use o else quando não houver erro

## ERRO COM FINALLY
### PROMPT: use o finally para executar código sempre

## CRIAR ERRO
### PROMPT: crie e lance seu próprio erro com raise

## VERIFICAR TIPO
### PROMPT: verifique o tipo do erro capturado

## Vamos fazer um programa que pede um número e mostra o seu dobro
## PROMPT: crie uma função chamada "pedir_numero" que pede um número ao usuário
## PROMPT: use um try-except para tratar o erro de entrada inválida (por exemplo, uma letra)
## PROMPT: mostre na tela a mensagem de erro
## PROMPT: use a função para pedir um número e mostrar o seu dobro

# 7. Juntando tudo

## Vamos fazer um jogo de adivinhação de número passo a passo
"""
crie uma função chamada "jogo_adivinhacao", dentro da função:
    crie uma variável chamada "numero_secreto" que recebe um número aleatório entre 1 e 3
    enquanto o usuário não acertar o número secreto:
        crie uma variável chamada "chute" que recebe um número digitado pelo usuário
        verifique se o chute é um número válido
        se nao for, mostre na tela "Você precisa digitar um número!"
        se for, verifique se o chute é igual ao número secreto
            se for, mostre na tela "Você acertou!"
            se não for, mostre na tela "Você errou!"
            mostre na tela o número secreto e o chute
            e pergunte se o usuário quer continuar jogando
            se sim, volta pro começo do loop
            se não, mostre na tela "Obrigado por jogar!"
                e termine a função
chame a função para jogar o jogo
"""

