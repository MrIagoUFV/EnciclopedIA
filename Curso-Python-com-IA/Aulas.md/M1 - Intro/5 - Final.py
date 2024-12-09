# Simples Assim!
# Saber que o python tem essas capacidades 
# é a única coisa que você precisa 
# para conseguir criar aquele programa de calcular a média.

# Você não precisa saber o nome de cada ferramenta,
# Não precisa decorar como escrever exatamente cada uma,
# Só precisa saber as capacidades e quando usar cada uma.

# E agora conhecendo essas primeiras capacidades,
# Você sabe que pode guardar informações, 
# pode pedir para o usuário digitar,
# pode mostrar mensagens na tela com essas informações guardadas, 
# pode fazer contas, 
# e pode arredondar números.

# Parece bobo? Mas você já consegue criar 
# qualquer programa que use essas capacidades.

# Vamos criar um programa para calcular 
# a hipotenusa de um triângulo retângulo:

# Perguntar o valor do cateto a e salvar em {a}
# Perguntar o valor do cateto b e salvar em {b}
# hipotenusa = raiz quadrada de (a² + b²)
# Mostrar o resultado na tela: "A hipotenusa é {hipotenusa}" com 2 casas decimais

# Pontos de atenção:
## 1. O valor dos catetos deve ser > 0 sempre, caso digite algo inválido, trate o erro, sem quebrar o programa
## Ao mostrar o resultado da hipotenusa, desenhe o trinagulo usando a biblioteca tkinter, e indicando os valores

import math
import tkinter as tk
from tkinter import messagebox

def ler_cateto(mensagem):
    while True:
        try:
            valor = float(input(mensagem))
            if valor > 0:
                return valor
            else:
                print("O valor deve ser maior que zero!")
        except ValueError:
            print("Digite apenas números positivos!")

def desenhar_triangulo(a, b, h):
    # Criar janela
    janela = tk.Tk()
    janela.title("Triângulo Retângulo")
    
    # Criar canvas
    canvas = tk.Canvas(janela, width=400, height=400)
    canvas.pack(pady=20)
    
    # Calcular escala para caber na tela
    escala = 200 / max(a, b, h)
    
    # Posição inicial
    x0, y0 = 100, 300
    
    # Desenhar triângulo
    canvas.create_line(x0, y0, x0 + a*escala, y0, width=2)  # Cateto a
    canvas.create_line(x0 + a*escala, y0, x0 + a*escala, y0 - b*escala, width=2)  # Cateto b
    canvas.create_line(x0, y0, x0 + a*escala, y0 - b*escala, width=2)  # Hipotenusa
    
    # Adicionar textos com mais espaçamento
    canvas.create_text(x0 + (a*escala)/2, y0 + 20, text=f"a = {a:.2f}")
    canvas.create_text(x0 + a*escala + 40, y0 - (b*escala)/2, text=f"b = {b:.2f}")  # Aumentei o espaçamento do b
    canvas.create_text(x0 + (a*escala)/2 - 40, y0 - (b*escala)/2, text=f"h = {h:.2f}")  # Aumentei o espaçamento do h
    
    # Marcar ângulo reto
    tamanho_quadrado = 20
    canvas.create_rectangle(x0 + a*escala - tamanho_quadrado, y0 - tamanho_quadrado, 
                          x0 + a*escala, y0)
    
    janela.mainloop()

# Lendo os catetos
a = ler_cateto("Digite o valor do cateto a: ")
b = ler_cateto("Digite o valor do cateto b: ")

# Calculando a hipotenusa
hipotenusa = math.sqrt(a**2 + b**2)

# Mostrando o resultado
print(f"A hipotenusa é {hipotenusa:.2f}")

# Desenhando o triângulo
desenhar_triangulo(a, b, hipotenusa)







# Eu posso fazer mais mil exemplos aqui
# mas acho melhor seguir para o próximo módulo 
# e mostrar na prática o que to falando.

# a didática desse curso vai ser totalmente diferente
# ao invés de te assustar com mil conceitos teóricos,
# a gente vai focar em aprender as capacidades de cada conceito sob demanda,
# e isso vai fazer total diferença no seu aprendizado.

# Esse curso pode mudar a forma como vc aprende a programar,
# Seja bem vindo ao futuro!
# Bora começar!