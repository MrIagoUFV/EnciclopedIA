"""
INTRODUÇÃO À PROGRAMAÇÃO ORIENTADA A OBJETOS (POO)

* EXPLICAÇÃO SIMPLIFICADA *

É um novo jeito de pensar na hora de programar, 
que pode nos ajudar a organizar o código,
e economizar muitas linhas.

Imagine que você está criando um programa para dirigir carros automatizados:

imagine que você tenha 1 carro inicialmente.

Você precisa definir as funções dele:

Carro simples 1:
- Ligar o carro
- Acelerar
- Frear
- Dar ré
- Ligar o farol
- Desligar o farol
- Buzinar
- Desligar o carro

Carro comum 1:
- Ligar o carro
- Acelerar
- Frear
- Dar ré
- Ligar o farol
- Desligar o farol
- Buzinar
- Desligar o carro
-- Ligar o rádio
-- Desligar o rádio

Carro turbo 1:
- Ligar o carro
- Acelerar
- Frear
- Dar ré
- Ligar o farol
- Desligar o farol
- Buzinar
- Desligar o carro
-- Ligar o rádio
-- Desligar o rádio
-- Ligar o turbo
-- Desligar o turbo

olha a bagunça que o código vai ficando...
imagina se eu quiser criar mais 100 carros...

POO é uma forma de organizar o código,
de forma que você define o que cada tipo de carro tem em comum apenas uma vez,
e durante o código, você pode utilizar tudo que foi definido, 
sem precisar repetir o código.

Nesse exemplo, você criaria uma classe Carro, 
Ela serviria de molde para contruir quantos carros você quiser,
e cada carro criado seguirá o molde que você definiu dentro da classe.

Então você teria algo tipo assim:

class Carro_Simples():
  # o que todo carro tem em comum
  - cor
  - Ligar o carro
  - Acelerar
  - Frear
  - Dar ré
  - Ligar o farol
  - Desligar o farol
  - Buzinar
  - Desligar o carro

class Carro_Comum(Carro_Simples):
  # o carro comum tem tudo do carro simples,
  # mas também tem:
  - Ligar o rádio
  - Desligar o rádio

class Carro_Turbo(Carro_Comum):
  # o carro turbo tem tudo do carro comum,
  # mas também tem:
  - Ligar o turbo
  - Desligar o turbo

# Agora, eu posso criar quantos carros eu quiser,

carro_simples_1 = Carro_Simples()
carro_simples_2 = Carro_Simples()
carro_simples_3 = Carro_Simples()
carro_comum_1 = Carro_Comum()
carro_comum_2 = Carro_Comum()
carro_turbo_1 = Carro_Turbo()
carro_turbo_2 = Carro_Turbo()
carro_turbo_3 = Carro_Turbo()
carro_turbo_4 = Carro_Turbo()
carro_turbo_5 = Carro_Turbo()
carro_comum_3 = Carro_Comum()
carro_comum_4 = Carro_Comum()
carro_comum_5 = Carro_Comum()
carro_comum_6 = Carro_Comum()
carro_comum_7 = Carro_Comum()
carro_simples_4 = Carro_Simples()
carro_simples_5 = Carro_Simples()
carro_simples_6 = Carro_Simples()
carro_simples_7 = Carro_Simples()
carro_simples_8 = Carro_Simples()
carro_simples_9 = Carro_Simples()
carro_simples_10 = Carro_Simples()
carro_comum_8 = Carro_Comum()
carro_comum_9 = Carro_Comum()
carro_comum_10 = Carro_Comum()
carro_turbo_6 = Carro_Turbo()
carro_turbo_7 = Carro_Turbo()


# E podemos personalizar as características de cada carro, dado tudo que ele tem.
# Então eu posso pegar o carro_turbo_1 por exemplo, e mudar algumas coisas específicas pra ele:

carro_turbo_1.cor = "azul"
carro_turbo_1.buzinar()

# e assim por diante.

Agora a gente vai ver isso na prática nessa aula,
com casos reais de POO.

"""

# 80/20 - AQUILO QUE REALMENTE IMPORTA APRENDER AGORA

"""
1. CLASSES E OBJETOS

Uma classe é como um 'molde'

Pense num castelo de areia feito com um molde.
O molde define como é feito o castelo,
Depois de construir o molde, eu posso usar ele quantas vezes eu quiser,
pra criar quantos castelos eu quiser.

O molde é o que a gente chama de classe, 
e cada castelo criado com ele a gente chama de uma instância do molde, 
ou seja, um objeto.

"""

## Operações úteis com Classes e Objetos:

## CLASSE SIMPLES
### PROMPT: crie uma classe chamada "Livro"

## ATRIBUTOS
### PROMPT: adicione atributos titulo, autor e paginas na classe Livro

## CONSTRUTOR
### PROMPT: crie um construtor que recebe titulo, autor e paginas

## MÉTODOS
### PROMPT: adicione um método ler() que imprime "Lendo o livro!"

## CRIAR OBJETO
### PROMPT: crie um objeto da classe Livro chamado "harry_potter"

## ACESSAR ATRIBUTOS
### PROMPT: mostre o titulo e autor do harry_potter

## CHAMAR MÉTODO
### PROMPT: faça o harry_potter ser lido

"""
2. HERANÇA

Herança permite que uma classe herde atributos
e métodos de outra classe.

Exemplo: 
- Classe Item (pai)
- Classe Livro (filho)
"""

## Operações úteis com Herança, seguindo o modelo:

## CLASSE PAI
### PROMPT: crie uma classe chamada "Item" com atributos titulo e preco, e um método descricao()

## CLASSE FILHA
### PROMPT: crie uma classe "Livro" que herda de "Item"

## SUPER
### PROMPT: use super() para chamar o construtor da classe pai e adicione o atributo autor

## SOBRESCRITA
### PROMPT: sobrescreva o método descricao() na classe Livro para retornar "Livro: {titulo}"


"""
3. POLIMORFISMO

Polimorfismo permite que objetos de diferentes classes
sejam tratados de maneira uniforme.

Exemplo: diferentes itens, mesmo método descricao()
"""

## Operações úteis com Polimorfismo, seguindo o modelo:

## MÉTODO COMUM
### PROMPT: crie um método descricao() nas classes Livro e Revista

## LISTA POLIMÓRFICA
### PROMPT: crie uma lista com diferentes itens

## LOOP POLIMÓRFICO
### PROMPT: faça um loop chamando descricao() de cada item


"""
4. MÉTODOS ESPECIAIS

Métodos especiais (magic methods) personalizam
comportamento de objetos.
"""

## Operações úteis com Métodos Especiais, seguindo o modelo:

## STR
### PROMPT: implemente __str__ para representação em string

## LEN
### PROMPT: implemente __len__ para retornar tamanho

## EQUALS
### PROMPT: implemente __eq__ para comparar objetos

## REPR
### PROMPT: implemente __repr__ para representação detalhada


#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#

# A parte acima é o 80/20 de POO. Aquilo que realmente importa saber agora no início do curso.

# Ver o restante dos conceitos agora só bagunçaria sua cabeça sem necessidade.
# Deixa pra aprender esse resto na prática, quando for necessário, SE for necessário:

"""
5. ENCAPSULAMENTO

Encapsulamento protege os dados dentro da classe
usando modificadores de acesso:
- público: acessível de qualquer lugar
- privado: acessível só dentro da classe
"""

## Operações úteis com Encapsulamento, seguindo o modelo:

## ATRIBUTO PRIVADO
### PROMPT: crie uma classe Livro com um atributo privado _isbn

## GETTER
### PROMPT: crie um método para acessar o atributo privado

## SETTER
### PROMPT: crie um método para modificar o atributo privado

## VALIDAÇÃO
### PROMPT: adicione validação no setter do isbn


"""
6. ABSTRAÇÃO

Abstração é esconder complexidade e mostrar apenas
o necessário. Usamos classes abstratas como 'modelos'.
"""

## Operações úteis com Abstração, seguindo o modelo:

## CLASSE ABSTRATA
### PROMPT: crie uma classe abstrata ItemBiblioteca com método emprestar()

## IMPLEMENTAÇÃO
### PROMPT: crie classes Livro e Revista que implementam emprestar()

## INTERFACE
### PROMPT: crie uma interface Catalogavel com método catalogar()


"""
7. COMPOSIÇÃO

Composição é criar objetos que contêm outros objetos.
É uma relação "tem um".
"""

## Operações úteis com Composição, seguindo o modelo:

## CLASSE COMPONENTE
### PROMPT: crie uma classe Capitulo

## CLASSE COMPOSTA
### PROMPT: crie uma classe Livro que tem vários Capitulos

## AGREGAÇÃO
### PROMPT: crie uma classe Biblioteca que tem vários Livros

"""
8. PROPRIEDADES

Propriedades permitem controlar acesso a atributos
de forma elegante.
"""

## Operações úteis com Propriedades, seguindo o modelo:

## PROPERTY
### PROMPT: crie uma property para acessar um atributo privado

## SETTER PROPERTY
### PROMPT: crie um setter com validação usando property

## DELETAR PROPERTY
### PROMPT: crie um deleter para uma property
