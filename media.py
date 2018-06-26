#!/usr/bin/python3
nome = input('Digite o nome do aluno: \n')
nota1 = int(input('Digite a primeira nota: \n'))
nota2 = int(input('Digite a segunda nota: \n'))
# nome = nome.title()
# nome = nome.replace("a","@")
# nome = nome.upper()
# nome = nome.lower()
media = (nota1 + nota2) / 2
print('A media do {} foi de {}'.format(nome.title().replace("a","@").strip(),media))
print(nome)