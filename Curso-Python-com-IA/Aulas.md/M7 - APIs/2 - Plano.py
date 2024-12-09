# Plano do Projeto

## 1. Criar usando o SDK do Firebase
## Eu criei um projeto no Firebase
## E também criei um banco de dados com o Firestore
## E aí eu criei uma conta de serviço para autenticar no Firebase
## E baixei a chave json para a raiz do projeto
## O arquivo se chama key.json

## Projeto: criar um sistema de cadastro de usuários
## Ao abrir o programa, o usuário vê uma tela de login do administrador

## Tela de login:
## "Bem vindo ao sistema de usuários"

## Escolher uma opção:
## 1. Login Admin
## 2. Login Usuario
## 3. Sair

## Se o usuário escolher 2. Login Usuario:
    ## "Digite seu email:" -> email do usuário (valide se é um email válido no formato nome@dominio.com) -> confira com o db
    ## "Digite sua senha:" -> senha do usuário (valide se tem mais de 6 caracteres) -> confira com o db
    ## "Bem-vindo {nome}" ou "Login inválido" ou "Senha inválida"
    ## "Aperte Enter para continuar..." -> volta para o login ou vai para o menu
    ## db:
        ## Collection: usuarios
            ## Podem ter varios documentos, um para cada usuario
            ## Cada documento tem os campos: nome, email, senha
    ## Ao tentar fazer o login, o sistema verifica se o email e a senha batem com algum documento na collection "usuarios"
    ## Se sim, ele vai para o menu de usuario e mostra "Olá {nome}" e o menu de opções: 1. Sair (trate a entrada errada)
    ## Se não, ele volta para o login e mostra "Login inválido"

## Se o usuário escolher 1. Login Admin:
    ## "Digite seu email:" -> email do admin (valide se é um email válido no formato nome@dominio.com) -> confira com o db
    ## "Digite sua senha:" -> senha do admin (valide se tem mais de 6 caracteres) -> confira com o db
    ## "Bem-vindo {nome}" ou "Login inválido" ou "Senha inválida"
    ## "Aperte Enter para continuar..." -> volta para o login ou vai para o menu
    ## db:
        ## {nome} -> nome do admin no campo "nome" do documento "login" na collection "admin"
        ## senha -> senha do admin no campo "senha" do documento "login" na collection "admin"
        ## email -> email do admin no campo "email" do documento "login" na collection "admin"
        ## CRUD: Create, Read, Update, Delete
    ## Ao fazer o login, o admin vê um menu com cinco opções (CRUD+Sair):
        ## 1. Cadastrar usuario
        ## 2. Listar usuarios
        ## 3. Atualizar usuario
        ## 4. Deletar usuario
        ## 5. Sair

        ## 1. Cadastrar usuario
            ## O admin insere o nome, email e senha do usuário
            ## O sistema valida se o email já está cadastrado
            ## Se sim, ele avisa que o email já está cadastrado
            ## Se não, ele cadastra o usuário e volta para o menu
        ## 2. Listar usuarios
            ## O admin vê a lista dos nomes e emails de todos os usuários cadastrados
            ## Volta para o menu
        ## 3. Atualizar usuario
            ## O admin escolhe o usuario que quer atualizar (lista numerada de nomes e emails) e pede para escolher um número para selecionar o usuario
            ## O sistema mostra o nome, email e senha do usuário escolhido (cada campo em uma linha com um número) e pede para escolher um número para selecionar o campo que quer atualizar
            ## O admin edita o campo escolhido, o sistema mostra os novos dados e pede para confirmar (s/n)
            ## Se sim, o sistema atualiza o usuário e volta para o menu
            ## Se não, ele volta para o menu
        ## 4. Deletar usuario
            ## O admin escolhe o usuario que quer deletar (lista numerada de nomes e emails) e pede para escolher um número para selecionar o usuario
            ## O sistema mostra os dados do usuario escolhido e pede para confirmar (s/n)
            ## Se sim, o sistema deleta o usuario e volta para o menu
            ## Se não, ele volta para o menu
        ## 5. Sair
            ## Volta para o login

## Tratamento de erros:
    ## Tente fazer o tratamento de erros o mais completo possível para cada entrada de dados
    ## Tratar a entrada errada do usuario
    ## Tratar a entrada errada do admin

## Pontos de atenção:
    ## Limpar a tela sempre que mudar de tela, mas usar input para esperar o usuário apertar Enter para continuar (o mesmo para quando der erro)
    ## Mostrar o nome do usuario/admin que está logado em ascii art usando a biblioteca ascii na raiz do projeto "from Ascii.textoparaascii import criar_ascii_art"
    ## Usar a função criar_ascii_art(texto) para criar o ascii art (retorna uma string)
