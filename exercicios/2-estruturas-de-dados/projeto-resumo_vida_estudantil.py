# Nesse exercício coletaremos dados de uma estudante, armazenaremos em um dicionário e imprimiremos na tela esse dados em um formato amigável.

# 1. Solicite a estudante os seguintes dados: nome, ano que conheceu o LinkedIn, ano atual e os cursos realizados no LinkedIn Learning separados por virgula em ordem cronológica
estudante = {}
estudante['nome'] = input('nome ')
estudante['anolk'] = int(input('ano que conheceu o LinkedIn '))
estudante['anohoje'] = int(input('ano atual '))
cursos = input('cursos separados por virgula ')
estudante['cursos']= cursos.split(', ')
# 2. Armazene esses dados em um dicionário

print(estudante)



# 3. Imprima na tela uma string com as informações de nome, ano_conheceu_linkedin, total de anos transcurridos, total de cursos realizados e (apenas) o primeiro e último curso.
total_anos = estudante['anohoje'] - estudante['anolk']
total_cursos = len(estudante['cursos'])
primeiro_curso = estudante['cursos'][0]
ultimo_curso = estudante['cursos'][-1]
print(f'O estudante {estudante["nome"]} esta no linkedin a {total_anos} anos. O primeiro curso foi o {primeiro_curso} e o ultimo curso {ultimo_curso} de um total de {total_cursos} cursos')