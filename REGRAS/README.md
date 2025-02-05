# REGRA - NEXTJS 14

## V4

Use essas regras para qualquer projeto:

Expo
```markdown
# REGRAS PARA SEGUIR EM CADA MÍNIMA AÇÃO

Responda sempre em português brasil

# FLUXO OBRIGATÓRIO DE DESENVOLVIMENTO

PRIMEIRO:
- Se for modificar arquivos, confira antes quais arquivos serão modificados, e para cada um, liste quais techos, estilos e funcionalidades devem permanecer imutáveis para manter a integridade do código. 

SEGUNDO:
- passe para a fase da ação passo a passo. Faça somente um passo por vez,
1. Decida o melhor primeiro passo e faça
2. Decida o melhor segundo passo e faça
3. ... por aí vai

# REGRAS DURANTE TODO O FLUXO DE DESENVOLVIMENTO

- DRY o estilo usando todas as classes e estilos importando do arquivo global de estilo.

# PONTOS DE ATENÇÃO

Criando projeto em React Native usando Expo com typescript
Para comandos do terminal, use a sintaxe correta do powershell do windows.
Já estamos na raiz do projeto,

Lembre-se, faça apenas uma ação por vez.

ANALISE AS REGRAS ACIMA E FAÇA O QUE SE PEDE:

```


Geral Typescript/React/Next/Expo


```markdown
# REGRAS PARA SEGUIR EM CADA MÍNIMA AÇÃO

Responda sempre em português brasil

Ao criar ou editar um page.tsx:
- Declare todos os tipos explicitamente no arquivo (não crie um arquivo separado para os tipos)
- Não reinvente a roda, use componentes de bibliotecas, somente se ainda não houver, crie em /components.
- Crie toda a lógica hook relacionada "use..." no arquivo (não crie um arquivo separado em hooks)
- Crie todas as funções utilitárias específicas dentro do próprio arquivo (não crie em lib/)
- Crie todos os Server Actions específicos dentro do próprio arquivo (não crie em actions/)
- Use zustand para gerenciar estado e crie a store no arquivo (não crie um arquivo separado em store)
- use a pasta /api/ para routes apenas quando necessário.

Nunca modularizar essas partes: (tipos, hooks, funções utilitárias, server actions e stores) é benéfico nesse contexto pois estamos programando com AI Copilots, e ter tudo no mesmo arquivo ajuda a centralizar todo contexto necessário e evita duplicação de código. Nunca crie pasta hooks.

# FLUXO OBRIGATÓRIO DE DESENVOLVIMENTO

PRIMEIRO:
- Se for modificar arquivos, confira antes quais arquivos serão modificados, e para cada um, liste quais techos, estilos e funcionalidades devem permanecer imutáveis para manter a integridade do código. 

SEGUNDO:
- passe para a fase da ação passo a passo. Faça somente um passo por vez,
1. Decida o melhor primeiro passo e faça
2. Decida o melhor segundo passo e faça
3. ... por aí vai

# REGRAS DURANTE TODO O FLUXO DE DESENVOLVIMENTO

- DRY o estilo usando todas as classes e estilos importando do mesmo arquivo de estilos do projeto.

# PONTOS DE ATENÇÃO

Lembre-se, faça apenas uma ação por vez.

ANALISE AS REGRAS ACIMA E FAÇA O QUE SE PEDE:

```

Nextjs

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
- Se for modificar arquivos, confira antes quais arquivos serão modificados, e para cada um, liste quais techos, estilos e funcionalidades devem permanecer imutáveis para manter a integridade do código. 

SEGUNDO:
- passe para a fase da ação passo a passo. Faça somente um passo por vez,
1. Decida o melhor primeiro passo e faça
2. Decida o melhor segundo passo e faça
3. ... por aí vai

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

Nextjs Completo

```markdown
Siga as regras

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
- Se for modificar arquivos, confira antes quais arquivos serão modificados, e para cada um, liste quais techos, estilos e funcionalidades devem permanecer imutáveis para manter a integridade do código. Envie isso e espere o ok do usuário.

SEGUNDO:
- Após a confirmação, passe para a fase do estudo: Sempre antes de cada ação confira na documentação das dependencias que estão sendo usadas como é a sintaxe correta. Se não tiver sido enviado a documentação para você, peça ela e espere o usuário enviar, antes de fazer qualquer coisa sem ter certeza. Isso evitará alucinação.

TERCEIRO:
- Após o estudo, passe para a fase da ação passo a passo. Faça somente um passo por vez, e sempre peça permissão para o próximo:
1. Decida o melhor primeiro passo e peça permissão.
2. Decida o melhor primeiro passo e peça permissão.
3. ... por aí vai, obrigatoriamente parando e pedindo permissão para continuar para o próximo, explicitando qual será. Espere a permissão do usuário. E siga assim até terminar a missão que foi dada.

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

ANALISE AS REGRAS ACIMA E FAÇA O QUE SE PEDE:
```


Nextjs Completo em Passos

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
- Se for modificar arquivos, confira antes quais arquivos serão modificados, e para cada um, liste quais techos, estilos e funcionalidades devem permanecer imutáveis para manter a integridade do código. Envie isso e espere o ok do usuário.

SEGUNDO:
- Após a confirmação, passe para a fase do estudo: Sempre antes de cada ação confira na documentação das dependencias que estão sendo usadas como é a sintaxe correta. Se não tiver sido enviado a documentação para você, peça ela e espere o usuário enviar, antes de fazer qualquer coisa sem ter certeza. Isso evitará alucinação.

TERCEIRO:
- Após o estudo, passe para a fase da ação passo a passo. Faça somente um passo por vez, e sempre peça permissão para o próximo:
1. Decida o melhor primeiro passo e peça permissão.
2. Decida o melhor primeiro passo e peça permissão.
3. ... por aí vai, obrigatoriamente parando e pedindo permissão para continuar para o próximo, explicitando qual será. Espere a permissão do usuário. E siga assim até terminar a missão que foi dada.

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

ANALISE AS REGRAS ACIMA E FAÇA O QUE SE PEDE:
```

-------------

Variações:

```
Siga as regras

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
- Se for modificar arquivos, confira antes quais arquivos serão modificados, e para cada um, liste quais techos, estilos e funcionalidades devem permanecer imutáveis para manter a integridade do código. Envie isso e espere o ok do usuário.

SEGUNDO:
- Após o estudo, passe para a fase da ação passo a passo. Faça somente um passo por vez, e sempre peça permissão para o próximo:
1. Decida o melhor primeiro passo e peça permissão.
2. Decida o melhor primeiro passo e peça permissão.
3. ... por aí vai, obrigatoriamente parando e pedindo permissão para continuar para o próximo, explicitando qual será. Espere a permissão do usuário. E siga assim até terminar a missão que foi dada.

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
crie os componentes no próprio arquivo
nunca modifique arquivos da pasta  /src/componentes/ui, apenas use-os, pois são componentes prontos do shadcn

Lembre-se, faça apenas uma ação por vez.

Sua missão é criar um exercício interativo com tudo em um único arquivo page.tsx (nunca crie outros arquivos)

ANALISE AS REGRAS ACIMA E FAÇA O QUE SE PEDE:

```


```
# REGRAS PARA SEGUIR EM CADA MÍNIMA AÇÃO

Responda sempre em português brasil

# FLUXO OBRIGATÓRIO DE DESENVOLVIMENTO

PRIMEIRO:
- Se for modificar arquivos, confira antes quais arquivos serão modificados, e para cada um, liste quais trechos, estilos e funcionalidades devem permanecer imutáveis para manter a integridade do código. Envie isso e espere o ok do usuário.

SEGUNDO:
- Após o estudo, passe para a fase da ação passo a passo. Faça somente um passo por vez, e sempre peça permissão para o próximo:
1. Decida o melhor primeiro passo e peça permissão.
2. Decida o melhor segundo passo e peça permissão.
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

```
# REGRAS PARA SEGUIR EM CADA MÍNIMA AÇÃO

Responda sempre em português brasil


# FLUXO OBRIGATÓRIO DE DESENVOLVIMENTO

PRIMEIRO:
- Se for modificar arquivos, confira antes quais arquivos serão modificados, e para cada um, liste quais trechos, estilos e funcionalidades devem permanecer imutáveis para manter a integridade do código. Envie isso e espere o ok do usuário.

SEGUNDO:
- Após a confirmação, passe para a fase do estudo: Sempre antes de cada ação confira na documentação do Expo e das dependências que estão sendo usadas como é a sintaxe correta. Se não tiver sido enviado a documentação para você, peça ela e espere o usuário enviar, antes de fazer qualquer coisa sem ter certeza. Isso evitará alucinação.

TERCEIRO:
- Após o estudo, passe para a fase da ação passo a passo. Faça somente um passo por vez, e sempre peça permissão para o próximo:
1. Decida o melhor primeiro passo e peça permissão.
2. Decida o melhor segundo passo e peça permissão.
3. ... por aí vai, obrigatoriamente parando e pedindo permissão para continuar para o próximo, explicitando qual será. Espere a permissão do usuário.

# REGRAS DURANTE TODO O FLUXO DE DESENVOLVIMENTO

- Use StyleSheet.create para estilos
- Implemente safe areas corretamente usando SafeAreaView
- Use Flexbox para layouts responsivos
- Siga as cores definidas em constants/Colors.ts
- Use as fontes definidas em constants/Fonts.ts
- Compatível sempre com iOS e Android
- Mantenha a compatibilidade com expo-router
- Use os assets da pasta correta (images, svgs, mock)

Lembre-se:
- Faça apenas uma ação por vez
- Peça permissão antes de cada passo
- Verifique a documentação antes de implementar
- Mantenha a consistência com o código existente


```

```

# REGRAS PARA SEGUIR EM CADA MÍNIMA AÇÃO

Responda sempre em português brasil

Ao criar ou editar arquivos:
- Declare todos os tipos explicitamente no arquivo (não crie um arquivo separado para os tipos)
- Não reinvente a roda, use componentes nativos do React Native e Expo primeiro
- Use os componentes existentes em /components antes de criar novos
- Crie toda a lógica hook relacionada "use..." no arquivo (não crie um arquivo separado em hooks)
- Crie todas as funções utilitárias específicas dentro do próprio arquivo
- Use zustand para gerenciar estado e crie a store no arquivo
- Sempre use SafeAreaView como container principal das screens
- Siga o padrão de estilização usando StyleSheet.create

# ESTRUTURA DO PROJETO

typescript
app/ # Pasta principal de navegação (expo-router)
├── app/ # Pasta principal de navegação (expo-router)
    ├── layout.tsx # Layout principal da aplicação
    ├── (tabs)/ # Grupo de rotas com tabs
        ├── _layout.tsx # Layout das tabs com bottom navigation
        ├── index.tsx # Tela inicial
        ├── # conjunto de telas públicas:

            /login, 
            /loginartista, 
            /onboarding
        ├── (auth)/ # Grupo de rotas autenticadas
            ├── _layout.tsx # Layout das rotas autenticadas
            ├── # conjunto de telas protegidas:
                /feed
    ├── assets/ # Recursos estáticos
        ├── fonts/ # Fontes customizadas
        ├── images/ # Imagens e ícones
        ├── mock/ # Dados mockados
        └── svgs/ # Arquivos SVG
    ├── components/ # Componentes reutilizáveis
    ├── constants/ # Constantes globais
        ├── Colors.ts # Cores do tema
        └── Fonts.ts # Configuração de fontes
    └── hooks/ # Hooks



# FLUXO OBRIGATÓRIO DE DESENVOLVIMENTO

PRIMEIRO:
- Se for modificar arquivos, confira antes quais arquivos serão modificados, e para cada um, liste quais trechos, estilos e funcionalidades devem permanecer imutáveis para manter a integridade do código. Envie isso e espere o ok do usuário.

SEGUNDO:
- Após a confirmação, passe para a fase do estudo: Sempre antes de cada ação confira na documentação do Expo e das dependências que estão sendo usadas como é a sintaxe correta. Se não tiver sido enviado a documentação para você, peça ela e espere o usuário enviar, antes de fazer qualquer coisa sem ter certeza. Isso evitará alucinação.

TERCEIRO:
- Após o estudo, passe para a fase da ação passo a passo. Faça somente um passo por vez, e sempre peça permissão para o próximo:
1. Decida o melhor primeiro passo e peça permissão.
2. Decida o melhor segundo passo e peça permissão.
3. ... por aí vai, obrigatoriamente parando e pedindo permissão para continuar para o próximo, explicitando qual será. Espere a permissão do usuário.

# REGRAS DURANTE TODO O FLUXO DE DESENVOLVIMENTO

- Use StyleSheet.create para estilos
- Implemente safe areas corretamente usando SafeAreaView
- Use Flexbox para layouts responsivos
- Siga as cores definidas em constants/Colors.ts
- Use as fontes definidas em constants/Fonts.ts
- Compatível sempre com iOS e Android
- Mantenha a compatibilidade com expo-router
- Use os assets da pasta correta (images, svgs, mock)

# PONTOS DE ATENÇÃO

Projeto em Expo com TypeScript
- Já executei criei o projeto Expo na raiz (executei: npx create-expo-app -t expo-template-blank-typescript)
- Já instalei o zustand (executei: npm install zustand)
- Já instalei o expo-router
- Para comandos do terminal, use a sintaxe correta do powershell do windows

Estrutura de Navegação:
- Use expo-router para navegação
- Mantenha a estrutura de grupos (auth), (tabs)
- Respeite os layouts (_layout.tsx)
- Use links nativos do expo-router

Lembre-se:
- Faça apenas uma ação por vez
- Peça permissão antes de cada passo
- Verifique a documentação antes de implementar
- Mantenha a consistência com o código existente



```
