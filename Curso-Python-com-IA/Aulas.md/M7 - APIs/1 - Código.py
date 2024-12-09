# Importa os módulos necessários
import os  # Para operações do sistema operacional
import re  # Para expressões regulares
import firebase_admin  # SDK do Firebase
from firebase_admin import credentials, firestore  # Módulos específicos do Firebase
from Ascii.textoparaascii import criar_ascii_art  # Módulo personalizado para arte ASCII
from google.cloud.firestore import FieldFilter  # Filtros do Firestore

# Obtém o diretório do script atual para localizar o arquivo de credenciais
diretorio_atual = os.path.dirname(os.path.abspath(__file__))  # Pega o caminho absoluto
caminho_credenciais = os.path.join(diretorio_atual, "key.json")  # Monta o caminho completo

# Inicializa a conexão com o Firebase
try:
    # Tenta carregar as credenciais e inicializar o app
    cred = credentials.Certificate(caminho_credenciais)  # Carrega o certificado
    firebase_admin.initialize_app(cred)  # Inicializa o app Firebase
    db = firestore.client()  # Cria o cliente do Firestore
except Exception as e:
    # Tratamento de erro caso falhe a inicialização
    print(f"Erro ao inicializar Firebase: {e}")
    print(f"Verifique se o arquivo key.json está em: {caminho_credenciais}")
    exit(1)  # Encerra o programa com código de erro

def limpar_tela():
    """Função para limpar o terminal, compatível com Windows e Unix"""
    os.system('cls' if os.name == 'nt' else 'clear')

def validar_email(email):
    """Função que valida o formato e tamanho de um email"""
    # Remove espaços e converte para minúsculas
    email = email.strip().lower()
    
    # Verifica se o email segue o padrão correto usando regex
    padrao = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if not re.match(padrao, email):
        print("Email inválido! Use o formato: nome@dominio.com")
        return False
    
    # Verifica se o email não excede o tamanho máximo permitido
    if len(email) > 255:
        print("Email muito longo! Máximo de 255 caracteres.")
        return False
    
    # Verifica o tamanho da parte local do email
    local, dominio = email.split('@')
    if len(local) > 64:
        print("Parte local do email muito longa! Máximo de 64 caracteres antes do @")
        return False
        
    return True

def validar_nome(nome):
    # Sanitiza o input
    nome = nome.strip()
    
    # Verifica se está vazio
    if not nome:
        print("O nome não pode estar vazio!")
        return False
    
    # Permite apenas letras, espaços e acentos
    padrao = r'^[a-zA-ZÀ-ÿ\s]+$'
    if not re.match(padrao, nome):
        print("O nome deve conter apenas letras e espaços!")
        print("Exemplo: João da Silva")
        return False
    
    # Verifica tamanho
    if len(nome) < 2 or len(nome) > 100:
        print("O nome deve ter entre 2 e 100 caracteres!")
        return False
    
    # Verifica espaços múltiplos
    if '  ' in nome:
        print("O nome não pode conter espaços duplos!")
        return False
    
    return True

def validar_senha(senha):
    # Verifica o tamanho mínimo da senha para garantir segurança básica
    if len(senha) < 6:
        print("A senha deve ter pelo menos 6 caracteres!")
        return False
    
    # Usa regex para permitir apenas letras e números, evitando caracteres especiais
    padrao = r'^[a-zA-Z0-9]+$'
    if not re.match(padrao, senha):
        print("A senha deve conter apenas letras sem acento e números!")
        print("Exemplo: Abc123")
        return False
    
    # Limita o tamanho máximo da senha para evitar problemas de armazenamento
    if len(senha) > 20:
        print("A senha deve ter no máximo 20 caracteres!")
        return False
    
    return True

def sanitizar_input(texto):
    """Função auxiliar para sanitizar inputs e evitar injeção de código malicioso"""
    # Verifica se o input é uma string, caso contrário retorna vazio
    if not isinstance(texto, str):
        return ''
    # Remove espaços e caracteres especiais do início e fim
    texto = texto.strip()
    # Limita o tamanho do texto para evitar sobrecarga de memória
    return texto[:1000]  # Limite arbitrário de 1000 caracteres

def esperar_enter():
    """Função que pausa a execução até o usuário pressionar Enter"""
    input("\nPressione Enter para continuar...")

def menu_usuario(nome):
    """Menu principal para usuários comuns"""
    while True:
        # Limpa a tela para melhor visualização
        limpar_tela()
        # Exibe arte ASCII personalizada com o nome
        print(criar_ascii_art(nome))
        print(f"\nOlá {nome}!")
        print("\nMenu do Usuário:")
        print("1. Sair")
        
        # Captura a escolha do usuário
        opcao = input("\nEscolha uma opção: ")
        if opcao == "1":
            return
        else:
            print("\nOpção inválida!")
            esperar_enter()

def menu_admin(nome):
    """Menu principal para administradores com opções de gerenciamento"""
    while True:
        limpar_tela()
        print(criar_ascii_art(nome))
        print("\nMenu do Administrador:")
        print("1. Cadastrar usuário")
        print("2. Listar usuários")
        print("3. Atualizar usuário")
        print("4. Deletar usuário")
        print("5. Sair")

        # Captura e processa a escolha do administrador
        opcao = input("\nEscolha uma opção: ")

        if opcao == "1":
            cadastrar_usuario()
        elif opcao == "2":
            listar_usuarios()
        elif opcao == "3":
            atualizar_usuario()
        elif opcao == "4":
            deletar_usuario()
        elif opcao == "5":
            return
        else:
            print("\nOpção inválida!")
            esperar_enter()

def verificar_colecao_usuarios():
    """Função que verifica e inicializa a coleção de usuários no banco de dados"""
    # Obtém lista de todas as coleções existentes
    colecoes = [col.id for col in db.collections()]
    # Se a coleção 'usuarios' não existir, cria ela
    if 'usuarios' not in colecoes:
        # Cria um documento temporário para inicializar a coleção
        doc_ref = db.collection('usuarios').document('temp')
        doc_ref.set({'temp': True})
        # Remove o documento temporário após criar a coleção
        doc_ref.delete()

def cadastrar_usuario():
    """
    Função para cadastrar um novo usuário no sistema.
    Permite cadastrar nome, email e senha com validações.
    """
    limpar_tela()
    print("Cadastro de Usuário\n")
    print("Digite 'cancelar' a qualquer momento para voltar ao menu\n")
    
    # Garante que a coleção de usuários existe
    verificar_colecao_usuarios()
    
    # Loop para validar o nome
    while True:
        nome = sanitizar_input(input("Digite o nome: "))
        if nome.lower() == 'cancelar':
            return
        if validar_nome(nome):
            break
            
    # Loop para validar o email e verificar duplicidade
    while True:
        email = sanitizar_input(input("Digite o email: "))
        if email.lower() == 'cancelar':
            return
        if not validar_email(email):
            continue
            
        # Verifica se email já existe no banco
        usuarios_ref = db.collection('usuarios')
        if usuarios_ref.where(filter=FieldFilter('email', '==', email.lower())).get():
            print("Email já cadastrado!")
            esperar_enter()
            return
        break
        
    # Loop para validar a senha
    while True:
        senha = sanitizar_input(input("Digite a senha: "))
        if senha.lower() == 'cancelar':
            return
        if validar_senha(senha):
            break
    
    # Loop para confirmar a senha
    while True:
        confirma_senha = sanitizar_input(input("Confirme a senha: "))
        if confirma_senha.lower() == 'cancelar':
            return
        if confirma_senha != senha:
            print("As senhas não coincidem!")
            continue
        break
    
    # Cadastra o novo usuário no banco de dados
    usuarios_ref.add({
        'nome': nome,
        'email': email.lower(),  # Padroniza email em minúsculas
        'senha': senha  # Em ambiente real, usar hash para segurança
    })
    print("\nUsuário cadastrado com sucesso!")
    esperar_enter()

def listar_usuarios():
    """
    Função para listar todos os usuários cadastrados.
    Exibe nome e email de cada usuário.
    """
    limpar_tela()
    print("Lista de Usuários\n")
    
    verificar_colecao_usuarios()
    
    # Busca todos os usuários do banco
    usuarios = db.collection('usuarios').get()
    if not usuarios or len(list(usuarios)) == 0:
        print("Nenhum usuário cadastrado!")
    else:
        # Exibe informações de cada usuário
        for usuario in usuarios:
            dados = usuario.to_dict()
            print(f"Nome: {dados['nome']}")
            print(f"Email: {dados['email']}\n")
    
    esperar_enter()

def atualizar_usuario():
    """
    Função para atualizar dados de um usuário existente.
    Permite modificar nome, email ou senha.
    """
    limpar_tela()
    print("Atualizar Usuário\n")
    print("Digite 'cancelar' a qualquer momento para voltar ao menu\n")
    
    verificar_colecao_usuarios()
    
    # Obtém lista de usuários
    usuarios_ref = db.collection('usuarios')
    usuarios = list(usuarios_ref.get())
    
    if not usuarios:
        print("Nenhum usuário cadastrado!")
        esperar_enter()
        return
    
    # Lista usuários disponíveis
    for i, usuario in enumerate(usuarios, 1):
        dados = usuario.to_dict()
        print(f"{i}. {dados['nome']} - {dados['email']}")
        
    # Seleciona usuário para atualizar
    while True:
        try:
            escolha = input("\nEscolha o usuário (número) ou digite 'cancelar': ")
            if escolha.lower() == 'cancelar':
                return
            escolha = int(escolha)
            if 1 <= escolha <= len(usuarios):
                break
            print("Número inválido!")
        except ValueError:
            print("Digite um número válido!")
    
    # Exibe dados atuais
    usuario_ref = usuarios[escolha-1]
    dados = usuario_ref.to_dict()
    
    limpar_tela()
    print("Dados atuais:")
    print("1. Nome:", dados['nome'])
    print("2. Email:", dados['email'])
    print("3. Senha:", dados['senha'])
    
    # Seleciona campo para atualizar
    while True:
        try:
            campo = int(input("\nQual campo deseja atualizar (1-3): "))
            if 1 <= campo <= 3:
                break
            print("Número inválido!")
        except ValueError:
            print("Digite um número válido!")
    
    # Atualiza nome
    if campo == 1:
        while True:
            novo_valor = sanitizar_input(input("Novo nome: "))
            if novo_valor.lower() == 'cancelar':
                return
            if validar_nome(novo_valor):
                break
    # Atualiza email
    elif campo == 2:
        while True:
            novo_valor = sanitizar_input(input("Novo email: "))
            if novo_valor.lower() == 'cancelar':
                return
            if validar_email(novo_valor):
                novo_valor = novo_valor.lower()
                # Verifica duplicidade de email
                email_existente = usuarios_ref.where(filter=FieldFilter('email', '==', novo_valor)).get()
                if email_existente and email_existente[0].id != usuario_ref.id:
                    print("Email já cadastrado!")
                    continue
                break
    # Atualiza senha
    else:
        while True:
            novo_valor = sanitizar_input(input("Nova senha: "))
            if novo_valor.lower() == 'cancelar':
                return
            if validar_senha(novo_valor):
                # Confirma nova senha
                confirma_senha = sanitizar_input(input("Confirme a nova senha: "))
                if confirma_senha != novo_valor:
                    print("As senhas não coincidem!")
                    continue
                break
    
    campo_atualizar = 'nome' if campo == 1 else 'email' if campo == 2 else 'senha'
    
    # Confirma e realiza atualização
    confirmacao = input("\nConfirmar atualização (s/n)? ").lower()
    if confirmacao == 's':
        usuario_ref.reference.update({campo_atualizar: novo_valor})
        print("\nUsuário atualizado com sucesso!")
    
    esperar_enter()

def deletar_usuario():
    """
    Função para deletar um usuário do sistema.
    Permite selecionar um usuário da lista e confirmar a exclusão.
    """
    # Limpa a tela para melhor visualização
    limpar_tela()
    print("Deletar Usuário\n")
    print("Digite 'cancelar' a qualquer momento para voltar ao menu\n")
    
    # Garante que a coleção de usuários existe
    verificar_colecao_usuarios()
    
    # Obtém lista de usuários do banco
    usuarios = list(db.collection('usuarios').get())
    if not usuarios:
        print("Nenhum usuário cadastrado!")
        esperar_enter()
        return
    
    # Exibe lista numerada de usuários
    for i, usuario in enumerate(usuarios, 1):
        dados = usuario.to_dict()
        print(f"{i}. {dados['nome']} - {dados['email']}")
        
    # Loop para validar escolha do usuário
    while True:
        escolha = input("\nEscolha o usuário para deletar (número) ou digite 'cancelar': ")
        if escolha.lower() == 'cancelar':
            return
            
        try:
            escolha = int(escolha)
            if 1 <= escolha <= len(usuarios):
                break
            print("Número inválido!")
        except ValueError:
            print("Digite um número válido ou 'cancelar'!")
    
    # Obtém referência e dados do usuário selecionado
    usuario_ref = usuarios[escolha-1]
    dados = usuario_ref.to_dict()
    
    # Exibe dados do usuário para confirmação
    print("\nDados do usuário:")
    print("Nome:", dados['nome'])
    print("Email:", dados['email'])
    
    # Confirma e realiza exclusão
    confirmacao = input("\nConfirmar exclusão (s/n)? ").lower()
    if confirmacao == 's':
        usuario_ref.reference.delete()
        print("\nUsuário deletado com sucesso!")
    
    esperar_enter()

def login_usuario():
    """
    Função para realizar login de usuário comum.
    Valida credenciais e direciona para o menu apropriado.
    """
    # Limpa a tela e exibe cabeçalho
    limpar_tela()
    print("Login de Usuário\n")
    print("Digite 'cancelar' a qualquer momento para voltar ao menu\n")
    
    try:
        # Verifica se existem usuários cadastrados
        usuarios = db.collection('usuarios').get()
        if not usuarios or len(list(usuarios)) == 0:
            print("Ainda não existem usuários cadastrados no sistema!")
            esperar_enter()
            return
    except Exception as e:
        print("Ainda não existem usuários cadastrados no sistema!")
        esperar_enter()
        return
    
    # Loop para validar email
    while True:
        email = sanitizar_input(input("Digite seu email: "))
        if email.lower() == 'cancelar':
            return
        if validar_email(email):
            break
            
    # Loop para validar senha
    while True:
        senha = sanitizar_input(input("Digite sua senha: "))
        if senha.lower() == 'cancelar':
            return
        if validar_senha(senha):
            break
    
    # Busca usuário no banco com as credenciais fornecidas
    usuarios_ref = db.collection('usuarios')
    usuario = usuarios_ref.where(
        filter=FieldFilter('email', '==', email)
    ).where(
        filter=FieldFilter('senha', '==', senha)
    ).get()
    
    # Verifica login e direciona para menu apropriado
    if usuario:
        print("\nBem-vindo", usuario[0].to_dict()['nome'])
        esperar_enter()
        menu_usuario(usuario[0].to_dict()['nome'])
    else:
        print("\nLogin inválido!")
        esperar_enter()
def login_admin():
    """
    Função para autenticação de administradores no sistema.
    Valida email e senha e direciona para o menu administrativo.
    """
    # Limpa a tela e exibe cabeçalho
    limpar_tela()
    print("Login de Administrador\n")
    
    # Solicita e valida o email do administrador
    email = input("Digite seu email: ")
    if not validar_email(email):
        print("Email inválido!")
        esperar_enter()
        return
    
    # Solicita e valida a senha do administrador    
    senha = input("Digite sua senha: ")
    if not validar_senha(senha):
        print("Senha inválida!")
        esperar_enter()
        return
    
    # Busca as credenciais do admin no banco
    admin_ref = db.collection('admin').document('login')
    admin = admin_ref.get()
    
    # Verifica se as credenciais são válidas
    if admin.exists and admin.to_dict()['email'] == email and admin.to_dict()['senha'] == senha:
        print("\nBem-vindo", admin.to_dict()['nome'])
        esperar_enter()
        menu_admin(admin.to_dict()['nome'])
    else:
        print("\nLogin inválido!")
        esperar_enter()

def main():
    """
    Função principal que exibe o menu inicial do sistema.
    Permite escolher entre login de admin, usuário ou sair.
    """
    while True:
        # Limpa a tela e exibe menu principal
        limpar_tela()
        print("Bem vindo ao sistema de usuários\n")
        print("1. Login Admin")
        print("2. Login Usuario") 
        print("3. Sair")
        
        # Captura e processa a escolha do usuário
        opcao = input("\nEscolha uma opção: ")
        
        # Direciona para a função apropriada baseado na escolha
        if opcao == "1":
            login_admin()
        elif opcao == "2":
            login_usuario()
        elif opcao == "3":
            limpar_tela()
            print("Até logo!")
            break
        else:
            print("\nOpção inválida!")
            esperar_enter()

# Ponto de entrada do programa
if __name__ == "__main__":
    main()
