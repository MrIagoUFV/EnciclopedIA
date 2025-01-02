# MODELO GERAL - NEXTJS 14

Já vem com todos os componentes do shadcn, zustand instalado, firebase, supabase, clerk e outras dependências iniciais

só executar: ```npm install```

<br><br>

### REGRAS


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

### ESTRUTURA INICIAL

```
# Project Directory Structure:
├── ./
    ├── .env.example
    ├── .eslintrc.json
    ├── .gptree_config
    ├── components.json
    ├── next.config.mjs
    ├── package.json
    ├── postcss.config.mjs
    ├── REGRAS.md
    ├── tailwind.config.ts
    ├── tsconfig.json
    ├── src/
        ├── app/
            ├── favicon.ico
            ├── globals.css
            ├── layout.tsx
            ├── page.tsx
            ├── fonts/
                ├── GeistMonoVF.woff
                ├── GeistVF.woff
        ├── components/
            ├── ui/
                ├── accordion.tsx
                ├── alert-dialog.tsx
                ├── alert.tsx
                ├── aspect-ratio.tsx
                ├── avatar.tsx
                ├── badge.tsx
                ├── breadcrumb.tsx
                ├── button.tsx
                ├── calendar.tsx
                ├── card.tsx
                ├── carousel.tsx
                ├── chart.tsx
                ├── checkbox.tsx
                ├── collapsible.tsx
                ├── command.tsx
                ├── context-menu.tsx
                ├── dialog.tsx
                ├── drawer.tsx
                ├── dropdown-menu.tsx
                ├── form.tsx
                ├── hover-card.tsx
                ├── input-otp.tsx
                ├── input.tsx
                ├── label.tsx
                ├── menubar.tsx
                ├── navigation-menu.tsx
                ├── pagination.tsx
                ├── popover.tsx
                ├── progress.tsx
                ├── radio-group.tsx
                ├── resizable.tsx
                ├── scroll-area.tsx
                ├── select.tsx
                ├── separator.tsx
                ├── sheet.tsx
                ├── sidebar.tsx
                ├── skeleton.tsx
                ├── slider.tsx
                ├── sonner.tsx
                ├── switch.tsx
                ├── table.tsx
                ├── tabs.tsx
                ├── textarea.tsx
                ├── toast.tsx
                ├── toaster.tsx
                ├── toggle-group.tsx
                ├── toggle.tsx
                ├── tooltip.tsx
        ├── hooks/
            ├── use-mobile.tsx
            ├── use-toast.ts
        ├── lib/
            ├── utils.ts

# BEGIN FILE CONTENTS

# File: REGRAS.md

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



# END FILE CONTENTS


# File: src\app\page.tsx

import Image from "next/image";

export default function Home() {
  return (
    <div className="grid grid-rows-[20px_1fr_20px] items-center justify-items-center min-h-screen p-8 pb-20 gap-16 sm:p-20 font-[family-name:var(--font-geist-sans)]">
      <main className="flex flex-col gap-8 row-start-2 items-center sm:items-start">
        <Image
          className="dark:invert"
          src="https://nextjs.org/icons/next.svg"
          alt="Next.js logo"
          width={180}
          height={38}
          priority
        />
        <ol className="list-inside list-decimal text-sm text-center sm:text-left font-[family-name:var(--font-geist-mono)]">
          <li className="mb-2">
            Get started by editing{" "}
            <code className="bg-black/[.05] dark:bg-white/[.06] px-1 py-0.5 rounded font-semibold">
              src/app/page.tsx
            </code>
            .
          </li>
          <li>Save and see your changes instantly.</li>
        </ol>

        <div className="flex gap-4 items-center flex-col sm:flex-row">
          <a
            className="rounded-full border border-solid border-transparent transition-colors flex items-center justify-center bg-foreground text-background gap-2 hover:bg-[#383838] dark:hover:bg-[#ccc] text-sm sm:text-base h-10 sm:h-12 px-4 sm:px-5"
            href="https://vercel.com/new?utm_source=create-next-app&utm_medium=appdir-template-tw&utm_campaign=create-next-app"
            target="_blank"
            rel="noopener noreferrer"
          >
            <Image
              className="dark:invert"
              src="https://nextjs.org/icons/vercel.svg"
              alt="Vercel logomark"
              width={20}
              height={20}
            />
            Deploy now
          </a>
          <a
            className="rounded-full border border-solid border-black/[.08] dark:border-white/[.145] transition-colors flex items-center justify-center hover:bg-[#f2f2f2] dark:hover:bg-[#1a1a1a] hover:border-transparent text-sm sm:text-base h-10 sm:h-12 px-4 sm:px-5 sm:min-w-44"
            href="https://nextjs.org/docs?utm_source=create-next-app&utm_medium=appdir-template-tw&utm_campaign=create-next-app"
            target="_blank"
            rel="noopener noreferrer"
          >
            Read our docs
          </a>
        </div>
      </main>
      <footer className="row-start-3 flex gap-6 flex-wrap items-center justify-center">
        <a
          className="flex items-center gap-2 hover:underline hover:underline-offset-4"
          href="https://nextjs.org/learn?utm_source=create-next-app&utm_medium=appdir-template-tw&utm_campaign=create-next-app"
          target="_blank"
          rel="noopener noreferrer"
        >
          <Image
            aria-hidden
            src="https://nextjs.org/icons/file.svg"
            alt="File icon"
            width={16}
            height={16}
          />
          Learn
        </a>
        <a
          className="flex items-center gap-2 hover:underline hover:underline-offset-4"
          href="https://vercel.com/templates?framework=next.js&utm_source=create-next-app&utm_medium=appdir-template-tw&utm_campaign=create-next-app"
          target="_blank"
          rel="noopener noreferrer"
        >
          <Image
            aria-hidden
            src="https://nextjs.org/icons/window.svg"
            alt="Window icon"
            width={16}
            height={16}
          />
          Examples
        </a>
        <a
          className="flex items-center gap-2 hover:underline hover:underline-offset-4"
          href="https://nextjs.org?utm_source=create-next-app&utm_medium=appdir-template-tw&utm_campaign=create-next-app"
          target="_blank"
          rel="noopener noreferrer"
        >
          <Image
            aria-hidden
            src="https://nextjs.org/icons/globe.svg"
            alt="Globe icon"
            width={16}
            height={16}
          />
          Go to nextjs.org →
        </a>
      </footer>
    </div>
  );
}


# END FILE CONTENTS


# File: src\app\globals.css

@tailwind base;
@tailwind components;
@tailwind utilities;

body {
  font-family: Arial, Helvetica, sans-serif;
}

@layer utilities {
  .text-balance {
    text-wrap: balance;
  }
}

@layer base {
  :root {
    --background: 0 0% 100%;
    --foreground: 240 10% 3.9%;
    --card: 0 0% 100%;
    --card-foreground: 240 10% 3.9%;
    --popover: 0 0% 100%;
    --popover-foreground: 240 10% 3.9%;
    --primary: 240 5.9% 10%;
    --primary-foreground: 0 0% 98%;
    --secondary: 240 4.8% 95.9%;
    --secondary-foreground: 240 5.9% 10%;
    --muted: 240 4.8% 95.9%;
    --muted-foreground: 240 3.8% 46.1%;
    --accent: 240 4.8% 95.9%;
    --accent-foreground: 240 5.9% 10%;
    --destructive: 0 84.2% 60.2%;
    --destructive-foreground: 0 0% 98%;
    --border: 240 5.9% 90%;
    --input: 240 5.9% 90%;
    --ring: 240 10% 3.9%;
    --chart-1: 12 76% 61%;
    --chart-2: 173 58% 39%;
    --chart-3: 197 37% 24%;
    --chart-4: 43 74% 66%;
    --chart-5: 27 87% 67%;
    --radius: 0.5rem;
    --sidebar-background: 0 0% 98%;
    --sidebar-foreground: 240 5.3% 26.1%;
    --sidebar-primary: 240 5.9% 10%;
    --sidebar-primary-foreground: 0 0% 98%;
    --sidebar-accent: 240 4.8% 95.9%;
    --sidebar-accent-foreground: 240 5.9% 10%;
    --sidebar-border: 220 13% 91%;
    --sidebar-ring: 217.2 91.2% 59.8%;
  }
  .dark {
    --background: 240 10% 3.9%;
    --foreground: 0 0% 98%;
    --card: 240 10% 3.9%;
    --card-foreground: 0 0% 98%;
    --popover: 240 10% 3.9%;
    --popover-foreground: 0 0% 98%;
    --primary: 0 0% 98%;
    --primary-foreground: 240 5.9% 10%;
    --secondary: 240 3.7% 15.9%;
    --secondary-foreground: 0 0% 98%;
    --muted: 240 3.7% 15.9%;
    --muted-foreground: 240 5% 64.9%;
    --accent: 240 3.7% 15.9%;
    --accent-foreground: 0 0% 98%;
    --destructive: 0 62.8% 30.6%;
    --destructive-foreground: 0 0% 98%;
    --border: 240 3.7% 15.9%;
    --input: 240 3.7% 15.9%;
    --ring: 240 4.9% 83.9%;
    --chart-1: 220 70% 50%;
    --chart-2: 160 60% 45%;
    --chart-3: 30 80% 55%;
    --chart-4: 280 65% 60%;
    --chart-5: 340 75% 55%;
    --sidebar-background: 240 5.9% 10%;
    --sidebar-foreground: 240 4.8% 95.9%;
    --sidebar-primary: 224.3 76.3% 48%;
    --sidebar-primary-foreground: 0 0% 100%;
    --sidebar-accent: 240 3.7% 15.9%;
    --sidebar-accent-foreground: 240 4.8% 95.9%;
    --sidebar-border: 240 3.7% 15.9%;
    --sidebar-ring: 217.2 91.2% 59.8%;
  }
}

@layer base {
  * {
    @apply border-border;
  }
  body {
    @apply bg-background text-foreground;
  }
}


# END FILE CONTENTS


# File: .env.example

# CLERK
NEXT_PUBLIC_CLERK_PUBLISHABLE_KEY=...
CLERK_SECRET_KEY=...

# Rotas de Autenticação - CLERK URLS
NEXT_PUBLIC_CLERK_SIGN_IN_URL=/sign-in
NEXT_PUBLIC_CLERK_SIGN_UP_URL=/sign-up
NEXT_PUBLIC_CLERK_AFTER_SIGN_IN_URL=/
NEXT_PUBLIC_CLERK_AFTER_SIGN_UP_URL=/ 

# Supabase
NEXT_PUBLIC_SUPABASE_URL=...
NEXT_PUBLIC_SUPABASE_ANON_KEY=...

#MongoDB
MONGODB_URI=...

# Groq API Key
NEXT_PUBLIC_GROQ_API_KEY=...
# OpenAI
OPENAI_API_KEY=...
# Hugging Face
NEXT_PUBLIC_HUGGING_FACE_API_KEY=...
# Github
NEXT_PUBLIC_GITHUB_TOKEN=...

# Firebase
NEXT_PUBLIC_FIREBASE_API_KEY=...
NEXT_PUBLIC_FIREBASE_AUTH_DOMAIN=...
NEXT_PUBLIC_FIREBASE_PROJECT_ID=...
NEXT_PUBLIC_FIREBASE_STORAGE_BUCKET=...
NEXT_PUBLIC_FIREBASE_MESSAGING_SENDER_ID=...
NEXT_PUBLIC_FIREBASE_APP_ID=...
NEXT_PUBLIC_FIREBASE_MEASUREMENT_ID=...



# END FILE CONTENTS


# File: package.json

{
  "name": "teste-web",
  "version": "0.1.0",
  "private": true,
  "scripts": {
    "dev": "next dev",
    "build": "next build",
    "start": "next start",
    "lint": "next lint"
  },
  "dependencies": {
    "@clerk/nextjs": "^6.9.6",
    "@hookform/resolvers": "^3.9.1",
    "@radix-ui/react-accordion": "^1.2.2",
    "@radix-ui/react-alert-dialog": "^1.1.4",
    "@radix-ui/react-aspect-ratio": "^1.1.1",
    "@radix-ui/react-avatar": "^1.1.2",
    "@radix-ui/react-checkbox": "^1.1.3",
    "@radix-ui/react-collapsible": "^1.1.2",
    "@radix-ui/react-context-menu": "^2.2.4",
    "@radix-ui/react-dialog": "^1.1.4",
    "@radix-ui/react-dropdown-menu": "^2.1.4",
    "@radix-ui/react-hover-card": "^1.1.4",
    "@radix-ui/react-label": "^2.1.1",
    "@radix-ui/react-menubar": "^1.1.4",
    "@radix-ui/react-navigation-menu": "^1.2.3",
    "@radix-ui/react-popover": "^1.1.4",
    "@radix-ui/react-progress": "^1.1.1",
    "@radix-ui/react-radio-group": "^1.2.2",
    "@radix-ui/react-scroll-area": "^1.2.2",
    "@radix-ui/react-select": "^2.1.4",
    "@radix-ui/react-separator": "^1.1.1",
    "@radix-ui/react-slider": "^1.2.2",
    "@radix-ui/react-slot": "^1.1.1",
    "@radix-ui/react-switch": "^1.1.2",
    "@radix-ui/react-tabs": "^1.1.2",
    "@radix-ui/react-toast": "^1.2.4",
    "@radix-ui/react-toggle": "^1.1.1",
    "@radix-ui/react-toggle-group": "^1.1.1",
    "@radix-ui/react-tooltip": "^1.1.6",
    "@supabase/auth-helpers-nextjs": "^0.10.0",
    "@supabase/supabase-js": "^2.47.10",
    "class-variance-authority": "^0.7.1",
    "clsx": "^2.1.1",
    "cmdk": "^1.0.0",
    "date-fns": "^3.6.0",
    "embla-carousel-react": "^8.5.1",
    "firebase": "^11.1.0",
    "input-otp": "^1.4.1",
    "lucide-react": "^0.469.0",
    "next": "14.2.21",
    "next-themes": "^0.4.4",
    "react": "^18",
    "react-day-picker": "^8.10.1",
    "react-dom": "^18",
    "react-hook-form": "^7.54.2",
    "react-resizable-panels": "^2.1.7",
    "recharts": "^2.15.0",
    "sharp": "^0.33.5",
    "sonner": "^1.7.1",
    "tailwind-merge": "^2.6.0",
    "tailwindcss-animate": "^1.0.7",
    "vaul": "^1.1.2",
    "zod": "^3.24.1",
    "zustand": "^5.0.2"
  },
  "devDependencies": {
    "@types/node": "^20",
    "@types/react": "^18",
    "@types/react-dom": "^18",
    "eslint": "^8",
    "eslint-config-next": "14.2.21",
    "postcss": "^8",
    "tailwindcss": "^3.4.1",
    "typescript": "^5"
  }
}


# END FILE CONTENTS


# File: src\app\layout.tsx

import type { Metadata } from "next";
import localFont from "next/font/local";
import "./globals.css";

const geistSans = localFont({
  src: "./fonts/GeistVF.woff",
  variable: "--font-geist-sans",
  weight: "100 900",
});
const geistMono = localFont({
  src: "./fonts/GeistMonoVF.woff",
  variable: "--font-geist-mono",
  weight: "100 900",
});

export const metadata: Metadata = {
  title: "Create Next App",
  description: "Generated by create next app",
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="en">
      <body
        className={`${geistSans.variable} ${geistMono.variable} antialiased`}
      >
        {children}
      </body>
    </html>
  );
}


# END FILE CONTENTS
```
