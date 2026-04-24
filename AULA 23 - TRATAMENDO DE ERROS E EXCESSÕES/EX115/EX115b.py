from estilos import style
from arquivo import documents
from time import sleep

arq = 'dados.txt'
if not documents.arquivoExiste(arq):
    documents.criarArquivo(arq)


while True:
    resp = style.menu(['Visualizar dados cadastrados', 'Cadastrar novo usuário', 'Sair do sistema'])
    if resp == 1:
    #OPÇÃO DE LISTAR UM CONTEÚDO DO ARQUIVO
         documents.lerArquivo(arq)
    elif resp == 2:
        style.cabecalho('NOVO CADASTRO')
        nome = str(input('Nome:'))
        idade = documents.leiaInt('Idade:')
        documents.cadastrar(arq, nome, idade)
    elif resp == 3:
        style.cabecalho('Saindo do sistema... Até logo!')
        break
    else:
        print('\033[31mErro! Digite uma opção válida.\033[0m')
    sleep(2)