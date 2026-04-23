from random import randint
from time import sleep

    #CRIANDO UMA FUNÇÃO PARA SORTEAR 5 NÚMEROS E COLOCÁ-LOS EM UMA LISTA
def sorteia(lista):
    print('Sorteando 5 valores da lista: ', end='')
    for c in range(0, 5):
        n = randint(0, 10)
        lista.append(n)
        print(f'{n} ', end='', flush=True)
    sleep(0.5)
    print('PRONTO!')
#CRIANDO UMA FUNÇÃO PARA SOMAR APENAS OS VALORES PARES DE UMA LISTA
def somaPar(lista):
    soma = 0
    for v in lista:
         if v % 2 == 0:
             soma += v
    print(f'Somando os valores pares de {lista}, temos {soma}.')

#PROGRAMA PRINCIPAL
numeros = []
sorteia(numeros)
somaPar(numeros)



