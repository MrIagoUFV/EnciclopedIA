"""
INTRODUÇÃO À ESTRUTURAS DE DADOS COM PYTHON

Imagine que você está organizando uma festa:

- Você tem uma LISTA de convidados em ordem de chegada
- Cada convidado tem suas informações (nome, idade, preferências)
- Alguns dados não podem mudar, como CPF
"""

"""
É assim que organizamos dados no Python!

Ao criar aplicações mais complexas, 
você vai precisar armazenar e organizar dados de forma mais eficiente.
Existem estruturas de dados que nos permitem guardar 
os tipos de dados que vimos, em conjunto, 
sem precisar criar uma variável para cada um.
"""

"""
1. LISTAS

Imagine que você precise guardar uma lista de compras ou uma lista de nomes...
Podemos usar uma LISTA para isso!
As listas são a estrutura mais básica de dados em Python.
 - Guardam itens em sequência
 - Cada item tee uma posição (índice) sendo a primeira posição o 0
 - Podemos adicionar/mover/remover/editar itens da lista
"""


# 1. LISTAS BÁSICAS

## CRUD - Create, Read, Update, Delete

### CRIAR (Create)
#### PROMPT: Crie uma lista de compras com: arroz, feijão, macarrão, açúcar 

### ADICIONAR (Create)
#### PROMPT: Adicione um produto: café

### ACESSAR (Read)
## PROMPT: Acesse o primeiro produto

### ATUALIZAR (Update)
## PROMPT: Mude o nome do primeiro produto para 'arroz integral'

### REMOVER (Delete)
## PROMPT: Remova o último produto

## Outras operações úteis com listas:

### MEDIR
#### PROMPT: Verificar tamanho da lista

### VERIFICAR
#### PROMPT: Verificar se item existe na lista

### ORDENAR
#### PROMPT: Ordenar lista (altera a lista original)

### INVERTER
#### PROMPT: Inverter lista

### ENCONTRAR ÍNDICE
#### PROMPT: Encontrar índice de um item

### CONTAR OCORRÊNCIAS
#### PROMPT: Contar ocorrências de um item

### COPIAR
#### PROMPT: Copiar lista (cria uma nova lista independente)

### LIMPAR
#### PROMPT: Limpar lista



"""

2. DICIONÁRIOS 
Os dicionários guardam dados em pares, 
igual num dicionário mesmo (palavras e definições),
Só que no python, podemos guardar qualquer tipo de dado:
   - Cada informação tem um nome (chave)
   - Cada chave tem um valor
   - Exemplo: dados_joao = {'nome': 'João', 'idade': 25}
"""

# 2. DICIONÁRIOS BÁSICOS

## CRUD - Create, Read, Update, Delete

### CRIAR (Create)
#### PROMPT: Crie um dicionário chamado 'dados' com: nome = 'Iago', idade = 24, cidade = 'Viçosa'

### ADICIONAR (Create)
#### PROMPT: Adicione um novo campo: 'altura' = 1.84

### ACESSAR (Read) 
#### PROMPT: Acesse o valor de 'idade'

### ATUALIZAR (Update)
#### PROMPT: Atualize o valor de 'idade' para 2

### REMOVER (Delete)
#### PROMPT: Remova o campo 'altura'

## Outras operações específicas dos dicionários:

### OBTER TODAS AS CHAVES
#### PROMPT: Mostrar todas as chaves do dicionário

### OBTER TODOS OS VALORES
#### PROMPT: Mostrar todos os valores do dicionário

### OBTER PARES CHAVE-VALOR
#### PROMPT: Mostrar todos os pares chave-valor

### VERIFICAR SE CHAVE EXISTE
#### PROMPT: Verificar se uma chave existe no dicionário

### VALOR PADRÃO
#### PROMPT: Pegar valor com padrão se não existir

### ATUALIZAR MÚLTIPLOS
#### PROMPT: Atualizar vários valores de uma vez

### COPIAR DICIONÁRIO
#### PROMPT: Criar uma cópia independente

### LIMPAR DICIONÁRIO
#### PROMPT: Remover todos os itens


# 3. TUPLAS

"""
Tuplas são sequências imutáveis que podem conter elementos de diferentes tipos.
São úteis quando precisamos garantir que os dados não serão alterados acidentalmente.
"""

## CRIAR TUPLA
### PROMPT: Criar uma tupla com coordenadas (x,y)

## ACESSAR ELEMENTOS
### PROMPT: Acessar o valor de x e y

## DESEMPACOTAMENTO
### PROMPT: Extrair valores para variáveis

## CONCATENAR
### PROMPT: Juntar duas tuplas

## REPETIR
### PROMPT: Repetir uma tupla

## VERIFICAR ELEMENTO
### PROMPT: Verificar se valor existe na tupla

## COMPRIMENTO
### PROMPT: Obter tamanho da tupla

## CONVERTER LISTA PARA TUPLA
### PROMPT: Transformar uma lista em tupla

## ÍNDICE DE ELEMENTO
### PROMPT: Encontrar posição de um valor

## CONTAR OCORRÊNCIAS
### PROMPT: Contar quantas vezes um valor aparece

## TENTAR MUDAR VALOR
### PROMPT: Tentar mudar valor de uma tupla (vai dar erro)