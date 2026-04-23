jogador = {}
gol = []
time = []
while True:
    jogador['Nome'] = str(input('Nome do jogador: '))
    partidas = int(input(f'Quantas partidas {jogador["Nome"]} jogou: '))
    gol.clear()
    for g in range(partidas):
        gol.append(int(input(f'Quantos gols na {g+1} partida: ')))
    jogador['Gols'] = gol.copy()
    jogador['Total'] = (sum(gol))
    time.append(jogador.copy())
    while True:
        resp = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
        if resp in 'SN':
            break
        print('ERRO! Digite apenas S ou N: ')
    if resp == 'N':
        break

print('=-' * 20)
print('Cod. ', end='')
for i in jogador.keys():
    print(f'{i:<15}', end='')
print()
for k, v in enumerate(time):
    print(f'{k:<3} ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('=-' * 20)
while True:
    busca = int(input('Mostrar dados de qual jogador? (999 para parar) '))
    if busca == 999:
        print('FINALIZANDO...')
        break
    if busca >= len(time):
        print(f'ERRO! Não existe jogador com código {busca}! Tente novamente.')
    else:
        print(f' -- LEVANTAMENTO DO JOGADOR {time[busca]["Nome"]}:')
        for i, g in enumerate(time[busca]['Gols']):
            print(f'   No jogo {i+1} fez {g} gols.')
print('<< VOLTE SEMPRE >>')
