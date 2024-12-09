# Vamos criar um programa para ajudar uma loja a calcular descontos

# FUNÇÕES: Bloco de código reutilizável que recebe um valor e retorna o desconto
# Funções nos ajudam a não repetir código e organizar melhor o programa
def calcular_desconto(valor):
    # CONDICIONAIS: Tomando decisões baseadas em comparações
    # Se o valor for menor que 100, não tem desconto
    if valor < 100:
        return 0
    # Se for entre 100 e 200, desconto de 10%
    elif valor < 200:
        return valor * 0.1  
    # Se for entre 200 e 500, desconto de 15%
    elif valor < 500:
        return valor * 0.15
    # Se for maior que 500, desconto de 20%
    else:
        return valor * 0.2

# LOOPS: Repetindo um bloco de código até uma condição ser atendida
# While True cria um loop infinito que só para quando encontra um break
valor_compra = 1
while valor_compra != 0:
    # TRATAMENTO DE ERROS: Prevenindo que o programa quebre se o usuário digitar algo errado
    try:
        # INPUT: Recebendo dados do usuário e convertendo para número decimal
        valor_compra = float(input("Digite o valor da compra (ou 0 para sair): "))
        
        # Se não for zero, calcula e mostra os valores
        if valor_compra != 0:
            # Usando a função que criamos para calcular o desconto
            desconto = calcular_desconto(valor_compra)
            # OPERADORES MATEMÁTICOS: Subtraindo o desconto do valor original
            valor_final = valor_compra - desconto
            
            # f-strings permitem incluir variáveis dentro de textos usando {}
            # :.2f formata números para mostrar apenas 2 casas decimais
            print(f"\nValor original: R${valor_compra:.2f}")
            print(f"Desconto: R${desconto:.2f}")
            print(f"Valor final: R${valor_final:.2f}")
        
    # Se o usuário digitar algo que não é número, mostra mensagem de erro
    except ValueError:
        print("Por favor, digite apenas números!")

print("Acabou")






