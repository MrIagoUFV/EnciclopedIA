import requests
from colorama import init, Fore, Style
import time

# Inicializa o Colorama
init()

# ASCII Art Banner
banner = """
╔══════════════════════════════════════╗
║     ENCURTADOR DE URLs - CleanURI    ║
╚══════════════════════════════════════╝
"""

def exibir_loading():
    print(f"{Fore.YELLOW}Processando", end="")
    for _ in range(3):
        time.sleep(0.5)
        print(".", end="", flush=True)
    print(Style.RESET_ALL)

# Limpa a tela e mostra o banner
print("\033[H\033[J")  # Limpa a tela
print(f"{Fore.CYAN}{banner}{Style.RESET_ALL}")

# Solicita a URL ao usuário
print(f"{Fore.GREEN}→ Digite a URL que você deseja encurtar:{Style.RESET_ALL}")
url_original = input(f"{Fore.WHITE}").strip()

# Configuração da requisição para a API da cleanuri
api_url = "https://cleanuri.com/api/v1/shorten"
dados = {
    "url": url_original
}

# Mostra animação de loading
exibir_loading()

# Faz a requisição POST para a API
try:
    resposta = requests.post(api_url, data=dados)

    # Verifica se a requisição foi bem sucedida
    if resposta.status_code == 200:
        # Extrai a URL encurtada da resposta JSON
        url_curta = resposta.json()["result_url"]
        print(f"\n{Fore.GREEN}✓ URL encurtada com sucesso!{Style.RESET_ALL}")
        print(f"\n{Fore.CYAN}URL Original: {Fore.WHITE}{url_original}")
        print(f"{Fore.CYAN}URL Encurtada: {Fore.WHITE}{url_curta}{Style.RESET_ALL}")
    else:
        print(f"\n{Fore.RED}✗ Erro ao encurtar a URL: {resposta.text}{Style.RESET_ALL}")

except requests.exceptions.RequestException as e:
    print(f"\n{Fore.RED}✗ Erro de conexão: {str(e)}{Style.RESET_ALL}")

print(f"\n{Fore.YELLOW}Pressione ENTER para sair...{Style.RESET_ALL}")
input()


