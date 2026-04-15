from datetime import date
#CRIANDO UM DICIONÁRIO PARA ARMAZENAR AS INFORMAÇÕES DE UM TRABALHADOR, INCLUINDO NOME, IDADE, CARTEIRA DE TRABALHO, ANO DE CONTRATAÇÃO, SALÁRIO E ANO DE APOSENTADORIA. 
reg = {}
reg['nome'] = str(input('Nome: ')).strip()
ano = int(input('Ano de nascimento: '))
reg['idade'] = date.today().year - ano
reg['ctps'] = int(input('Carteira de trabalho (0 não tem): '))
#VERIFICANDO SE O USUÁRIO POSSUI CARTEIRA DE TRABALHO. SE SIM, O PROGRAMA SOLICITA O ANO DE CONTRATAÇÃO E O SALÁRIO, CALCULANDO O ANO DE APOSENTADORIA COM BASE NA REGRA DE 35 ANOS DE CONTRIBUIÇÃO. SE O USUÁRIO NÃO TIVER CARTEIRA DE TRABALHO, O PROGRAMA PULA ESSAS ETAPAS E EXIBE AS INFORMAÇÕES COLETADAS ATÉ O MOMENTO.
if reg['ctps'] != 0:
    reg['contratação'] = int(input('Ano de contratação: '))
    reg['salário'] = float(input('Salário: R$'))
    reg['aposentadoria'] = reg['contratação'] + 35 - ano
print('-=' * 30)
for k, v in reg.items():
    print(f' - {k} : {v}.')   