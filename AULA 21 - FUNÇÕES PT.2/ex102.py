#CRIANDO UMA FUNÇÃO PARA CÁLCULO DO FATORIAL
def fatorial(n, show=False):
    #CRIANDO UM MANUAL PARA ESTA DEFINIÇÃOFUNÇÃO
    '''fatorial (n, show=False)
        -> Calcula o fatorial de um número .
        :param n: O número a ser cálculado;
        :param show: (opcional) Mostrar ou não a conta
        :return: o valor do Fatorial de um número n.
        '''
    print('='*30)
    f = 1
    #REALIZANDO O CÁLCULO DO FATORIAL
    for v in range(n, 0, -1):
        f*=v
        #CRIANDO UMA CONDIÇÃO DE QUE SE FOR VERDADEIRO, POSSA RETORNAR DE FORMA FORMATADA O CÁLCULO DO FATORIAL 
        if show == True:
            print (v, end='')
            if v > 1:
                print(' x ', end=' ')
            else:
                print(' = ', end = '')
    return f



help(fatorial)
print(fatorial(5, show=True))