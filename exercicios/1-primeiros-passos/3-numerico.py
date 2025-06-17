data_nascimento = '05-10-1976'
idade_numerica = 46
altura = 1.74

# Descubra o tipo de dado de cada variável acima
print(type(data_nascimento))
print(type(idade_numerica))
print(type(altura))

# Realize uma operação entre dados do tipo string e inteiro
print(data_nascimento*idade_numerica)

# Realize uma operação entre dados do tipo inteiro e float
print(idade_numerica/altura)
print(round(idade_numerica/altura,3))
print(int(idade_numerica/altura))
print(F"eu tenho {int(altura*2)} dias")