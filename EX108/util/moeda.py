def metade(n=0):
    return n / 2
def dobro(n=0):
    return n * 2
def aumentar(n = 0, p = 0):
    res = n + ( n * p / 100)
    return res
def diminuir(n = 0, p = 0):
    res = n - (n * p / 100)
    return res
def moeda(n = 0, moeda = 'R$'):
    return f'{moeda}{n:.2f}'.replace('.', ',')