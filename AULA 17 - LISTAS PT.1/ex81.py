lista = list()
while True:
    lista.append(int('Digite um valor: '))
    lista.sort(reverse=True)
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resp in 'N':
        break
print('#-#'*30)
print(f'Você digitou {len(lista)} valores.')
print(f'Os valores em ordem decrescente são: {lista}')
if 5 in lista:
    print('O valor 5 faz parte da lista!')
else:
    print('O valor 5 não foi encontrado na lista!')