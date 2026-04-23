
#CRIANDO UM DICIONÁRIO PARA ARMAZENAR AS INFORMAÇÕES DO JOGADOR E UMA LISTA PARA GUARDAR O NÚMERO DE GOLS.
jogador = {}
gol = []
jogador['nome'] = str(input('Nome do jogador: '))
jogador['partidas'] = int(input('Número de partidas jogadas: '))
#COM A RESPOSTA DO NÚMERO DE PARTIDAS, O PROGRAMA SOLICITA A INSERÇÃO DO NÚMERO DE GOLS POR PARTIDAS.
for p in range(jogador['partidas']):
    gol.append(int(input(f'Número de gols na partida {p+1}: ')))
#CRIANDO UM NOVO ELEMENTO NO DICIONÁRIO PARA ARMAZENAR A LISTA DE GOLS E OUTRO PARA CALCULAR O TOTAL DE GOLS, SOMANDO OS VALORES DA LISTA DE GOLS.
jogador['gols'] = gol
jogador['total'] = sum(gol)
print('-=' * 30)
#EXIBINDO AS INFORMAÇÕES DO JOGADOR, INCLUINDO O NOME, O NÚMERO DE PARTIDAS, OS GOLS POR PARTIDA E O TOTAL DE GOLS. CADA INFORMAÇÃO É EXIBIDA DE FORMA FORMATADA PARA MELHOR LEITURA.
print (jogador)
for k, v in jogador.items():
    print(f' - {k} : {v}.')
print('-=' * 30)
print(f'O jogador {jogador["nome"]} jogou {jogador["partidas"]} partidas.')
for i, v in enumerate(jogador['gols']):
    print(f'   => Na partida {i+1}, fez {v} gols.')
print(f'Foi um total de {jogador["total"]} gols.')