# Nesse exercício coletaremos dados de uma estudante, armazenaremos em um dicionário e imprimiremos na tela esse dados em um formato amigável.

# 1. Solicite a estudante os seguintes dados: nome, ano que conheceu o LinkedIn, ano atual e os cursos realizados no LinkedIn Learning separados por virgula em ordem cronológica
nome = input('nome ')
anolk = input('ano que conheceu o LinkedIn ')
anohoje = input('ano atual ')
cursos = input('cursos separados por virgula ')
est01 ={'nome':nome,'anolk':anolk,'anohoje':anohoje,'cursos':cursos}
print(est01.keys())
print(est01.values())
print(est01['cursos'])
# 2. Armazene esses dados em um dicionário


# 3. Imprima na tela uma string com as informações de nome, ano_conheceu_linkedin, total de anos transcurridos, total de cursos realizados e (apenas) o primeiro e último curso.
