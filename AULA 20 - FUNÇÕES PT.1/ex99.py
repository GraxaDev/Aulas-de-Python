from time import sleep
#CRIANDO UMA FUNÇÃO PARA ANALISAR OS VALORES ARMAZENADOS
def valor(*valor):
    print('-='*20)
    sleep(1)
    print(f'Analisando os valores passados...')
    #CONTAGEM E MAIOR RECEBEM UM NÚMERO INICIAL PARA QUE SEJAM ATUALIZADOS DURANTE A ANÁLISE DOS VALORES
    cont = maior = 0
    #ANALISANDO OS VALORES PARA REALIZAR A CONTAGEM E VERIFICAÇÃO DO MAIOR NÚMERO
    for v in valor:
        cont+= 1
        if v > maior:
            maior = v
    print(f'Os valores informados foram: ', end='')
    for v in valor:
        sleep(0.5)
        print(f'{v} ', end='', flush=True)
    print()
    sleep(1)
    print(f'Foram informados {cont} valores ao todo.')
    sleep(1)
    print(f'O maior valor informado foi {maior}.')
    print('-='*20)

#CÓDIGO CLEAN COM FORMA SIMPLES E DIRETA DE SE OBTER O RESULTADO, UTILIZANDO AS FUNÇÕES LEN() E MAX() PARA CONTAR A QUANTIDADE DE VALORES E ENCONTRAR O MAIOR VALOR, RESPECTIVAMENTE.
    '''for v in valor:
        print(f'{v} ', end='', flush=True)
        sleep(0.5)
    print(f'Foram informados {len(valor)} valores ao todo.')
    if len(valor) > 0:
        sleep(1)
        print(f'O maior valor informado foi {max(valor)}.')
    print('-='*20)'''

valor(2, 9, 4, 5, 7, 1)
valor(4, 7, 0)
valor(1, 2)
valor(6)
valor(0)