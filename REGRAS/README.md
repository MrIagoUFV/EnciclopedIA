# REGRA - NEXTJS 14

## V3

Use essas regras para qualquer projeto:

```markdown
<ALWAYS FOLLOW THIS RULES OR YOU WILL DIE>

## FLUXO OBRIGATÓRIO DE DESENVOLVIMENTO PARA CADA MENSAGEM QUE EU TE ENVIAR

PRIMEIRO:
- Se for modificar arquivos, confira antes quais arquivos serão modificados, e para cada um, liste quais techos, estilos e funcionalidades devem permanecer imutáveis para manter a integridade do código. Envie isso e espere o ok do usuário.

SEGUNDO:
- Após a confirmação, passe para a fase do estudo: Sempre antes de cada ação confira na documentação das dependencias que estão sendo usadas como é a sintaxe correta. Se não tiver sido enviado a documentação para você, peça ela e espere o usuário enviar, antes de fazer qualquer coisa sem ter certeza. Isso evitará alucinação.

TERCEIRO:
- Após o estudo, passe para a fase da ação passo a passo. Faça somente um passo por vez, e sempre peça permissão para o próximo:
1. Decida o melhor primeiro passo e peça permissão.
2. Decida o melhor primeiro passo e peça permissão.
3. ... por aí vai, obrigatoriamente parando e pedindo permissão para continuar para o próximo, explicitando qual será. Espere a permissão do usuário. E siga assim até terminar a missão que foi dada.

</ ALWAYS FOLLOW THIS RULES OR YOU WILL DIE>
```

## BÔNUS - REGRAS/PROMPTS QUE USO AO FINAL DE PROMPTS


Use essas regras para projetos react/native/nextjs, no final de cada prompt, não nas regras em geral:

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
```


```markdown
Confira antes, quais arquivos serão modificados, e em cada um, quais techos devem permanecer imutáveis para manter a integridade do código

Confira na doc as sintaxes corretas e boas práticas também: @nomedadoc
```


```markdown
antes de criar, leia a doc para ver se tem como fazer exatamente isso. Se não crie uma solução mais próxima possível e me fale seu plano para eu confirmar antes de começar: @nomedadoc
```
