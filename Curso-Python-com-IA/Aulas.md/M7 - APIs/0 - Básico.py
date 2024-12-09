# Programa simples para testar a API da Brasil API

# Ler um ddd e retornar a lista de cidades que pertencem ao ddd

# Mostre a mensagem inicial: "Digite o ddd que você deseja consultar: ":
# Use a API do Brasil API para obter os dados
# Retorne da seguinte forma:
    # Cidades do DDD {ddd}:
    # -------------------------
    # cidade1
    # cidade2
    # ...
    # Estado: {estado}

import requests
import json
import os
import time
from datetime import datetime, timedelta
from unidecode import unidecode
from colorama import init, Fore, Back, Style
import platform

# Inicializa o colorama
init(autoreset=True)

# Lista de DDDs válidos no Brasil (baseado em dados da ANATEL)
DDDS_VALIDOS = [
    11, 12, 13, 14, 15, 16, 17, 18, 19,  # São Paulo
    21, 22, 24, 27, 28,                   # Rio de Janeiro e Espírito Santo
    31, 32, 33, 34, 35, 37, 38,          # Minas Gerais
    41, 42, 43, 44, 45, 46, 47, 48, 49,  # Paraná e Santa Catarina
    51, 53, 54, 55,                      # Rio Grande do Sul
    61, 62, 63, 64, 65, 66, 67, 68, 69,  # Centro-Oeste e Norte
    71, 73, 74, 75, 77, 79,              # Bahia e Sergipe
    81, 82, 83, 84, 85, 86, 87, 88, 89,  # Nordeste
    91, 92, 93, 94, 95, 96, 97, 98, 99   # Norte e Maranhão
]

CACHE_FILE = 'ddds_cache.json'
CACHE_VALIDITY_DAYS = 7

def limpar_tela():
    """Limpa a tela do terminal de acordo com o sistema operacional"""
    os.system('cls' if platform.system() == 'Windows' else 'clear')

def mostrar_banner():
    """Mostra o banner do programa"""
    banner = """
    ██████╗ ██████╗ ██████╗     ██████╗ ██████╗  █████╗ ███████╗██╗██╗     
    ██╔══██╗██╔══██╗██╔══██╗    ██╔══██╗██╔══██╗██╔══██╗██╔════╝██║██║     
    ██║  ██║██║  ██║██║  ██║    ██████╔╝██████╔╝███████║███████╗██║██║     
    ██║  ██║██║  ██║██║  ██║    ██╔══██╗██╔══██╗██╔══██║╚════██║██║██║     
    ██████╔╝██████╔╝██████╔╝    ██████╔╝██║  ██║██║  ██║███████║██║███████╗
    ╚═════╝ ╚═════╝ ╚═════╝     ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝╚═╝╚══════╝
    """
    print(Fore.CYAN + banner + Style.RESET_ALL)
    print(Fore.YELLOW + "\n    Consulta de DDDs por Cidade" + Style.RESET_ALL)
    print(Fore.GREEN + "    Desenvolvido com Brasil API\n" + Style.RESET_ALL)

def normalizar_texto(texto):
    """Remove acentos e converte para maiúsculas"""
    return unidecode(texto.upper().strip())

def carregar_cache():
    """Carrega dados do cache se existirem e forem válidos"""
    if os.path.exists(CACHE_FILE):
        try:
            with open(CACHE_FILE, 'r', encoding='utf-8') as f:
                cache = json.load(f)
                cache_date = datetime.fromisoformat(cache['last_update'])
                if datetime.now() - cache_date < timedelta(days=CACHE_VALIDITY_DAYS):
                    return cache['data']
        except (json.JSONDecodeError, KeyError, ValueError):
            pass
    return None

def salvar_cache(data):
    """Salva os dados no cache com a data atual"""
    cache = {
        'last_update': datetime.now().isoformat(),
        'data': data
    }
    with open(CACHE_FILE, 'w', encoding='utf-8') as f:
        json.dump(cache, f, ensure_ascii=False, indent=2)

def mostrar_progresso(atual, total):
    """Mostra uma barra de progresso colorida em ASCII"""
    porcentagem = (atual / total) * 100
    barra = '█' * int(porcentagem // 2)
    espacos = ' ' * (50 - len(barra))
    print(f'\r{Fore.YELLOW}Carregando DDDs: [{Fore.GREEN}{barra}{espacos}{Fore.YELLOW}] {porcentagem:.1f}%', 
          end='', flush=True)

def obter_dados_ddds():
    """Obtém dados de todos os DDDs da API com tratamento adequado"""
    print(f"{Fore.CYAN}Iniciando carregamento dos dados dos DDDs...{Style.RESET_ALL}")
    
    dados_ddds = {}
    total = len(DDDS_VALIDOS)
    
    for i, ddd in enumerate(DDDS_VALIDOS, 1):
        try:
            time.sleep(0.5)
            url = f"https://brasilapi.com.br/api/ddd/v1/{ddd}"
            resposta = requests.get(url, timeout=10)
            
            if resposta.status_code == 200:
                dados_ddds[str(ddd)] = resposta.json()
            
            mostrar_progresso(i, total)
            
        except requests.RequestException as e:
            print(f"\n{Fore.RED}Erro ao consultar DDD {ddd}: {e}{Style.RESET_ALL}")
            continue
    
    print(f"\n{Fore.GREEN}Carga de dados concluída!{Style.RESET_ALL}")
    return dados_ddds

def obter_coordenadas_cidade(cidade, estado):
    """Obtém as coordenadas de uma cidade usando a API do Nominatim"""
    try:
        # Formata a busca com cidade e estado
        busca = f"{cidade}, {estado}, Brazil"
        
        # Faz a requisição para o Nominatim (OpenStreetMap)
        url = "https://nominatim.openstreetmap.org/search"
        params = {
            "q": busca,
            "format": "json",
            "limit": 1
        }
        headers = {
            "User-Agent": "DDD_Clima_App/1.0"  # Identificação do app (boa prática)
        }
        
        response = requests.get(url, params=params, headers=headers, timeout=10)
        
        if response.status_code == 200:
            dados = response.json()
            if dados:
                return {
                    "lat": float(dados[0]["lat"]),
                    "lon": float(dados[0]["lon"])
                }
    except Exception as e:
        print(f"{Fore.RED}Erro ao obter coordenadas: {e}{Style.RESET_ALL}")
    return None

def obter_previsao_tempo(lat, lon):
    """Obtém a previsão do tempo usando a API do Open-Meteo"""
    try:
        url = "https://api.open-meteo.com/v1/forecast"
        params = {
            "latitude": lat,
            "longitude": lon,
            "current": ["temperature_2m", "relative_humidity_2m", "precipitation", 
                       "weather_code", "wind_speed_10m"],
            "timezone": "America/Sao_Paulo"
        }
        
        response = requests.get(url, params=params, timeout=10)
        
        if response.status_code == 200:
            return response.json()
    except Exception as e:
        print(f"{Fore.RED}Erro ao obter previsão: {e}{Style.RESET_ALL}")
    return None

def traduzir_clima(codigo):
    """Traduz os códigos WMO de tempo para português"""
    codigos = {
        0: "Céu limpo",
        1: "Parcialmente limpo",
        2: "Parcialmente nublado",
        3: "Nublado",
        45: "Neblina",
        48: "Neblina com formação de gelo",
        51: "Garoa leve",
        53: "Garoa moderada",
        55: "Garoa intensa",
        56: "Garoa congelante leve",
        57: "Garoa congelante intensa",
        61: "Chuva fraca",
        63: "Chuva moderada",
        65: "Chuva forte",
        66: "Chuva congelante leve",
        67: "Chuva congelante forte",
        71: "Neve fraca",
        73: "Neve moderada",
        75: "Neve forte",
        77: "Grãos de neve",
        80: "Pancadas de chuva fracas",
        81: "Pancadas de chuva moderadas",
        82: "Pancadas de chuva violentas",
        85: "Pancadas de neve fracas",
        86: "Pancadas de neve fortes",
        95: "Tempestade",
        96: "Tempestade com granizo leve",
        99: "Tempestade com granizo forte"
    }
    return codigos.get(codigo, "Desconhecido")

def mostrar_previsao(cidade, previsao):
    """Mostra a previsão do tempo formatada"""
    if not previsao or "current" not in previsao:
        print(f"{Fore.RED}Dados de previsão indisponíveis{Style.RESET_ALL}")
        return
    
    current = previsao["current"]
    
    print(f"\n{Fore.CYAN}Previsão do tempo para {cidade.upper()}:")
    print(f"{Fore.YELLOW}-------------------------{Style.RESET_ALL}")
    print(f"{Fore.GREEN}Temperatura: {current['temperature_2m']}°C")
    print(f"Umidade: {current['relative_humidity_2m']}%")
    print(f"Precipitação: {current['precipitation']} mm")
    print(f"Velocidade do vento: {current['wind_speed_10m']} km/h")
    print(f"Condição: {traduzir_clima(current['weather_code'])}{Style.RESET_ALL}")

def encontrar_cidades_duplicadas(cidade_norm, dados_ddds):
    """Encontra todas as ocorrências de uma cidade nos diferentes DDDs"""
    cidades_encontradas = []
    
    for ddd, dados in dados_ddds.items():
        cidades_norm = [normalizar_texto(city) for city in dados["cities"]]
        if cidade_norm in cidades_norm:
            # Encontra o nome original da cidade (com acentuação)
            idx = cidades_norm.index(cidade_norm)
            nome_original = dados["cities"][idx]
            cidades_encontradas.append({
                "nome": nome_original,
                "estado": dados["state"],
                "ddd": ddd
            })
    
    return cidades_encontradas

def consultar_ddds_cidade(dados_ddds):
    """Consulta os DDDs de uma cidade e mostra a previsão do tempo"""
    while True:
        limpar_tela()
        mostrar_banner()
        
        cidade = input(f"{Fore.CYAN}Digite o nome da cidade (ou 'sair' para encerrar): {Style.RESET_ALL}")
        
        if cidade.lower() in ['sair', 'exit', 'q', 'quit']:
            print(f"\n{Fore.YELLOW}Obrigado por usar o programa!{Style.RESET_ALL}")
            break
            
        if not cidade.strip():
            input(f"{Fore.RED}Nome da cidade não pode estar vazio. Pressione ENTER para continuar...{Style.RESET_ALL}")
            continue
            
        cidade_norm = normalizar_texto(cidade)
        
        # Encontra todas as ocorrências da cidade
        cidades_encontradas = encontrar_cidades_duplicadas(cidade_norm, dados_ddds)
        
        if not cidades_encontradas:
            print(f"\n{Fore.RED}Nenhuma cidade encontrada com o nome: {cidade}{Style.RESET_ALL}")
            input(f"\n{Fore.YELLOW}Pressione ENTER para continuar...{Style.RESET_ALL}")
            continue
        
        cidade_selecionada = None
        
        # Se encontrou mais de uma cidade com o mesmo nome
        if len(cidades_encontradas) > 1:
            print(f"\n{Fore.YELLOW}Foram encontradas várias cidades com esse nome:{Style.RESET_ALL}")
            for i, c in enumerate(cidades_encontradas, 1):
                print(f"{Fore.CYAN}{i}. {c['nome']} - {c['estado']}{Style.RESET_ALL}")
            
            while True:
                try:
                    opcao = int(input(f"\n{Fore.YELLOW}Digite o número da cidade desejada: {Style.RESET_ALL}"))
                    if 1 <= opcao <= len(cidades_encontradas):
                        cidade_selecionada = cidades_encontradas[opcao-1]
                        break
                    else:
                        print(f"{Fore.RED}Opção inválida. Tente novamente.{Style.RESET_ALL}")
                except ValueError:
                    print(f"{Fore.RED}Por favor, digite um número válido.{Style.RESET_ALL}")
        else:
            cidade_selecionada = cidades_encontradas[0]
        
        # Exibe os resultados para a cidade selecionada
        print(f"\n{Fore.GREEN}Informações para {cidade_selecionada['nome']} - {cidade_selecionada['estado']}:")
        print(f"{Fore.YELLOW}-------------------------{Style.RESET_ALL}")
        print(f"{Fore.CYAN}DDD: {cidade_selecionada['ddd']}{Style.RESET_ALL}")
        
        # Obtém e mostra a previsão do tempo
        coordenadas = obter_coordenadas_cidade(cidade_selecionada['nome'], cidade_selecionada['estado'])
        if coordenadas:
            previsao = obter_previsao_tempo(coordenadas["lat"], coordenadas["lon"])
            mostrar_previsao(cidade_selecionada['nome'], previsao)
        
        input(f"\n{Fore.YELLOW}Pressione ENTER para continuar...{Style.RESET_ALL}")

def main():
    """Função principal do programa"""
    limpar_tela()
    mostrar_banner()
    
    # Tenta carregar do cache primeiro
    dados_ddds = carregar_cache()
    
    # Se não há cache válido, obtém os dados da API
    if dados_ddds is None:
        dados_ddds = obter_dados_ddds()
        salvar_cache(dados_ddds)
    
    consultar_ddds_cidade(dados_ddds)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n\n{Fore.YELLOW}Programa encerrado pelo usuário.{Style.RESET_ALL}")
    except Exception as e:
        print(f"\n{Fore.RED}Erro inesperado: {e}{Style.RESET_ALL}")

