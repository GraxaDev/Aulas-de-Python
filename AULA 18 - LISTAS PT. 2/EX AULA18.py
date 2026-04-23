'''teste = []
teste.append('Miqueias')
teste.append('25')
pessoas=[]
pessoas.append(teste[:])    
teste[0] = 'Maria'
teste[1] = '30'
pessoas.append(teste[:])
print(pessoas)'''

'''galera = [['João', 25], ['Maria', 30], ['Pedro', 20]]
if galera[0][0] == 'João':  
        galera[0][0] = 'Joãozinho'
for p in galera:
    print(f'{p[0]} tem {p[1]} anos de idade.')  '''

galera = []
dado = []
totmai = totmen = 0
for c in range(0, 3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    galera.append(dado[:])
    dado.clear()
print(galera)
for p in galera:
    if p[1] >= 21:
        print(f'{p[0]} é maior de idade.')
        totmai += 1
    else:
        print(f'{p[0]} é menor de idade.') 
        totmen += 1
print(f'Temos {totmai} maiores e {totmen} menores de idade.')