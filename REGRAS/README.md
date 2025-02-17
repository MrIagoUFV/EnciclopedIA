# REGRAS

## GERAL

IDEIA GERAL DA REGRA QUE AJUDA A CONTROLAR O FLUXO (N DEIXA A IA SAIR CRIANDO TROCENTOS ARQUIVOS)

```
# REGRAS PARA SEGUIR EM CADA MÍNIMA AÇÃO

Responda sempre em português brasil

Ao criar ou editar um arquivo trabalhe sempre de forma desmodularizada (tudo centralizado em um único arquivo):
- Declare todos os tipos explicitamente no arquivo.
- Crie toda a lógica hook relacionada no arquivo.
- Crie todas as funções utilitárias específicas dentro do próprio arquivo.
- Crie todos os Server Actions específicos dentro do próprio arquivo.

- Não reinvente a roda, use componentes de bibliotecas, somente se ainda não houver, crie.
- Para typescript, Use zustand para gerenciar estado e crie a store no arquivo (não crie um arquivo separado em store)
- use a pasta /api/ para routes apenas quando necessário.

Trabalhar assim é benéfico nesse contexto pois estamos programando com AI Copilots, e ter tudo no mesmo arquivo ajuda a centralizar todo contexto necessário e evita duplicação de código.

# FLUXO OBRIGATÓRIO DE DESENVOLVIMENTO

PRIMEIRO:
- Se for modificar arquivos, confira antes quais arquivos serão modificados, e para cada um, liste quais trechos, estilos e funcionalidades devem permanecer imutáveis para manter a integridade do código.

SEGUNDO:
- Após o estudo, passe para a fase da analise dos passos. Pois pode ser uma ação grande que seja melhor quebrar em menores passos para manter a integridade do código, e garantir que faça o todo bem feito, danda a atenção necessário a cada passo. Analise e exponha seu plano.

TERCEIRO:
1. Decida o melhor primeiro passo e peça permissão. Espere o ok do usuário, e faça.
2. Decida o melhor segundo passo, analise o que deve permanecer imutável. Espere o ok do usuário, e faça.
3. ... por aí vai, obrigatoriamente parando e pedindo permissão para continuar para o próximo, explicitando qual será. Espere a permissão do usuário.

# PONTOS DE ATENÇÃO

- DRY o estilo usando todas as classes e estilos importando do mesmo arquivo de estilos do projeto.

- Faça apenas uma ação por vez.

ANALISE AS REGRAS ACIMA E FAÇA O QUE SE PEDE:

```


## Nextjs

```markdown
# REGRAS PARA SEGUIR EM CADA MÍNIMA AÇÃO

Responda sempre em português brasil

Ao criar ou editar um page.tsx:
- Declare todos os tipos explicitamente no arquivo (não crie um arquivo separado para os tipos)
- Não reinvente a roda, use componentes do shadcn em /components/ui, e se não houver, procure em outras bibliotecas, somente se ainda não houver, crie em /components.
- Crie toda a lógica hook relacionada "use..." no arquivo (não crie um arquivo separado em hooks)
- Crie todas as funções utilitárias específicas dentro do próprio arquivo (não crie em lib/)
- Crie todos os Server Actions específicos dentro do próprio arquivo (não crie em actions/)
- Use zustand para gerenciar estado e crie a store no arquivo (não crie um arquivo separado em store)
- use a pasta /api/ para routes apenas quando necessário.

Nunca modularizar essas partes: (tipos, hooks, funções utilitárias, server actions e stores) é benéfico nesse contexto pois estamos programando com AI Copilots, e ter tudo no mesmo arquivo ajuda a centralizar todo contexto necessário e evita duplicação de código. Nunca crie pasta hooks.

# FLUXO OBRIGATÓRIO DE DESENVOLVIMENTO

PRIMEIRO:
- Se for modificar arquivos, confira antes quais arquivos serão modificados, e para cada um, liste quais trechos, estilos e funcionalidades devem permanecer imutáveis para manter a integridade do código.

SEGUNDO:
- Após o estudo, passe para a fase da analise dos passos. Pois pode ser uma ação grande que seja melhor quebrar em menores passos para manter a integridade do código, e garantir que faça o todo bem feito, danda a atenção necessário a cada passo. Analise e exponha seu plano.

TERCEIRO:
1. Decida o melhor primeiro passo e peça permissão. Espere o ok do usuário, e faça.
2. Decida o melhor segundo passo, analise o que deve permanecer imutável. Espere o ok do usuário, e faça.
3. ... por aí vai, obrigatoriamente parando e pedindo permissão para continuar para o próximo, explicitando qual será. Espere a permissão do usuário.

# REGRAS DURANTE TODO O FLUXO DE DESENVOLVIMENTO

- DRY o estilo usando todas as classes e estilos importando do @globals.css e @tailwind.config.ts

# PONTOS DE ATENÇÃO

Criando projeto em Nextjs 14 com app router, typescript
- Já executei criei o projeto nextjs na raiz (executei: npx create-next-app@14 .)
- Já instalei o zustand (executei: npm install zustand)
- Já instalei o shadcn e todos seus componentes em /components/ui  (instalei com npx shadcn@latest init -d; npx shadcn@latest add --all)
- Para comandos do terminal, use a sintaxe correta do powershell do windows.

Já estamos na raiz do projeto,
crie os page.tsx em /src/app/
crie os componentes em /src/componentes
nunca modifique arquivos da pasta  /src/componentes/ui, apenas use-os, pois são componentes prontos do shadcn

Lembre-se, faça apenas uma ação por vez.

## Stack

### Web:

- Framework: Next.js
- Linguagem: TypeScript
- Estilos: TailwindCSS
- Componentes: Shadcn e lucide-react
- Autenticação: Firebase Auth
    - JWT → Supabase (RLS)
- Banco de dados: Supabase
    - PostgreSQL
- Storage: Supabase Storage
- Deploy: Digital Ocean
    - CI/CD automático

ANALISE AS REGRAS ACIMA E FAÇA O QUE SE PEDE:

```


## EXPO:

```
# EXPO - REGRAS PARA SEGUIR EM CADA MÍNIMA AÇÃO

Responda sempre em português brasil

Codifique em inglês, variaveis names etc, pois tem gringos no projeto.
// Comments in english too.

# FLUXO OBRIGATÓRIO DE DESENVOLVIMENTO

PRIMEIRO:
- Se for modificar arquivos, confira antes quais arquivos serão modificados, e para cada um, liste quais trechos, estilos e funcionalidades devem permanecer imutáveis para manter a integridade do código.

SEGUNDO:
- Após o estudo, passe para a fase da analise dos passos. Pois pode ser uma ação grande que seja melhor quebrar em menores passos para manter a integridade do código, e garantir que faça o todo bem feito, danda a atenção necessário a cada passo. Analise e exponha seu plano.

TERCEIRO:
1. Decida o melhor primeiro passo e peça permissão. Espere o ok do usuário, e faça.
2. Decida o melhor segundo passo, analise o que deve permanecer imutável. Espere o ok do usuário, e faça.
3. ... por aí vai, obrigatoriamente parando e pedindo permissão para continuar para o próximo, explicitando qual será. Espere a permissão do usuário.

# REGRAS DURANTE TODO O FLUXO DE DESENVOLVIMENTO

- Sempre Use tailwind (nativewind v4) para estilo
- Sempre Dry e Siga o estilo, cores e fontes definidos em ./src/styles/global.css
- Sempre use zustand para gerenciar o estado local e @tanstack/react-query para server
- Sempre mantenha a compatibilidade com expo-router usando pasta src/app

Lembre-se:
- Criando projeto em React Native usando Expo com typescript
- Todos os arquivos são "index.tsx" criados dentro da pasta que ela sim recebe o nome relativo ao intuito do componente/página. Ao importar, se usa apenas o nome da pasta, sem fazer referencia ao index.
- Para comandos do terminal, use a sintaxe correta do powershell do windows.
- Faça apenas uma ação por vez
- Peça permissão antes de cada passo
- Sempre analise o que deve permanecer imutável para manter a integridade do código

Ao criar ou editar um index.tsx:
- Declare todos os tipos explicitamente no arquivo (não crie um arquivo separado para os tipos)
- Não reinvente a roda, use componentes e icones de bibliotecas, somente se ainda não houver, crie em /components.
- Crie toda a lógica hook relacionada "use..." no arquivo (não crie um arquivo separado em hooks)
- Crie todas as funções utilitárias específicas dentro do próprio arquivo (não crie em lib/)
- Crie todos os Server Actions específicos dentro do próprio arquivo (não crie em actions/)
- Use zustand para gerenciar estado e crie a store no arquivo (não crie um arquivo separado em store)
- use a pasta /api/ para routes apenas quando necessário.

Nunca modularizar essas partes: (tipos, hooks, funções utilitárias, server actions e stores) é benéfico nesse contexto pois estamos programando com AI Copilots, e ter tudo no mesmo arquivo ajuda a centralizar todo contexto necessário e evita duplicação de código. Nunca crie pasta hooks.

## Stack do projeto

- Framework: React Native with Expo
- Linguagem: TypeScript
- Estilos: Nativewind (Tailwind)
- Autenticação: Fast-Api-Users Auth
    - JWT → MongoDb (RLS)
- Banco de dados: MongoDb na Digital Ocean (Cluster)
- Storage: Spaces da Digital Ocean
```
