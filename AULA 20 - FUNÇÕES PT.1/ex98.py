from time import sleep
#CRIANDO UMA FUNÇÃO PARA CONTAGEM REGRESSIVA E PROGRESSIVA, COM PASSO PERSONALIZADO
def contagem(i, f, p):
    print('-='*20)
    #TRATANDO O PASSO PARA QUE SEJA SEMPRE POSITIVO E DIFERENTE DE ZERO
    if p < 0:
        p*= -1
    if p == 0:
        p = 1
    print(f'Contando de {i} até {f} de {p} em {p}:')
    #SE O INICIO FOR MENOR QUE O FIM, A CONTAGEM É PROGRESSIVA
    if i < f:
        cont = i
        while cont <= f:
            print(f'{cont} ', end='', flush=True)
            sleep(0.5)
            cont += p
        print('Fim!')
    else:
    #SE O INICIO FOR MAIOR QUE O FIM, A CONTAGEM É REGRESSIVA
        cont = i
        while cont >= f:
            print(f'{cont} ', end='', flush=True)
            sleep(0.5)
            cont -= p
        print('FIM!')
    print('=-'*20)

#CONTAGEM DEFINIDA PELO SISTEMA UTILIZANDO A FUNÇÃO CRIADA
contagem(1, 10, 1)
contagem(10, 0, 2)
#CONTAGEM PERSONALIZADA PELO USUÁRIO
print('Agora é sua vez de personalizar a contagem!')
ini = int(input('Início: '))
fim = int(input('Fim: '))
pas = int(input('Passo: '))
contagem(ini, fim, pas)