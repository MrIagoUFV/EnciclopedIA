# REGRA - NEXTJS 14

## V4

Use essas regras para qualquer projeto:

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
