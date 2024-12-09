# Vamos criar um programa para calcular descontos em uma loja!

# Primeiro, vamos pensar em como vai funcionar:
# - O cliente vai digitar quanto deu a compra dele
# - O programa vai calcular o desconto baseado no valor
# - E mostrar na tela quanto ele vai pagar no final

# Para calcular o desconto, vamos fazer assim:
# - Se a compra for menos de 100 reais, não tem desconto
# - Se for entre 100 e 200 reais, desconto de 10%
# - Se for entre 200 e 500 reais, desconto de 15%  
# - Se passar de 500 reais, desconto de 20%

# O programa precisa:
# 1. Perguntar o valor da compra pro cliente
# 2. Ver quanto de desconto ele tem direito
# 3. Mostrar:
#    - Quanto deu a compra
#    - Quanto ele ganhou de desconto 
#    - Quanto vai pagar no final

# - Deixar o cliente fazer várias contas seguidas
# - Só parar quando ele digitar 0
# - Se ele digitar algo errado (tipo uma letra), 
#   avisar que só pode número e deixar tentar de novo

# PSEUDO-CODIGO:

"""
# Programa para Calcular Descontos em uma Loja
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
