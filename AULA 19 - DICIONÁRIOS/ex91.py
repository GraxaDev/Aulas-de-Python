from random import randint
from time import sleep
from operator import itemgetter
#CRIANDO UM DICIONÁRIO PARA GUARDAR OS JOGADORES E SEUS RESPECTIVOS VALORES
players = {}
#USANDO UM LAÇO PARA GERAR UM NÚMERO ALEATÓRIO ENTRE 1 E 6 PARA CADA JOGADOR
print('Valores sorteados:')
for k in range(1, 5):
    players[f'Jogador {k}'] = randint(1, 6)
    print(f'Jogador {k} jogou {players[f"Jogador {k}"]}')
    sleep(1)
print('-=' * 30)
#ORDENANDO O DICIONÁRIO PELO VALOR DE CADA JOGADOR EM ORDEM DECRESCENTE 
ranking = sorted(players.items(), key=itemgetter(1), reverse=True)
print('Ranking dos jogadores:')
#USANDO UM LAÇO PARA EXIBIR O RANKING DOS JOGADORES, MOSTRANDO A POSIÇÃO, O NOME DO JOGADOR E O VALOR QUE ELE OBTIVEU. CADA EXIBIÇÃO É SEGUIDA DE UMA PAUSA DE 1 SEGUNDOS PARA MELHORAR A LEITURA.
for i, v in enumerate(ranking):
    print(f'{i+1}º lugar: {v[0]} com {v[1]}')
    sleep(1)
