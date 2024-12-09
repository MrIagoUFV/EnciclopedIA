"""# Programa para Calcular Descontos em uma Loja
INÍCIO DO PROGRAMA

FUNÇÃO calcular_desconto(valor)
    SE valor < 100 ENTÃO
        RETORNE 0
    SENÃO SE valor < 200 ENTÃO
        RETORNE 10% do valor
    SENÃO SE valor < 500 ENTÃO
        RETORNE 15% do valor
    SENÃO
        RETORNE 20% do valor
    FIM SE
FIM FUNÇÃO

REPETIR INDEFINIDAMENTE
    TENTAR
        SOLICITAR valor_compra ao usuário
        
        SE valor_compra = 0 ENTÃO
            SAIR do loop
        FIM SE
        
        desconto = CHAMAR calcular_desconto(valor_compra)
        valor_final = valor_compra - desconto
        
        EXIBIR valor_compra formatado
        EXIBIR desconto formatado
        EXIBIR valor_final formatado
        
    SE OCORRER ERRO de valor inválido ENTÃO
        EXIBIR mensagem de erro
        CONTINUAR loop
    FIM TENTAR
FIM REPETIR

FIM DO PROGRAMA

# PONTOS DE ATENÇÃO:
- Não permita valores menores que 0
- Ao exibir o cálculo do desconto:
    - pergunte se a pessoa quer continua, se sim, limpe a tela e continue
    - Se não, pare o programa, e exiba uma mensagem de fim:
        - Limpe a tela
        - Mostre um mensagem bonita com ascii art
"""

import os

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def calcular_desconto(valor):
    if valor < 0:
        raise ValueError("O valor não pode ser negativo!")
    if valor < 100:
        return 0
    elif valor < 200:
        return valor * 0.1
    elif valor < 500:
        return valor * 0.15
    else:
        return valor * 0.2

def mostrar_mensagem_fim():
    limpar_tela()
    print("""
    ╔═══════════════════════════════════════╗
    ║                                       ║
    ║        Obrigado por utilizar          ║
    ║      nosso sistema de descontos!      ║
    ║                                       ║
    ║             Volte sempre!             ║
    ║                                       ║
    ╚═══════════════════════════════════════╝
    """)

while True:
    try:
        valor_compra = float(input("Digite o valor da compra (ou 0 para sair): "))
        
        if valor_compra == 0:
            mostrar_mensagem_fim()
            break
            
        desconto = calcular_desconto(valor_compra)
        valor_final = valor_compra - desconto
        
        print(f"\nValor original: R${valor_compra:.2f}")
        print(f"Desconto: R${desconto:.2f}")
        print(f"Valor final: R${valor_final:.2f}\n")
        
        continuar = input("Deseja continuar? (s/n): ").lower()
        if continuar != 's':
            mostrar_mensagem_fim()
            break
            
        limpar_tela()
        
    except ValueError as e:
        if str(e) == "O valor não pode ser negativo!":
            print(e)
        else:
            print("Por favor, digite apenas números!")
