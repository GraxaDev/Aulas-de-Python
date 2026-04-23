from utilidadescev import moeda
from utilidadescev import dado

p = dado.leiaDado('Digite o preço: R$')
print(moeda.resumo(p, 35, 22))