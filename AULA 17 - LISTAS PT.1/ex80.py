lista = []
# Criando uma lista em ordem sem usar o sort()
for i in range(5):
    n = (int(input(f'Digite um valor: ')))
    #fazendo uma verificação de duplicidade
    if n not in lista:
        #verificando se o número é maior que o último elemento da lista ou se a lista está vazia
        if i == 0 or n > lista[-1]:
            lista.append(n)
            print('Adicionado ao final da lista...')
        #verificando onde o número deve ser inserido na lista para manter a ordem
        else:
            pos = 0
            while pos < len(lista):
                if n < lista[pos]:
                    lista.insert(pos, n)
                    print(f'Valor adicionado na posição {pos}...')
                    break
                pos += 1
    #se o número já estiver na lista, ele não será adicionado
    else:
        print('Valor duplicado! Não será adicionado.')
print('=-'*30)
#exibindo os valores digitados
print(f'Você digitou os valores {lista}')