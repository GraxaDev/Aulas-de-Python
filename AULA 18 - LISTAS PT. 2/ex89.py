#CRIANDO UMA LISTA PARA ARMAZENAR OS DADOS DO ALUNO, ONDE CADA ELEMENTO É UMA SUBLISTA COM O NOME, AS NOTAS E A MÉDIA DO ALUNO. O PROGRAMA PERMITE AO USUÁRIO INSERIR VÁRIOS ALUNOS, CALCULAR A MÉDIA DE CADA UM E EXIBIR UM RELATÓRIO FINAL COM OS NOME E MÉDIAS. O USUÁRIO TAMBÉM PODE CONSULTAR AS NOTAS DE UM ALUNO ESPECÍFICO DIGITANDO O NÚMERO CORRESPONDENTE.
aluno = []
#SOLICITANDO AO USUÁRIO QUE INSIRA O NOME E AS NOTAS DE CADA ALUNO, O PROGRAMA CONTINUARÁ INSERINDO ALUNOS ATÉ QUE O USUÁRIO DECIDA PARAR.
while True:
    nome = str(input('Nome: ')).strip()
#VERIFICANDO SE O NOME DO ALUNO JÁ FOI CADASTRADO NA LISTA. SE NÃO FOR, O PROGRAMA SOLICITA AS NOTAS, CALCULA A MÉDIA E ARMAZENA OS DADOS NA LISTA. SE O NOME JÁ EXISTIR, UMA MENSAGEM DE ERRO É EXIBIDA E O USUÁRIO É SOLICITADO A TENTAR NOVAMENTE.
    if nome not in [a[0] for a in aluno]:
        nota1 = float(input('Nota 1: '))
        nota2 = float(input('Nota 2: '))
        media = (nota1 + nota2) / 2
        aluno.append([nome, [nota1, nota2], media])
    else:
        print('Aluno já cadastrado! Tente novamente.')
    resp = str(input('Quer continuar? [S/N] ')).strip().upper()
#SE A RESPOSTA PARA CONTINUAR OU NÃO É INVÁLIDA, O PROGRAMA SOLICITA NOVAMENTE ATÉ QUE SEJA DIGITADA UMA RESPOSTA VÁLIDA (S OU N). SE O USUÁRIO DECIDIR PARAR, O PROGRAMA EXIBE UM RELATÓRIO FINAL COM OS NOME E MÉDIAS DE CADA ALUNO.
    while resp not in 'SN': 
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()
    if resp == 'N':
        break
print('-=' * 30)
#FORMATAÇÃO DA TABELA DE RELATÓRIO FINAL, EXIBINDO O NOME E A MÉDIA DE CADA ALUNO. 
print('-' * 26)
print(f'{"Nº":<3} {"NOME":<10} {"MÉDIA":>8}')
for a in aluno:
    print(f'{aluno.index(a)+1:<3} {a[0]:<10} {a[2]:>8.1f}')
print(f'Foram registrados {len(aluno)} alunos.')
#CALCULANDO A MÉDIA DA SALA SOMANDO AS MÉDIAS DE CADA ALUNO E DIVIDINDO PELO NÚMERO TOTAL DE ALUNOS, EXIBINDO O RESULTADO FORMATADO COM UMA CASA DECIMAL.
mediasala = 0
for a in aluno:
    mediasala += a[2]
mediasala /= len(aluno)
print(f'A média da sala é {mediasala:.1f}')
print('-=' * 30)
#AQUI O USUÁRIO PODE CONSULTAR AS NOTAS DE UM ALUNO ESPECÍFICO DIGITANDO O NÚMERO CORRESPONDENTE. O PROGRAMA CONTINUA PERMITINDO CONSULTAS ATÉ QUE O USUÁRIO DECIDA PARAR DIGITANDO 999. SE O NÚMERO DIGITADO FOR VÁLIDO, AS NOTAS DO ALUNO SÃO EXIBIDAS; CASO CONTRÁRIO, UMA MENSAGEM DE ERRO É MOSTRADA.
while True:
    opc = int(input('Mostrar notas de qual aluno? (999 para parar) '))
    if opc == 999:
        print('FINALIZANDO...')
        break
    if opc <= len(aluno):
        print(f'Notas de {aluno[opc-1][0]} são {aluno[opc-1][1]}')
    else:
        print('Aluno não encontrado! Tente novamente.')