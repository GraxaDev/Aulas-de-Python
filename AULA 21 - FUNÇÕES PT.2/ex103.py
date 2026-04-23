
#CRIANDO UMA FUNÇÃO PARA O NOME DO JOGADOR E A QUANTIDADE DE GOLS;
#A FUNÇÃO RECEBE O NOME DO JOGADOR, CASO NÃO SEJA DIGITADO PREENCHE COM "DESCONHECIDO";
#SE A MESA COISA OCORRER COM O CAMPO GOLS, OU SEJA DIGITADO UMA LETRA, O CAMPO É INVALIDADO INFORMANDO "0 GOLS".
def camp(jog = '<desconhecido>', gol = 0):
    print(f'O jogador {jog} fez {gol} gols(s) na temporada.')


n = str(input('Digite o nome do jogador: '))
g = str(input('Número de gols na temporada: ')).strip()

#VERIFICANDO SE A VARIÁVEL G É NUMÉRICO
if g.isnumeric():
    #SE FOR, TRANSFORMA O G DE "STR" PARA "INT"
    g = int(g)
else:
    #SE FOR UM "STR" PREENCHE COM 0
    g = 0

if n.strip() == '':
    #SE A VARIÁVEL "N" QUE É O NOME DO JOGADOR ESTIVER VAZIA, INFORMA A FUNÇÃO APENAS O NÚMERO DE GOLS E A FUNÇÃO PREENCHERÁ COM "<DESCONHECIDO>"
    camp(gol=g)
else:
    #CASO OS CAMPO ESTEJAM CORRETOS, ENVIA PARA A FUNÇÃO AMBOS OS DADOS DIGITADOS PELO USUÁRIO.
    camp(n, g)