def ler_nota(mensagem):
    while True:
        try:
            nota = float(input(mensagem))
            if 0 <= nota <= 10:
                return nota
            else:
                print("Número inválido, digite um número entre 0 e 10")
        except ValueError:
            print("Digite apenas números!")

def avaliar_media(media):
    if media > 6:
        return "Passou! Parabéns!"
    elif media == 6:
        return "Caraca... Foi por pouco ein, mas passou!"
    else:
        return "Se fudeo"

# Lendo as notas
nota1 = ler_nota("Digite a primeira nota: ")
nota2 = ler_nota("Digite a segunda nota: ")
nota3 = ler_nota("Digite a terceira nota: ")

# Calculando a média
media = (nota1 + nota2 + nota3) / 3

# Mostrando o resultado
print(f"A média do aluno é: {media:.2f}")
print(avaliar_media(media))
