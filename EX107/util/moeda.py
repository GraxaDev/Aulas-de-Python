def metade(n):
    return n / 2
def dobro(n):
    return n * 2
def aumentar(n, p):
    res = n + ( n * p / 100)
    return res
def diminuir(n, p):
    res = n - (n * p / 100)
    return res
def moeda(n):
    return f'R${n:.2f}'