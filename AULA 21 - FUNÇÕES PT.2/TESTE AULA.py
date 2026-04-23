#def teste():
    #a = 5
    #print(f'A variável A local vale {a}')

#a = 12
#teste()
#print(f'A variável A global vale {a}')

'''def somar(a=0, b=0, c=0):
    s = a + b + c
    return s    
    

r1 = somar(4,7,9)
r2 = somar (2,4)
r3 = somar(2)
print(f'As somas dos cálculos deram {r1}, {r2} e {r3}')'''

def fatorial(num=1, show=False):
    f =1 
    for c in range(num, 0, -1):
        f*=c
        if show==True:
            print(c)
    return f

n = int(input('Digite um número: '))
print(f'O fatorial de {n} é igual a {fatorial(n)}')


'''def par(n=0):
    if n % 2 ==0:
        return True
    else:
        return False

n = int(input('Digite um número para saber se ele é par: '))
if par(n):
    print(f'O número {n} É par.')
else:
    print(f'O número {n} NÃO É par.')'''