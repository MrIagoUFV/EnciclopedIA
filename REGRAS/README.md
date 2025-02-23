# REGRAS

> Adapte os detalhes para as especificidades do seu projeto!

# JSON

## REGRA QUE USO PARA EXPO (REACT NATIVE)

```json
{
    "general": {
        "response_language": "Português (Brasil)",
        "code_language": "English",
        "comment_language": "English"
    },
    "development_flow": {
        "steps": [
            {
                "phase": "PRIMEIRO",
                "description": "Se for modificar arquivos, confira antes quais arquivos serão modificados, e para cada um, liste quais trechos, estilos e funcionalidades devem permanecer imutáveis para manter a integridade do código."
            },
            {
                "phase": "SEGUNDO",
                "description": "Após o estudo, passe para a fase de análise dos passos. Se a ação for grande, divida em passos menores para manter a integridade do código, garantindo que cada etapa receba a atenção necessária. Analise e exponha seu plano."
            },
            {
                "phase": "TERCEIRO",
                "steps": [
                    "Decida o melhor primeiro passo, e faça. ",
                    "Decida o melhor segundo passo, analise o que deve permanecer imutável e faça. ",
                    "Continue, obrigatoriamente analisando o que deve permanecer imutável e fazendo um passo por vez."
                ]
            }
        ]
    },
    "development_rules": [
        "Sempre use tailwind (nativewind v4) para estilo",
        "Sempre aplique o princípio DRY e siga o estilo, cores e fontes definidos em ./global.css",
        "Sempre use zustand para gerenciar o estado local e @tanstack/react-query para operações no servidor",
        "Sempre mantenha a compatibilidade com expo-router utilizando a pasta app/",
        "Sempre defina as cores do tema como variáveis CSS no global.css e use-as via classes tailwind",
        "Para gradientes no React Native, sempre use expo-linear-gradient com cores definidas no global.css",
        "Nunca use códigos de cor diretamente nos componentes, sempre use as variáveis semânticas do tema",
        "Carregue apenas as fontes necessárias em cada página usando useFonts",
        "Use nomes semânticos para cores (neutral-darkest, primary, etc.) em vez de nomes descritivos",
        "Mantenha a consistência do sistema de cores com paletas neutral e primary",
        "Defina tamanhos de fonte sem unidades px para compatibilidade com React Native",
        "Sempre use o sistema de internacionalização para textos visíveis",
        "Defina as traduções no escopo do arquivo onde serão usadas",
        "Mantenha as chaves de tradução organizadas e semânticas",
        "Garanta suporte completo para português e inglês em todas as strings"
    ],
    "project_guidelines": {
        "project_type": "Projeto em React Native usando Expo com TypeScript",
        "file_naming": "Todos os arquivos são 'index.tsx' criados dentro de pastas cujo nome reflete o intuito do componente/página. Ao importar, use apenas o nome da pasta, sem referenciar explicitamente o 'index'.",
        "terminal_commands": "Use a sintaxe correta do PowerShell do Windows para comandos do terminal",
        "one_action_at_a_time": "Execute apenas uma ação por vez e peça permissão antes de cada passo",
        "immutable_analysis": "Sempre analise o que deve permanecer imutável para preservar a integridade do código",
        "theme_management": {
            "colors": {
                "naming": "Use nomes semânticos (neutral-darkest, primary) em vez de descritivos (black, orange)",
                "definition": "Defina todas as cores como variáveis CSS no global.css",
                "usage": "Use apenas via classes tailwind que referenciam as variáveis",
                "palettes": {
                    "neutral": "darkest → lightest para escala de cinza",
                    "primary": "cor principal e variante dark"
                }
            },
            "gradients": {
                "definition": "Defina cores e locations no global.css",
                "implementation": "Use expo-linear-gradient com w-full h-full",
                "container": "Sempre use overflow-hidden em containers de gradiente"
            },
            "typography": {
                "scale": "H1-H6, Label, Body 1-5 com tamanhos sem px",
                "weights": "Bold e Regular da fonte Istok",
                "lineHeight": "Automático para melhor adaptação"
            },
            "internationalization": {
                "structure": {
                    "location": "Defina as traduções no próprio arquivo da página/componente",
                    "namespacing": "Use o nome da página/componente como namespace",
                    "organization": "Agrupe traduções por contexto semântico"
                },
                "implementation": {
                    "hook": "Use o hook useLanguages com o namespace correto",
                    "translations": "Adicione traduções via i18n.addResourceBundle",
                    "languages": "Suporte obrigatório para pt-BR e en"
                },
                "best_practices": {
                    "keys": "Use chaves descritivas e semânticas (ex: buttonLabel, pageTitle)",
                    "variables": "Evite strings hardcoded, use sempre o sistema de tradução",
                    "fallbacks": "Garanta que todas as chaves existam em todos os idiomas"
                },
                "components": {
                    "text": "Use o hook t() para todos os textos visíveis",
                    "buttons": "Inclua estados de loading/disabled nas traduções",
                    "forms": "Traduza labels, placeholders e mensagens de erro"
                }
            }
        }
    },
    "index_tsx_guidelines": {
        "type_declaration": "Declare todos os tipos explicitamente no próprio arquivo (não criar um arquivo separado para os tipos)",
        "use_existing_components": "Não reinvente a roda; utilize componentes e ícones de bibliotecas existentes. Se não existirem, crie-os em /components",
        "logic_hooks": "Implemente toda a lógica de hooks (iniciada com 'use...') no mesmo arquivo, sem separar em arquivos de hooks",
        "utility_functions": "Crie funções utilitárias específicas dentro do próprio arquivo, sem separá-las em lib/",
        "server_actions": "Crie todos os Server Actions específicos dentro do próprio arquivo, sem movê-los para actions/",
        "state_management": "Use zustand para gerenciar o estado e crie a store no próprio arquivo, sem separá-la",
        "api_routes": "Utilize a pasta /api/ para rotas apenas quando necessário",
        "centralization": "Nunca modularize tipos, hooks, funções utilitárias, server actions ou stores; centralize tudo no mesmo arquivo para facilitar a integração com AI Copilots",
        "styling": {
            "colors": "Use apenas classes tailwind que referenciam variáveis do tema",
            "gradients": "Use LinearGradient com cores do global.css",
            "fonts": "Use fontFamily via style prop com fontes carregadas no _layout.tsx"
        }
    },
    "stack": {
        "framework": "React Native with Expo",
        "language": "TypeScript",
        "styles": "Nativewind (Tailwind)",
        "authentication": "Fast-Api-Users Auth (JWT → MongoDb com RLS)",
        "database": "MongoDb na Digital Ocean (Cluster)",
        "storage": "Spaces da Digital Ocean"
    }
}
```

## REGRA QUE USO PARA NEXTJS

```json
{
    "general": {
        "response_language": "Português (Brasil)"
    },
    "page_tsx_guidelines": {
        "type_declaration": "Declare todos os tipos explicitamente no próprio arquivo (não crie um arquivo separado para os tipos)",
        "component_usage": "Use componentes do shadcn em /components/ui; se não houver, procure em outras bibliotecas; se ainda não existir, crie em /components",
        "hook_logic": "Crie toda a lógica dos hooks (prefixados com 'use...') no mesmo arquivo (não crie um arquivo separado em hooks)",
        "utility_functions": "Crie todas as funções utilitárias específicas dentro do próprio arquivo (não crie em lib/)",
        "server_actions": "Crie todos os Server Actions específicos dentro do próprio arquivo (não crie em actions/)",
        "state_management": "Use zustand para gerenciar o estado e crie a store no próprio arquivo (não crie um arquivo separado em store)",
        "api_routes": "Utilize a pasta /api/ para rotas apenas quando necessário",
        "centralization": "Nunca modularize tipos, hooks, funções utilitárias, server actions e stores; centralizar tudo no mesmo arquivo ajuda a manter o contexto para AI Copilots. Nunca crie pasta hooks."
    },
    "development_flow": {
        "steps": [
            {
                "phase": "PRIMEIRO",
                "description": "Se for modificar arquivos, confira antes quais arquivos serão modificados, e para cada um, liste quais trechos, estilos e funcionalidades devem permanecer imutáveis para manter a integridade do código."
            },
            {
                "phase": "SEGUNDO",
                "description": "Após o estudo, passe para a fase de análise dos passos. Se a ação for grande, divida em passos menores para manter a integridade do código, garantindo que cada etapa receba a atenção necessária. Analise e exponha seu plano."
            },
            {
                "phase": "TERCEIRO",
                "steps": [
                    "Decida o melhor primeiro passo, e faça. ",
                    "Decida o melhor segundo passo, analise o que deve permanecer imutável e faça. ",
                    "Continue, obrigatoriamente analisando o que deve permanecer imutável e fazendo um passo por vez."
                ]
            }
        ]
    },
    "development_rules": [
        "Utilize o princípio DRY para estilos, importando todas as classes e estilos de @globals.css e @tailwind.config.ts."
    ],
    "points_of_attention": {
        "project_creation": "Projeto Next.js 14 criado na raiz (npx create-next-app@14 .)",
        "zustand": "zustand já instalado (npm install zustand)",
        "shadcn": "shadcn e seus componentes instalados em /components/ui (todos componentes já instalados em /components/ui, e o useToast instalado em /hooks/use-toast)",
        "terminal_syntax": "Use a sintaxe correta do PowerShell do Windows para comandos do terminal",
        "project_structure": {
            "pages": "Crie os page.tsx em /src/app/",
            "components": "Crie os componentes em /src/componentes",
            "ui_components": "Nunca modifique os arquivos em /src/componentes/ui; utilize-os conforme fornecidos"
        },
        "action_guideline": "Execute apenas uma ação por vez"
    },
    "stack": {
        "framework": "Next.js",
        "language": "TypeScript",
        "styles": "TailwindCSS",
        "components": "Shadcn e lucide-react",
        "authentication": "Firebase Auth (JWT → Supabase com RLS)",
        "database": "Firebase Firestore",
        "storage": "Não há",
        "deploy": "Digital Ocean (CI/CD automático)"
    }
}
```



# MARKDOWN

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
