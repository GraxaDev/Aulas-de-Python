'''try:
    a = int(input('Digite um número: '))
    b = int(input('Digite outro número: '))
    r = a / b
except (ValueError, TypeError):
    print('\033[0;30;41mTivemos um problema nos tipos de dados que você digitou.\033[m')
except ZeroDivisionError:
    print('\033[0;30;41mNão é possível dividir um número por zero.\033[m')
except KeyboardInterrupt:
    print('\033[0;30;41mO usuário preferiu não informar os dados.\033[m')
else:
    print(f'O resultado de {a} dividido por {b} é {r:.0f}.')
finally:
    print(f'Volte sempre!')'''
op = int(input('Digite:'))
