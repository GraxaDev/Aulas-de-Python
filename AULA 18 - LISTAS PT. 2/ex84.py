#Criando listas para armazenar os dados temporários e os dados principais, além de variáveis para armazenar o maior e menor peso    
temp = []
princ = []
maior = menor = 0
#Criando um loop para solicitar os dados do usuário e armazená-los nas listas correspondentes, além de verificar o maior e menor peso
while True:
    temp.append(str(input('Nome: ')))
    temp.append(float(input('Peso: ')))
#Verificando se a lista principal está vazia para definir o maior e menor peso, ou comparando o peso atual com o maior e menor peso para atualizá-los, além de armazenar os dados na lista principal
    if len(princ) == 0:
        maior = menor = temp[1]
    else:
        if temp[1] > maior:
            maior = temp[1]
        if temp[1] < menor:
            menor = temp[1]
#Armazenando os dados temporários na lista principal e limpando a lista temporária para a próxima entrada, além de solicitar ao usuário se deseja continuar ou não
    princ.append(temp[:])
    temp.clear()
    resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resp in 'N':
        break
print('-=' * 30)
print(f'Foram cadastradas {len(princ)} pessoas.')
print(f'O maior peso foi de {maior}Kg. Peso de ', end='')
#Percorrendo a lista principal para encontrar as pessoas que possuem o maior peso e exibindo seus nomes, além de percorrer a lista principal para encontrar as pessoas que possuem o menor peso e exibindo seus nomes
for p in princ:
    if p[1] == maior:
        print(f'[{p[0]}]. ', end='') 
print(f'O menor peso foi de {menor}kg. Peso de ', end='')
for p in princ:
    if p[1] == menor:
        print(f'[{p[0]}]. ', end='')
