"""
Neste problema, deve-se ler o código de uma peça 1, o número de peças 1, o valor unitário de cada peça 1, o código de uma peça 2, o número de peças 2 e o valor unitário de cada peça 2. Após, calcule e mostre o valor a ser pago.

Entrada
O arquivo de entrada contém duas linhas de dados. Em cada linha haverá 3 valores, respectivamente dois inteiros e um valor com 2 casas decimais.

Saída
A saída deverá ser uma mensagem conforme o exemplo fornecido abaixo, lembrando de deixar um espaço após os dois pontos e um espaço após o "R$". O valor deverá ser apresentado com 2 casas após o ponto.
"""

def valor(qnt1, valor1, qnt2, valor2):
    total = qnt1 * valor1 + qnt2 * valor2
    return print(f'VALOR A PAGAR: R$ {total:.2f}')

lista1 = input().split(' ')
a = float(lista1[0])
b = float(lista1[1])
c = float(lista1[2])

lista2 = input().split(' ')
d = float(lista2[0])
e = float(lista2[1])
f = float(lista2[2])

valor(b,c,e,f)