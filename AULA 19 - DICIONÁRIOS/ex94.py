#CRIANDO UM DICIONÁRIO PARA GUARDAR AS INFORMAÇÕES DE CADA PESSOA, UMA LISTA PARA GUARDAR TODOS OS DADOS E UMA VARIÁVEL PARA CALCULAR A MÉDIA POSTERIORMENTE.
ind = {}
geral = []
media = 0
#LAÇO PARA CADASTRAR AS PESSOAS, VERIFICANDO SE O SEXO E A RESPOSTA DE CONTINUAR SÃO VÁLIDOS.
while True:
    ind['nome'] = input('Nome: ').strip().title()
    ind['sexo'] = input('Sexo: [M/F] ').upper()[0]
    if ind['sexo'] not in 'MF':
       ind['sexo'] = input('ERRO! Por favor, digite apenas M ou F.').upper()[0]
    ind['idade'] = int(input('Idade: '))
    #IMPORTANTE FAZER CÓPIA PARA O DICIONÁRIO, POIS SE NÃO FOR FEITA A CÓPIA, O DICIONÁRIO VAI SER REFERENCIADO E TODOS OS DADOS VÃO SER SUBSTITUÍDOS PELO ÚLTIMO CADASTRO.
    geral.append(ind.copy())
    resp = input('Quer continuar? [S/N] ').upper()[0]
    if resp == 'N':
        break
    elif resp != 'S':   
        resp = str(input('ERRO! Por favor, digite apenas S ou N.'))
print('=-' * 30)

#MOSTRANDO OS RESULTADOS DE ACORDO COM O QUE FOI PEDIDO.
print(f'A) Ao todo temos {len(geral)} pessoas cadastradas.')
#PARA CALCULAR A MÉDIA, SOMAMOS AS IDADES DE TODAS AS PESSOAS E DIVIDIMOS PELO NÚMERO DE PESSOAS CADASTRADAS. O RESULTADO É ARREDONDADO PARA DUAS CASAS DECIMAIS.
media = sum([p["idade"] for p in geral]) / len(geral)
print(f'B) A média de idade é de {media:.2f} anos.')
#PARA VERIFICAR AS MULHERES CADASTRADAS, PERCORREMOS A LISTA DE DICIONÁRIOS E IMPRIMIMOS O NOME DAS PESSOAS QUE TIVEREM O SEXO 'F'.
print('C) As mulheres cadastradas foram: ', end='')
for m in geral:
    if m['sexo'] == 'F':
         print(f'{m["nome"]} ', end='')
print()
#PARA VERIFICAR AS PESSOAS QUE ESTÃO ACIMA DA MÉDIA, PERCORREMOS A LISTA DE DICIONÁRIOS E IMPRIMIMOS O NOME, SEXO E IDADE DAS PESSOAS QUE TIVEREM A IDADE MAIOR OU IGUAL À MÉDIA CALCULADA ANTERIORMENTE.
print('D) Lista das pessoas que estão acima da média: ')
for p in geral:
    if p['idade'] >= media:
        print(f'   Nome = {p["nome"]}; Sexo = {p["sexo"]}; Idade = {p["idade"]};')
print('<< ENCERRADO >>')