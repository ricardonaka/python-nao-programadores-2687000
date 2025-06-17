# Crie uma lista apenas com elementos numéricos
elenum =[0,1,2,3,4,5,6,7,8]
print(elenum)

# Crie uma lista contendo todos os tipos e estrutura de dados que você aprendeu até agora
listtudo =['linkd',3,[1,2,3,4],True]
print(listtudo)

# Imprima na tela apenas os 5 primeiros elementos da lista
print(elenum[0:5])

# Crie um slice na lista para que imprima na tela os elementos de índice par
print(elenum[0:-1:2])

# Remova da lista o último item
elenum.pop(-1)
print(elenum)

# Insira na lista um novo item
elenum.append(99)
elenum.append(5)
print(elenum)

# Remova da lista um item específico
elenum.remove(5)
print(elenum)
elenum.remove(5)

# extend list
elenum.extend(listtudo)
print(elenum)