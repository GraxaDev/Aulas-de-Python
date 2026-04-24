def leiaFloat(msg):
    while True:
        try:
            n = float(input(msg))
        except(TypeError,ValueError):
            print(f'\033[31mERRO! Digite um número inteiro válido.\033[0m')
            continue
        except KeyboardInterrupt:
            print('\033[31mO usuário preferiu não digitar este número.\033[0m')
            return 0
        else:
            return n