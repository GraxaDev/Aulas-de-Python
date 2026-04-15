#Criando uma lista com 3 listas dentro dela, cada uma com 3 elementos, formando uma matriz 3x3.
matriz = [[[], [], []], [[], [], []], [[], [], []]]
#Para preencher a matriz, utilizamos dois loops for aninhados, onde o primeiro loop percorre as linhas e o segundo loop percorre as colunas. Em cada iteração, solicitamos ao usuário que digite um valor para a posição correspondente da matriz.
for i in range(0, 3):
    for j in range(0, 3):
        matriz[i][j] = int(input(f"Digite um valor para a posição [{i}] [{j}]: "))
#Após preencher a matriz, utilizamos novamente dois loops for aninhados para exibir os valores da matriz formatados. O comando print(f"[{matriz[i][j]:^5}]", end="") é utilizado para imprimir cada elemento da matriz centralizado em um campo de 5 caracteres, e o parâmetro end="" evita que o print adicione uma nova linha após cada elemento. Após imprimir cada linha da matriz, utilizamos print() para adicionar uma nova linha.
for i in range(0, 3):
    for j in range(0, 3):
        print(f"[{matriz[i][j]:^5}]", end="")
    print()
