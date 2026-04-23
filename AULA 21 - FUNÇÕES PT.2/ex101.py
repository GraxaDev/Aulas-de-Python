#CRIANDO UMA FUNÇÃO
def voto(ano):
    #IMPORTANDO BIBLIOTECA PARA PEGAR O ANO ATUAL
    from datetime import date
    v = date.today().year - ano
    #VERIFICANDO A IDADE E CONFORME A RESPOSTA, RETORNANDO COM A OPÇÃO DE VOTO.
    if v < 18 and v >= 16 or v >=65:
        return f'Com {v} anos o voto é OPCIONAL'
    elif v >= 18:
        return f'Com {v} anos o voto é OBRIGATÓRIO'
    else:
        return f'com {v} anos o voto NÃO É PERMITIDO'

ano = int(input('Digite o seu ano de nascimento: '))
print(voto(ano))