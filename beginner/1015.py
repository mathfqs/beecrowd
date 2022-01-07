"""
Leia os quatro valores correspondentes aos eixos x e y de dois pontos quaisquer no plano, p1(x1,y1) e p2(x2,y2) e calcule a distância entre eles, mostrando 4 casas decimais após a vírgula, segundo a fórmula:

Distancia =  

Entrada
O arquivo de entrada contém duas linhas de dados. A primeira linha contém dois valores de ponto flutuante: x1 y1 e a segunda linha contém dois valores de ponto flutuante x2 y2.

Saída
Calcule e imprima o valor da distância segundo a fórmula fornecida, com 4 casas após o ponto decimal.
"""

def distancia(x1,y1,x2,y2):
    distancia = ((x2 - x1)**2 + (y2 - y1)**2)**0.5
    return print(f'{distancia:.4f}')

p1 = input().split(' ')
a = float(p1[0])
b = float(p1[1])

p2 = input().split(' ')
c = float(p2[0])
d = float(p2[1])

distancia(a,b,c,d)