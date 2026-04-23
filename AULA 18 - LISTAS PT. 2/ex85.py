'''#Criando objetos para armazenar os números pares e ímpares, e a lista final de números
par = []
impar = []
numeros = []
#Solicitando ao usuário que digite 7 valores e armazenando-os nas listas correspondentes
for c in range(7):
    n = int(input(f'Digite o {c+1}º valor: '))
    #Verificando se o número é par ou ímpar e armazenando-o na lista correspondente, além de ordenar as listas
    if n % 2 == 0:
        par.append(n)
        par.sort()
    else:
    #Verificando se o número é par ou ímpar e armazenando-o na lista correspondente, além de ordenar as listas
        impar.append(n)
        impar.sort()
#Concatenando as listas de números pares e ímpares para criar a lista final de números
numeros = par + impar
print(f'Os números pares digitados foram: {par}')
print(f'Os números ímpares digitados foram: {impar}')'''

n = [[], []]
valor = 0
for c in range(7):
    valor = int(input(f'Digite o {c+1}º valor: '))
    if valor % 2 == 0:
        n[0].append(valor)
    else:
        n[1].append(valor)
n[0].sort()
n[1].sort() 
print(f'Os números digitados foram: {n}')
print(f'Os números pares digitados foram: {n[0]}')
print(f'Os números ímpares digitados foram: {n[1]}')
