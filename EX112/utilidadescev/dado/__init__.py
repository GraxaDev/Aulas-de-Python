def leiaDado(msg):
    valido = False
    while not valido:
        entrada = str(input(msg)).replace(',', '.').strip()
        if entrada.isalpha() or entrada == '':
            print(f'\033[1;31mERRO! "{entrada}" é um valor inválido.\033[m')
        else:
            valido = True
            return float(entrada)
