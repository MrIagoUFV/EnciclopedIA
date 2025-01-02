# Modelos
 Moldes para acelerar as configurações iniciais

### CONFIGURAÇÕES INICIAIS

> npm install zustand

> npx shadcn@latest init -d

> npx shadcn@latest add --all

### INSTALAR O PYTHON

- [x] ADD TO PATH

### INSTALAR O GPTREE

(WINDOWS)
>  pip install pyreadline3

>  pip install windows-curses

(TODOS)

>  pip install gptree-cli

---
<br><br><br>
---

### Sobre o GPTree

[gptree](https://github.com/travisvn/gptree)

![GPTree Demo](https://github.com/travisvn/gptree/raw/main/demo.gif)

O GPTree é uma ferramenta CLI (Command Line Interface) que ajuda a fornecer contexto de projetos de código para LLMs (Large Language Models).

#### O que ele faz

- Gera uma estrutura de diretório em árvore do seu projeto
- Combina o conteúdo dos arquivos relevantes em um único arquivo de texto
- Permite selecionar arquivos interativamente
- O resultado pode ser facilmente copiado e colado em prompts de LLMs

#### Uso Básico

Para usar na forma mais simples, basta executar no diretório do seu projeto:

#### Principais Opções

> -i    			: Permite selecionar arquivos interativamente

> -c    			: Copia o resultado para a área de transferência

> -p    			: Usa a seleção anterior de arquivos

> -s    			: Salva a seleção atual para uso futuro

> -dsm  			: Para copiar muitos tokens

> --include-file-types	: Lista de tipos de arquivo para incluir (ex: .py,.js)

> --exclude-file-types	: Lista de tipos de arquivo para excluir


No modo interativo (`-i`), você pode:
- Usar ↑/↓ para navegar
- ESPAÇO para selecionar/deselecionar arquivos
- 'a' para selecionar/deselecionar todos
- ENTER para confirmar
- ESC para sair

##### Exemplos Práticos

1. Seleção interativa com tipos específicos:
> gptree -i --include-file-types '.py,.js'

2. Salvar seleção atual:
> gptree -i --s

3. Reutilizar seleção anterior e copiar:
> gptree -p -c
