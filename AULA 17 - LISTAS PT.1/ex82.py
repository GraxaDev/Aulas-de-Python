# Criando objetos para armazenar os números pares e ímpares
pares = []
impares = []
while True:
    n = int(input('Digite um valor: '))
    # Verificando se o número é par ou ímpar e adicionando à lista correspondente
    if n % 2 == 0:
        pares.append(n)
    else:
        impares.append(n)
    resp = ' '
    # Perguntando ao usuário se deseja continuar, garantindo que a resposta seja válida
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resp in 'N':
        break
print('#-#'*30)
# Exibindo as listas completas, bem como os valores pares e ímpares separadamente
print(f'A lista completa é: {pares + impares}')
print(f'Os valores pares digitados foram: {pares}')
print(f'Os valores ímpares digitados foram: {impares}') 