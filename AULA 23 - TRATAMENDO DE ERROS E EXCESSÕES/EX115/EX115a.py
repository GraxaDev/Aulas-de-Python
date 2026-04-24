'''1 - visualizar
2 - cadastrar 
3 - Encerrar'''

from estilos import style
from time import sleep

while True:
    resp = style.menu(['Visualizar dados cadastrados', 'Cadastrar novo usuário', 'Sair do sistema'])
    if resp == 1:
         style.cabecalho('Opção 1')
    elif resp == 2:
        style.cabecalho('Opção 2')
    elif resp == 3:
        style.cabecalho('Saindo do sistema... Até logo!')
        break
    else:
        print('\033[31mErro! Digite uma opção válida.\033[0m')
    sleep(2)