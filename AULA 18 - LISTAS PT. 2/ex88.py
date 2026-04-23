#Importando as bibliotecas necessárias
from random import randint
from time import sleep
print('-'*50)
print(f'{'JOGO DA MEGASENA':^50}')
print('-'*50)
#Solicitando ao usuário a quantidade de jogos que deseja sortear e armazenando o valor em uma variável. O comando input() é utilizado para solicitar a entrada do usuário, e a função int() é utilizada para converter a entrada em um número inteiro.
sort = int(input('Quantos jogos você quer que eu sorteie? '))
print(f'{f" SORTEANDO {sort} JOGOS ":#^50}')
sleep(1)
#Utilizando um loop for para sortear os jogos. O loop externo percorre a quantidade de jogos solicitada pelo usuário, enquanto o loop interno gera 6 números aleatórios entre 1 e 60 para cada jogo. A função randint() é utilizada para gerar os números aleatórios, e a estrutura while é utilizada para garantir que não haja números repetidos em um mesmo jogo. Os jogos são armazenados em uma lista chamada jogo, e a função sorted() é utilizada para exibir os números de cada jogo em ordem crescente.
for i in range(sort):
    jogo = []
    for j in range(6):
        num = randint(1, 60)
        while num in jogo:
            num = randint(1, 60)
        jogo.append(num)
#Exibindo os jogos sorteados utilizando um loop for para percorrer a lista de jogos e imprimir cada jogo formatado. O comando sleep() é utilizado para adicionar uma pausa de 1 segundo entre a exibição de cada jogo, criando um efeito visual mais agradável.
    print(f'Jogo {i+1}: {sorted(jogo)}')
    sleep(1)
print(f'{' BOA SORTE! ':=^50}')