def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except(TypeError, ValueError):
            print(f'\033[31mERRO! Digite um número inteiro válido.\033[0m')
            continue
        except KeyboardInterrupt:
            print('\033[31mO usuário preferiu não digitar este número.\033[0m')
            return 0 
        else:
            return n

def linha(tam=42):
    return '-' * tam

def cabecalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())

def menu(n):
    cabecalho('MENU PRINCIPAL')
    c = 1
    for item in n:
        print(f'\033[1;33m{c} \033[0m- \033[94m{item}\033[0m')
        c +=1
    print(linha())
    opc = leiaInt('Sua opção: ')
    return opc
