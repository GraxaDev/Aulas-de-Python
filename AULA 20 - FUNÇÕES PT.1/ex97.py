#CRIANDO UMA FUNÇÃO PARA ESCREVER UMA MENSAGEM COM UM FORMATO ESPECIAL
def escreva(msg):
    #CALCULANDO O TAMANHO DA MENSAGEM PARA DEFINIR O TAMANHO DA BORDA
    tam = len(msg) + 4
    print('~' * tam)
    print(f'{msg}'.center(tam))
    print('~' * tam)
#ENTRADA DE DADOS
msg = str(input("DIGITE UMA MENSAGEM: "))
#CHAMANDO A FUNÇÃO PARA ESCREVER A MENSAGEM
escreva(msg)