from estilos import style

def arquivoExiste(nome):
    try:
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True

def criarArquivo(nome):
    try:
        a = open(nome, 'wt+')
        a.close()
    except:
        print('Houve um erro na criação do arquivo.')
    else:
        print(f'Arquivo {nome} criado com sucesso.')

def lerArquivo(nome):
    try:
        a = open(nome, 'rt')
    except:
        print('Erro ao ler o arquivo.')
    else:
        style.cabecalho('PESSOAS CADASTRADAS')
        for n in a:
            dado = n.split(';')
            dado[1] = dado[1].replace('\n', '')
            print(f'{dado[0]:<30}{dado[1]:>3} anos')

    finally:
        a.close()

def cadastrar(arq, nome='desconhecido', idade = 0):
    try:
        a = open(arq, 'at')
    except:
        print('Houve um erro na abertura do arquivo.')
    else:
        try:
            a.write(f'{nome};{idade}\n')
        except:
            print('Houve um ERRO na hora de escrever os dados.')
        else:
            print(f'Novo registro de {nome} adicionado com sucesso.')
        finally:
            a.close()

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

