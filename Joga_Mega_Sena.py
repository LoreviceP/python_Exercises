from random import randint
from time import sleep
lista = []
jogos = list()
cont = 0
tot = 1
print('=-=' * 10)
print('      JOGAR NA MEGA SENA      ')
print('=-=' * 10)
quant = int(input('Quantos jogos você quer que eu sorteie? '))
while tot <= quant:
    cont = 0
    while True:
        n = randint(1, 60)
        if n not in lista:
            lista.append(n)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot += 1
print('-=' * 3, 'SORTEANDO JOGOS', '-=' * 3)
for i, linha in enumerate(jogos):
    print(f'Jogo {i + 1}: {linha}')
    sleep(1)
print('-=' * 5, 'BOA SORTE', '-=' * 5)