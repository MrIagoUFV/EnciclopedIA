"""
MANIPULAÇÃO DE DADOS E ARQUIVOS

Imagine que você está organizando seus arquivos no computador:
- Você tem diferentes tipos de arquivos (word -> docx, excel -> xlsx, bloco de notas -> txt)
- Cada tipo tem seu próprio formato e uso
- Você consegue ler, escrever e manipular esses arquivos
- E pode manter os dados salvos mesmo depois de fechar o programa e desligar o computador

Em python podemos fazer a mesma coisa com esses arquivos, 
só que ao invés de fazer isso manualmente, 
vamos usar o computador para fazer isso automaticamente.
"""

"""
A manipulação de arquivos em python é bem simples, 
só precisamos conhecer quais são os tipos de arquivos que podemos manipular 
e como o python nos permite manipular cada tipo de arquivo.

1. ARQUIVOS DE TEXTO são como cadernos:
   - Salvam texto puro linha por linha
   - Fáceis de ler e editar
   - Bons para logs e anotações simples
   
2. ARQUIVOS JSON são como fichas organizadas:
   - Salvam dados estruturados
   - Fáceis de ler por humanos e máquinas
   - Ótimos para configurações e dados complexos

3. ARQUIVOS CSV são como planilhas:
   - Salvam dados em formato tabular
   - Podem ser abertos no Excel
   - Perfeitos para dados em forma de tabela

Parece complicado...
Mas você só precisa entender quando usar cada formato
e as operações básicas de leitura e escrita.
"""


"""
1. ARQUIVOS DE TEXTO

Arquivos de texto (.txt) são os mais simples de manipular.
São como um caderno digital onde podemos:
- Escrever texto linha por linha
- Ler todo conteúdo de uma vez
- Adicionar mais conteúdo ao final
- Ler linha por linha

Principais operações:
- Abrir arquivo: open("arquivo.txt", modo)
  - modo "w": escrita (apaga conteúdo)
  - modo "r": leitura
  - modo "a": adicionar ao final
- Ler conteúdo: read() ou readlines()
- Escrever: write() ou writelines() 
- Fechar: close()

O mais seguro é usar with que fecha automaticamente:
with open("arquivo.txt", "w") as arquivo:
    arquivo.write("texto")
"""

## Operações úteis com Arquivos de Texto, seguindo o modelo:

## CRIAR E ESCREVER
### PROMPT: crie um arquivo notas.txt e escreva "Primeira nota" nele

## LER TUDO
### PROMPT: leia e mostre todo conteúdo do arquivo notas.txt

## ADICIONAR LINHA
### PROMPT: adicione "Segunda nota" em uma nova linha no arquivo

## LER LINHA A LINHA  
### PROMPT: leia e mostre cada linha do arquivo separadamente

## ESCREVER LISTA
### PROMPT: escreva uma lista de strings como linhas no arquivo

## COPIAR ARQUIVO
### PROMPT: copie o conteúdo de um arquivo para outro

## VERIFICAR EXISTÊNCIA
### PROMPT: verifique se um arquivo existe antes de abrir

## DELETAR ARQUIVO
### PROMPT: delete um arquivo do sistema

"""
2. ARQUIVOS JSON

JSON (JavaScript Object Notation) é um formato que salva dados estruturados de forma organizada.
É muito usado principalmente para APIs da web, ou seja, para troca de dados entre sistemas.

Principais características:
- Fácil de ler por humanos e máquinas
- Suporta dados aninhados (dicionários dentro de dicionários)
- Tipos de dados: strings, números, booleanos, null, arrays e objetos
- Formato universal que qualquer linguagem entende
"""

## Operações úteis com JSON, seguindo o modelo:

## CRIAR E SALVAR
### PROMPT: crie um dicionário com dados de uma pessoa (nome, idade e cidade) e salve em um arquivo pessoas.json

## LER ARQUIVO
### PROMPT: leia e mostre os dados do arquivo pessoas.json

## ADICIONAR DADOS
### PROMPT: adicione mais uma pessoa ao arquivo pessoas.json

## ATUALIZAR DADOS
### PROMPT: altere a idade de uma pessoa no arquivo pessoas.json

## DELETAR DADOS
### PROMPT: remova uma pessoa do arquivo pessoas.json

## BUSCAR DADOS
### PROMPT: procure e mostre os dados de uma pessoa específica no arquivo

## VALIDAR JSON
### PROMPT: verifique se uma string está em formato JSON válido

## FORMATAR JSON
### PROMPT: salve um JSON de forma indentada e legível

"""
3. ARQUIVOS CSV

CSV (Comma-Separated Values) é um formato que organiza dados em forma de tabela,
como uma planilha do Excel. Cada linha representa um registro e as colunas são
separadas por vírgulas.

Principais características:
- Formato simples e leve para dados tabulares
- Pode ser aberto em editores de planilha como Excel e Google Sheets
- Suporta dados em formato de lista ou dicionário
- Muito usado para importar/exportar dados

Operações principais:
- Criar e escrever dados em CSV
- Ler dados de um CSV existente 
- Trabalhar com cabeçalhos (colunas)
- Manipular como lista ou dicionário
"""

## Operações úteis com CSV, seguindo o modelo:

## CRIAR CSV SIMPLES
### PROMPT: crie um arquivo notas.csv com nome e nota de 3 alunos

## LER CSV SIMPLES
### PROMPT: leia e mostre os dados do arquivo notas.csv linha por linha

## ADICIONAR DADOS
### PROMPT: adicione mais um aluno e sua nota ao arquivo notas.csv

## CRIAR COM CABEÇALHO
### PROMPT: crie um arquivo funcionarios.csv com colunas: nome, cargo e salário

## LER COM CABEÇALHO
### PROMPT: leia o arquivo funcionarios.csv e mostre como dicionário

## FILTRAR DADOS
### PROMPT: mostre apenas funcionários com salário acima de 5000

## ATUALIZAR DADOS
### PROMPT: atualize o salário de um funcionário específico

## CALCULAR TOTAL
### PROMPT: some o total de salários de todos funcionários

## EXPORTAR SELEÇÃO
### PROMPT: crie um novo CSV só com funcionários de um cargo específico

## VALIDAR DADOS
### PROMPT: verifique se todas as linhas têm o número correto de colunas

"""
DICAS IMPORTANTES:

1. Sempre use 'with' para abrir arquivos
   - Fecha automaticamente mesmo com erros
   - Evita problemas de memória

2. Escolha o formato certo:
   - Texto: dados simples, logs
   - JSON: dados estruturados, configs
   - CSV: dados tabulares, planilhas

3. Trate erros ao manipular arquivos:
   - Arquivo pode não existir
   - Formato pode estar inválido
   - Permissões podem ser negadas

4. Faça backup antes de modificar
   - Dados são importantes
   - Erros podem corromper arquivos
   - Melhor prevenir que remediar
"""
