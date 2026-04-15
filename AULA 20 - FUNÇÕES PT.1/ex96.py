#DEFININDO A FUNÇÃO PARA CALCULAR A AREA DE UM TERRENO
def l():
    print("-" * 30)
def area(largura, comprimento):
    a = largura * comprimento
    print(f"A AREA DO TERRENO {largura}x{comprimento} É DE {a:.2f}m²")
l()
print("CALCULO DE AREA DE UM TERRENO")
l()
#ENTRADA DE DADOS
largura = float(input("LARGURA (m): "))
comprimento = float(input("COMPRIMENTO (m): "))
l()
#CHAMANDO A FUNÇÃO PARA CALCULAR A AREA
area(largura, comprimento)
l()