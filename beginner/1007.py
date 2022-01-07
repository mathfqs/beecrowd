"""
Leia quatro valores inteiros A, B, C e D. A seguir, calcule e mostre a diferença do produto de A e B pelo produto de C e D segundo a fórmula: DIFERENCA = (A * B - C * D).

Entrada
O arquivo de entrada contém 4 valores inteiros.

Saída
Imprima a mensagem DIFERENCA com todas as letras maiúsculas, conforme exemplo abaixo, com um espaço em branco antes e depois da igualdade.
"""

def dif(a,b,c,d):

    r = (a*b-c*d)
    return print('DIFERENCA =',r)

v1 = int(input())
v2 = int(input())
v3 = int(input())
v4 = int(input())

dif(v1,v2,v3,v4)