#!/usr/bin/python3
nome = ['fabio','carla','maria','joseee']
# nome = [nomes.title() for nomes in nome]#list compression cria uma \
# copia da propria lista formatada
#print('sim' if nome == ' daniel else 'nao')# if ternario

print(nome)
exit()
numeros = list(range(40,100))
# print(nome[2])
# nomes2 = nome[2:]
# print(nomes2)
# nome.append(['marta','goku']) insere no final da lista
print(nome)
nome.insert(0,'goku')#insere na posicao desejada
print(nome)
nome.pop()#retira o ultimo da lista
print(nome)
nome.remove('goku')#remove o item desejadoo
print(nome)
# print(nome[-1][1])
#print(len(nome))
print(numeros)

if 43 in numeros:
    print('sim')
else:
    print('nao')

if 'fabio' in nome:
    print('sim')
else:
    print('nao')