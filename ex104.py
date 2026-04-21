#CRIANDO UMA FUNÇÃO PARA VERIFICAR SE O INPUT É NUMÉRICO
def leiaInt(msg):
    #CRIAMOS PARÂMETROS DE VERIFICAÇÃO
    ok=False
    valor = 0
    while True:
        #A VARIÁVEL "N" RECEBE O INPUT COMO "STRIN/STR" DO USUÁRIO
        n = str(input(msg))
        #SE A VARIÁVEL FOR NUMÉRICA, TRANSFORMAMOS DE STR PARA INT E CONVERTEMOS O "OK" DE FALSE PARA TRUE
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            #SE A VARIÁVEL "N" CONTINUAR COMO "STR" EXIBE UMA MENSAGEM NO TERMINAL ATÉ QUE O USUÁRIO DIGITE UM TEXTO NUMÉRICO VÁLIDO
            print(f'\033[31mERRO! Digite um número inteiro válido.\033[0m')
        #SE O USUÁRIO DIGITAR O TEXTO NUMÉRICO, O SISTEMA ENCERRA O LOOP E SAI DO LAÇO
        if ok:
            break
    return valor

n = leiaInt('Digite um número: ')
print(f'O número digitado é o {n}')