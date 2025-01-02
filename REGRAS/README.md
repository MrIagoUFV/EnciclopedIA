# MODELO GERAL - NEXTJS 14


```markdown
REGRAS PARA DESENVOLVER EM NEXJS:

Responda sempre em português brasil

# Regras para seguir em cada ação do agente de desenvolvimento.

Sempre procure na documentação relevante antes de executar qualquer comando ou editar qualquer arquivo.

use comandos do powershell para comandos no terminal

Ao criar ou editar um page.tsx:
- Declare todos os tipos explicitamente no arquivo (não crie um arquivo separado para os tipos)
- Não reinvente a roda, use componentes do shadcn em /components/ui, e se não houver, procure em outras bibliotecas, somente se ainda não houver, crie em /components.
- Crie toda a lógica relacionada no arquivo (não crie um arquivo separado em hooks)
- Use zustand para gerenciar estado e crie a store no arquivo (não crie um arquivo separado em store)
Não modularizar essas partes é benéfico nesse contexto pois estamos programando com AI Copilots, e ter tudo no mesmo arquivo ajuda a centralizar todo contexto necessário e evita duplicação de código.

- DRY o estilo usando todas as classes e estilos importando do @globals.css e tailwind.config.ts

Erros, dependências e outras coisas que são resolvidas por comando no terminal (ex. npm install), execute o comando (não crie ou modifique os arquivos manualmente nesses casos)

# Pontos de atenção:

Criando projeto em Nextjs 14 com app router, typescript
- Já executei criei o projeto nextjs na raiz (executei: npx create-next-app@14 .)
- Já instalei o zustand (executei: npm install zustand)
- Já instalei o shadcn e todos seus componentes em /components/ui  (instalei com npx shadcn@latest init -d; npx shadcn@latest add --all)

Já estamos na raiz do projeto,
crie os page.tsx em /src/app/
crie os componentes em /src/componentes

ANALISE AS REGRAS ACIMA E O PROJETO E ESTRUTURA INICIAL ABAIXO:

```