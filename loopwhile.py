#!/usr/bin/python3

cont = 0
# while cont >= 10:
    # print(cont)
    # cont += 1
'''
soma = 0
while True:
    num = int(input("Digite um numero ou 0 para sair: "))
    if num == 0:
        break
    soma += num
print('total: {}'.format(soma))

'''



nome = []

while True:
    x = input('Digite um nome ou S para sair: \n')
    if x.lower().strip() == 's':
        break
    nome.append(x)
print(nome)



