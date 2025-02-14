# Programming-Prompts
Prompts para usar no seu processo de desenvolvimento, para entender e documentar o código, além de obter insights e análises que você ainda não pensou.

- Por @mriago: https://www.youtube.com/@mriago

- Colaborações são muito bem-vindas!

## 🪙 PROMPTS DE OURO


    
- Engenharia reversa
    
    ```markdown
    
    Aja como engenheiro de prompt e crie a melhor sequência de prompts para recriar esse exato projeto 100% funcional e completo.
    
    Os promtps serão promtptados para uma ai agent que codifica sozinha e você só precisa planejar bem a sequência de passos e a descrição do prompt.
    
    Siga sempre essas 6 diretrizes:
    
    1. O prompt deve ser focado em prática, por exemplo: "1. Crie uma estrutura básica de uma página HTML5". 
    2. Otimize a ordem dos prompts para ficar eficiente possível, seguindo o raciocínio de um humano, fazendo as configurações sob demanda na ordem que um humano faria. Foque em implementar todas as funcionalidades primeiro, para depois estilizar, caso precise.
    3. Cada prompt deve ser o mais completo e descritivo possível, instruindo sobre o conteúdo, funcionalidades, lógica, estrutura etc.
    4. Indique os comandos para instalar todas as bibliotecas necessárias.
    5. O prompts devem ser instruções completas passo a passo, verificando cada passo para evitar erros, não deixe pontas soltas ou coisas a fazer, mande fazer tudo o que tem que ser feito e configurado para não ter nenhum erro ou aviso.
    6. A ia pode apenas criar e editar arquivos, a parte de comandos do terminal sou eu quem faço, reescreva acima separando em blocos quando passar para ações humanas e ia. Escreva na melhor ordem de ser executada, podendo criar varios blocos para indicar a necessidade de uma ação humana antes de continuar para a ação ia. Ações humanas em um bloco markdown separado das ações ia em outro bloco
    
    Deve ter quantos prompts forem necessário, de 1 até 100. Seja sempre o mais prompt eficient possível.
    
    Por favor, formate a resposta em um bloco copiável em Markdown para fácil leitura e organização.
    ```
    
- Pseudo-código e Lógica
    
    ```markdown
    Converta este código em pseudo-código:
    
    Por favor:
    1. Use linguagem natural
    2. Explique a lógica passo a passo
    3. Identifique os principais algoritmos utilizados
    4. Destaque as estruturas de controle importantes
    ```

    ```markdown
    Converta este código em pseudo-código:
    
    Por favor use linguagem natural
    Use o método black box para entender as partes lógicas do código
    O pseudo código não deve conter termos técnicos, mas sim termos que até leigos  consigam ler e entender toda lógica do código
    
    Obrigatório: Use a mesma estrutura do código para aprender por associação
    
    Responda em um bloco markdown
    ```

    ```markdown
    Deixe mais completo ainda
    ```
    
    ```markdown
    me de o user story desse código seguindo o fluxo de uso contando a história, iniciei o porgrama e ...
    ```
    
    ```markdown
    Crie o programa em pseudo-código para realizar esse user story:
    
    Por favor use linguagem natural
    Use o método black box para entender as partes lógicas do código
    O pseudo código não deve conter termos técnicos, mas sim termos que até leigos  consigam ler e entender toda lógica do código
    
    Obrigatório: Use a mesma estrutura do código para aprender por associação
    
    Responda em um bloco markdown
    ```
    
- Pergunta certa
    
    ```markdown
    Na programação e outras ciências, maia importante que a resposta é a pergunta. 
    Quais perguntas que não estou te fazendo que eu deveria estar fazendo?
    ```
    

## Documentar

- Documentar o Início
    
    ```markdown
    Escreva uma documentação no início do código, exiplicando todo o código, e tudo o que for necessário documentar
    ```
    
    ```markdown
    Analise este código  e crie uma documentação técnica que inclua:
    - Visão geral do projeto
    - Principais funcionalidades
    - Estrutura do código
    - Dependências (opcional)
    - Como executar (opcional)
    Por favor, use linguagem clara e objetiva, focando nos aspectos mais importantes.
    ```
    
- Comenta os blocos
    
    ```markdown
    Comente o inicio desse bloco lógico, explicando para que serve
    ```
    

## Entender

- Para cada parte: Pseudocódigo
    
    ```markdown
    Adicione o pseudo código originário dessa parte, para entender o racicínio para criar a parte e cada coisa que ela faz, nesse formato:
    
    explicação da parte
    pseudocódigo (qual seria o prompt detalhado para ia criar essa parte, sem linguagem técnica)
    ```
    
- Análise Linha por Linha
    
    ```markdown
    comente no final de cada linha, traduzindo de forma que um leigo entenda toda a lógica
    ```
    
    ```markdown
    Explique o seguinte trecho de código, comentando cada linha:
    
    Por favor:
    1. Explique o que cada linha faz
    2. Por que essa abordagem foi escolhida
    3. Quais conceitos de programação estão sendo aplicados
    ```
    
- Análise de Blocos Lógicos
    
    ```markdown
    Analise este bloco de código:
    
    Por favor:
    1. Qual é o propósito principal deste bloco?
    2. Como ele se integra com o resto do código?
    3. Quais padrões de design estão sendo utilizados?
    4. Como isso poderia ser implementado de forma diferente?
    ```
    
- Engenharia Reversa do Raciocínio
    
    ```markdown
    Considerando este código:
    
    Por favor:
    1. Qual foi provavelmente o processo de pensamento do desenvolvedor?
    2. Quais problemas ele precisou resolver?
    3. Como ele quebrou o problema em partes menores?
    4. Quais decisões de design foram tomadas e por quê?
    ```
    
- Visualização do Fluxo de Dados
    
    ```markdown
    Explique o fluxo de dados neste código:
    
    Por favor:
    1. Como os dados se movem entre as diferentes partes do código?
    2. Quais são os estados principais do jogo?
    3. Como as informações são armazenadas e atualizadas?
    4. Crie um diagrama em texto mostrando o fluxo de dados
    ```
    
- Explicação para Diferentes Níveis
    
    ```markdown
    Explique este código em três níveis:
    1. Para um iniciante completo em programação
    2. Para um programador intermediário
    3. Para um programador avançado
    
    Destaque aspectos diferentes para cada nível de experiência.
    ```
    
- Identificação de Padrões
    
    ```markdown
    Analise este código e identifique:
    1. Padrões comuns de programação utilizados
    2. Onde esses padrões aparecem em outras aplicações
    3. Como esses padrões podem ser adaptados para outros projetos
    4. Alternativas a esses padrões
    ```
    
- Conexão de Conceitos
    
    ```markdown
    Relacione os conceitos usados neste código com:
    1. Princípios fundamentais de programação
    2. Padrões de design comuns
    3. Outros códigos similares
    4. Conceitos de computação em geral
    ```
    
- Metacognição
    
    ```markdown
    Analise minha abordagem para entender este código:
    
    [EXPLICAÇÃO DA SUA COMPREENSÃO]
    
    1. Há aspectos importantes que estou negligenciando?
    2. Quais conceitos fundamentais devo revisar?
    3. Como posso melhorar meu processo de aprendizado?
    ```
    
- Técnica do Professor Imaginário
    
    ```markdown
    Atue como um professor de [estilo específico] e explique este código:
    ```
    
    Estilos possíveis:
    - Professor que usa analogias do dia a dia
    - Professor focado em fundamentos matemáticos
    - Professor que ensina através de desafios práticos
    - Professor que foca em boas práticas da indústria
    
- Técnica da Documentação Progressiva
    
    ```markdown
    Documentação Nível 1: Explique este código como se fosse para uma criança de 10 anos.
    
    Documentação Nível 2: Agora explique os mesmos conceitos para um estudante de programação.
    
    Documentação Nível 3: Agora faça uma análise técnica profunda para um desenvolvedor sênior.
    
    Compare as três explicações e destaque como os conceitos foram apresentados diferentemente em cada nível.
    ```
    
    ```markdown
    Documentação Nível 1: Explique este código como se fosse para uma criança de 10 anos.
    ```
    
    ```markdown
    Documentação Nível 2: Agora explique os mesmos conceitos para um estudante de programação.
    ```
    
    ```markdown
    Documentação Nível 3: Agora faça uma análise técnica profunda para um desenvolvedor sênior.
    ```
    
    ```markdown
    Compare as três explicações e destaque como os conceitos foram apresentados diferentemente em cada nível.
    ```
    

## Melhorar

- Como fazer…
    
    ```markdown
    Sou iniciante, estou aprendendo através de projetos. Me explique o raciocínio passo que eu preciso: (fazer tal coisa)
    
    Use um linguagem que iniciantes entendam usando pseudocódigo depois traduzindo para código.
    ```
    
- Otimizar trecho
    
    ```markdown
    Tem como dimunir a complexidade dessa parte para otimizar a execução mantendo a mesma funcionalidade? Existe um algorítmo ou boilerplate para isso?
    ```
    
- Otimizar código
    
    ```markdown
    Analise como dimunir a complexidade desse código completo para remover coisas obsoletas,redundântes, overengeneering, e otimizar a execução, mantendo a mesma funcionalidade:
    ```
    
- Otimização e Refatoração
    
    ```markdown
    Analise este código e sugira melhorias:
    
    Por favor, considere:
    1. Simplicidade do código
    2. Performance
    3. Manutenibilidade
    4. Boas práticas
    5. Segurança
    ```
    
- Debug e Testes
    
    ```markdown
    Para este código:
    1. Quais são os possíveis pontos de falha?
    2. Como podemos testar cada funcionalidade?
    3. Quais casos de borda precisamos considerar?
    4. Como implementar tratamento de erros adequado?
    ```
    
- Evolução do Código
    
    ```markdown
    Sugira maneiras de evoluir este código:
    1. Novas funcionalidades que mantêm a essência do código
    2. Como implementar cada nova funcionalidade
    3. Quais desafios técnicos surgiriam
    4. Como o código atual precisaria ser modificado
    ```
    
- Prompt de Análise de Impacto
    
    ```markdown
    Para esta função do jogo:
    [CÓDIGO]
    
    Analise o impacto de cada linha:
    1. O que acontece se esta linha for removida?
    2. O que acontece se esta variável for alterada?
    3. Como este código afeta outras partes do sistema?
    4. Quais são as dependências críticas?
    ```
    

## Recriar

- Entenda o raciocino para recriar
    
    ```markdown
    Sou iniciante, estou aprendendo através de projetos. Me explique o raciocínio passo que eu teria que ter para criar esse código desde o zero até chegar aqui, em linguagem que iniciantes entendam usando pseudocódigo:
    ```
    
- Recriando do Zero
    
    ```markdown
    Me ajude a planejar a recriação dessa exata página do zero.
    Por favor:
    1. Liste os componentes necessários
    2. Sugira uma ordem de implementação
    3. Destaque os principais desafios a serem resolvidos
    4. Forneça pseudo-código para começar
    
    Não me dê o código pronto, apenas me guie no processo de pensamento.
    ```
    
- Técnica de Engenharia Reversa Avançada
    
    ```markdown
    Para este trecho de código:
    [CÓDIGO]
    
    1. Quais problemas este código resolve?
    2. Liste todas as decisões técnicas tomadas
    3. Para cada decisão:
       - Por que foi escolhida esta abordagem?
       - Quais alternativas foram provavelmente consideradas?
       - Quais trade-offs estão envolvidos?
    4. Reconstrua o processo de desenvolvimento:
       - Qual foi provavelmente a primeira versão?
       - Como ela evoluiu até esta versão?
       - Quais refatorações aconteceram no caminho?
    ```

    ---

  ## Utils

  
- Utils
    
    ```markdown
    melhore o layout da pagina pois para mobile está não tão agradavel o feeling (melhore usando princípios de UX e neurociência, tornando-o mais atraente, fácil e persuasivo)
    ```

- Utils
    
    ```markdown
    melhore usando princípios de UX e neurociência, tornando-o mais atraente, fácil e persuasivo.
    ```

- Utils
    
    ```markdown
    melhorar o texto usando princípios de UX writing e neuromarketing, tornando-o mais atraente e fácil de ler:
    ```

- Utils
    
    ```markdown
    deixe mais legivel seguindo boas praticas de ux e neurociencia, pois o texto está raw plain
    ```


- Utils
    
    ```markdown
    Crie um MobileNav.tsx com:
    - Barra superior fixa com logo à esquerda e botões de busca e menu à direita
    - Ao clicar no botão de busca, animar a entrada de uma barra de busca deslizando da direita, escondendo o conteúdo anterior para a esquerda
    - Ao fechar a busca, animar a saída da barra deslizando para direita, revelando o conteúdo anterior
    - Barra inferior fixa com botões de Home, Library e Premium (se usuário premium)
    - Quando a busca estiver aberta, esconder a barra inferior deslizando para baixo
    - Usar shadcn Button e Input
    - Usar Tailwind para animações e estilos
    - Seguir o tema dark com cores em #121212 e #242424
    - Otimizar para mobile first
    - Manter o código DRY usando constantes para classes comuns
    ```

- Utils
    
    ```markdown
    agora complete a mobilenav baseada na desktop, porem otimizada nas boas praticas de mobile nav    
    ```


- Utils
    
    ```markdown
    agora crie um banco de dados fake para ser usado como mockup, use json para salvar e ler o dados de forma a deixar na melhor forma para posteriormente ser convertido para funcional com sql.
    
    faça isso na pasta /mockdb
    
    defina o schema inicial em schema.ts
    
    defina os dados iniciais como se está logado, email e senha etc
    ```

- Utils
    
    ```markdown
    
    arrume isso! mas antes, estude o código e identifique o que pode ser @Web 
    ```

- Utils
    
    ```markdown
    
    arrume isso! mas antes, estude o código e identifique o que pode ser @Web 
    ```

- Utils
    
    ```markdown
    
    antes de criar, leia a doc em @Flet para ver se tem como fazer exatamente isso. Se não crie uma solução mais próxima possível e me fale seu plano para eu confirmar antes de começar
    ```
- Utils
    
    ```markdown
    
    Confira antes, quais arquivos serão modificados, e em cada um, quais techos devem permanecer imutáveis para manter a integridade do código

    Confira na doc do @Flet as sintaxes corretas e boas práticas também.
    ```


    - Utils
    
    ```markdown
    
    agora melhore as cores e componentes icones bordas espaçamentos etc, para ficar um aspecto mais expensive e premium e profissional
    
    melhore tambem a aparcecia do titulo e subtitulo para tb ficar profissional com efeito etc
    ```

## Melhorar Estilo

```markdown
    melhore usando princípios de UX e neurociência, tornando-o mais atraente, fácil e persuasivo.
```

```markdown
    make it juicy:

    https://www.thedevelobear.com/post/microinteractions/ 

    https://www.gamedeveloper.com/game-platforms/how-to-prototype-a-game-in-under-7-days 
```
