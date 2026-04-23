lista = []
while True:
    v = (int(input('Digite um valor: ')))
    lista.sort()
    if v not in lista:
        lista.append(v)
        print('Valor adicionado com sucesso...')
    else:        
        print('Valor duplicado! Não vou adicionar...')
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resp in 'N':
        break
print('=-'*30)
print(f'Você digitou os valores {lista}')