from time import sleep

c = ('\033[m',      #0 - SEM COR
    '\033[0;30;41m', #1 - VERMELHO
    '\033[0;30;42m', #2 - VERDE 
    '\033[0;30;43m', #3 - AMARELO
    '\033[0;30;44m', #4 - AZUL
    '\033[0;30;45m', #5 - ROXO
    '\033[7;30m'    #6 - BRANCO
    );


def ajuda(com):
    sleep(1)
    titulo(f'ACESSANDO O MANUAL DO COMANDO \'{com}\'', 4)
    print(c[6], end='')
    help(com)
    print(c[0],end='')
    sleep(2)

def titulo(msg, cor = 0):
    print(c[cor], end='')
    tam = len(msg) + 4
    print('~'* tam)
    print(f'  {msg}  ')
    print('~'* tam)
    print(c[0], end='')

comando = ''
while True: 
    titulo("SISTEMA DE AJUDA PyHELP", 2)
    sleep(1)
    comando = str(input('Digite a função ou biblioteca: ')).strip().lower()
    if comando == "fim":
        break
    else:
        ajuda(comando)
sleep(1)
titulo("ATÉ LOGO!", 1)