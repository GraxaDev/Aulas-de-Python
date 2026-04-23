def metade(n):
    return n / 2
def dobro(n):
    return n * 2
def aumentar(n, p):
<<<<<<< HEAD
    res = n + ( n * p / 100)
    return res
def diminuir(n, p):
    res = n - (n * p / 100)
    return res
=======
    a = n / p + n 
    return a
def diminuir(n, p):
    b = p / 100
    a = n * b 
    return n - a
>>>>>>> 7615448285fe6c8b45d2040ef2ac7e91239b90ec
def moeda(n):
    return f'R${n:.2f}'