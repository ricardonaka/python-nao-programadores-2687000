# Declare 4 variáveis do tipo numérica
x = 1
y = 2
w = 7
z = 4


# Crie uma estrutura condicional para comparar dois números
if x > y:
    print(f' x > y')
else:
    print(f' x < y')


# Se a condição for verdadeira, imprima na tela uma mensagem informando que a condição foi cumprida e informando o número de maior valor


# Se a condição não for cumprida, imprima na tela uma mensagem informando que a condição é negativa e informe o número de maior valor


# Insira outras condições na estrutura condicional usando o elif
if x > y:
    print(f'x > y')
elif w > z:
    print(f'w > z')
else:
    print(f'nada verdadeiro')
# Incremente a estrutura condicional já existente com expressões lógicas utilizando "and" ou "or"
if (x > y) and (w > z):
    print(f'os dois verdadeiros')
elif (x > y) or (w > z):
    print(f'um dos dois verdadeiros')
else:
    print(f'nenhum verdadeiro')
# Crie uma estrutura condicional onde mais de uma condição seja verdadeira, e use apenas a palavra reservada "if"
