from time import sleep
def contagem(* num):
    for i in range(num[0], num[1]+1, num[2]):
        sleep(0.5)
        print(f'{i}', end=' ')  
    print('FIM!')

contagem(1, 10, 1)
contagem(0, 10, 2)
print('Agora é sua vez de personalizar a contagem!')
ini = int(input('Início: '))
fim = int(input('Fim: '))
pas = int(input('Passo: '))
contagem(ini, fim, pas)