# Programa para calcular média de notas

# Agora vamos ler o código linha por linha
# sem nos preocuparmos em decorar
# só explorar o código entender o que cada linha faz

# O input() mostra uma mensagem e espera o usuário digitar algo
# O float() converte o texto digitado em número decimal
# Aqui estamos guardando o número na variável nota1
nota1 = float(input("Digite a primeira nota: "))

# Mesma coisa para nota2
nota2 = float(input("Digite a segunda nota: "))

# E nota3
nota3 = float(input("Digite a terceira nota: "))

# Para calcular a média somamos as 3 notas e dividimos por 3
# O resultado é guardado na variável media
media = (nota1 + nota2 + nota3) / 3

# print() mostra uma mensagem na tela
# f"..." permite incluir variáveis na mensagem usando {}
# :.2f arredonda o número para 2 casas decimais
print(f"A média do aluno é: {media:.2f}")
