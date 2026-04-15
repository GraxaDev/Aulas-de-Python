#CRIANDO UM DICIONÁRIO PARA ARMAZENAR OS DADOS DE UM ALUNO, INCLUINDO O NOME, AS NOTAS,E CALCÚLA A MÉDIA.
aluno = {}
aluno['nome'] = str(input('Nome: ')).strip()
nota1 = float(input(f'Digite a primeira nota de {aluno["nome"]}: '))
nota2 = float(input(f'Digite a segunda nota de {aluno["nome"]}: '))
media = (nota1 + nota2) / 2
aluno['media'] = media
#VERIFICANDO A SITUAÇÃO DO ALUNO COM BASE NA MÉDIA CALCULADA. SE A MÉDIA FOR MAIOR OU IGUAL A 7, O ALUNO É CONSIDERADO APROVADO; SE A MÉDIA FOR ENTRE 5 E 6.9, O ALUNO ESTÁ EM RECUPERAÇÃO; SE A MÉDIA FOR MENOR QUE 5, O ALUNO É REPROVADO. 
if aluno['media'] >= 7:
    aluno['situacao'] = 'Aprovado'
elif aluno['media'] >= 5:
    aluno['situacao'] = 'Recuperação'
else:
    aluno['situacao'] = 'Reprovado'
print('-=' * 30)
#EXIBINDO O NOME DO ALUNO, A MÉDIA CALCULADA E A SITUAÇÃO DE ACORDO COM A MÉDIA, FORMATANDO A MÉDIA COM UMA CASA DECIMAL.
print(f'Nome do aluno: {aluno["nome"]}')
print(f'Média: {aluno["media"]:.1f}')
print(f'Situação: {aluno["situacao"]}')