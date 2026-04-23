#Criando uma lista para matriz e uma lista para armazenar os números pares
matriz = [[[], [], []], [[], [], []], [[], [], []]]
pares = []
#Preenchendo a matriz com os valores digitados pelo usuário e armazenando os números pares na lista correspondente. Utilizamos dois loops for aninhados para percorrer as linhas e colunas da matriz, solicitando ao usuário que digite um valor para cada posição. Se o valor digitado for par, ele é adicionado à lista de números pares.
for i in range(3):
    for j in range(3):
        matriz[i][j] = int(input(f'Digite um valor para a posição [{i}] [{j}]: '))
        if matriz[i][j] % 2 == 0:
            pares.append(matriz[i][j])
print('=-'*20)
#Exibindo a matriz formatada utilizando dois loops for aninhados para percorrer as linhas e colunas da matriz. O comando print(f'[{matriz[i][j]:^5}]', end='') é utilizado para imprimir cada elemento da matriz centralizado em um campo de 5 caracteres, e o parâmetro end='' evita que o print adicione uma nova linha após cada elemento. Após imprimir cada linha da matriz, utilizamos print() para adicionar uma nova linha.
for i in range(3):
    for j in range(3):
        print(f'[{matriz[i][j]:^5}]', end='')
    print()
print('=-'*20)
#Calculando e exibindo a soma dos números pares, a soma dos valores da terceira coluna e o maior valor da segunda linha. A função sum() é utilizada para calcular a soma dos números pares, enquanto a função max() é utilizada para encontrar o maior valor da segunda linha da matriz.
print(f'A soma dos números pares é {sum(pares)}')
print(f'A soma dos valores da terceira coluna é: {(matriz[0][2] + matriz[1][2] + matriz[2][2])}')
print(f'O maior valor da segunda linha é: {max(matriz[1])}')