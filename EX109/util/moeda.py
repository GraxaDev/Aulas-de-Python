def metade(n=0, formato=False):
    '''
    -> FUNÇÃO DE LOCALIZAR A METADE DE UM NÚMERO.
    :param n: Número a ser dividido
    :param formato: Se True retorna formatado para moeda em Real. 
                    Se False, retorna o número digitado em float.
    '''
    res = n /2
    return res if formato is False else moeda(res)
def dobro(n=0, formato=False):
    '''
    -> FUNÇÃO PARA DESCOBRIR O DOBRO DE UM NÚMERO.
    :param n: Número a ser multiplicado
    :param formato: Se True retorna formatado para moeda em Real. 
                    Se False, retorna o número digitado em float.
    '''
    res = n * 2
    return res if formato is False else moeda(res)
def aumentar(n = 0, p = 0, formato=False):
    ''' 
    -> FUNÇÃO PARA ACRESCENTAR EM PORCENTAGEM A UM NÚMERO.
    :param n: Número a ser cálculado;
    :param p: Número a ser acrescido para porcentagem;
    :param formato: Se True retorna formatado para moeda em Real. 
                    Se False, retorna o número digitado em float.
    
    '''
    res = n + ( n * p / 100)
    return res if formato is False else moeda(res)
def diminuir(n = 0, p = 0, formato=False):
    '''    
    -> FUNÇÃO PARA DIMINUIR EM PORCENTAGEM A UM NÚMERO.
    :param n: Número a ser cálculado;
    :param p: Número a ser diminuido para porcentagem;
    :param formato: Se True retorna formatado para moeda em Real. 
                    Se False, retorna o número digitado em float.
    '''
    res = n - (n * p / 100)
    return res if formato is False else moeda(res)
def moeda(n = 0, moeda = 'R$'):
    '''
    -> FUNÇÃO PARA A FORMATAÇÃO EM REAL (R$)
    :param n: O número a ser formatado.
    :param moeda: A formatação padrão em Reais (R$)
    '''
    return f'{moeda}{n:.2f}'.replace('.', ',')