# E vizualizar exatamente como queremos cada parte:

# - receber 3 notas:

## - mostrar "Digite a primeira nota" e deixar o usuário digitar
## - salvar o que ele digitou como {nota1}
## - mostrar "Digite a segunda nota" e deixar o usuário digitar
## - salvar o que ele digitou como {nota2}
## - mostrar "Digite a terceira nota" e deixar o usuário digitar
## - salvar o que ele digitou como {nota3}

# Agora que temos as notas,
# vamos calcular a média:

## - fazer a conta (nota1 + nota2 + nota3) / 3 
## - salvar o resultado como {media}

# Agora que temos a média,
# vamos exibir o resultado:

## - mostrar "A média do aluno é: {media}"
## - a média precisa estar arredondada para 2 casas decimais

# Pontos de atenção:
## Cada nota deve ser um número entre 0 e 10, e pode ter casas decimais
    ### Se não satisfazer essas condições, trate o erro sem fechar o programa:
        #### Mostre: "Número inválido , digite um número entre 0 e 10" se o erro for número inválido
        #### Mostre: "Digite apenas números!", se a pessoa digitou algo que não um número
## Ao mostrar a média, mostre também uma mensagem baseada na nota do aluno:
### Se média > 6: "Passou! Parabéns!"
### Se média for exatamente 6: "Caraca... Foi por pouco ein, mas passou!"
### Se média for < 6: "Se fudeo"

