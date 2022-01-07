""""
Leia dois valores inteiros. A seguir, calcule o produto entre estes dois valores e atribua esta operação à variável PROD. A seguir mostre a variável PROD com mensagem correspondente.   

Entrada
O arquivo de entrada contém 2 valores inteiros.

Saída
Imprima a mensagem "PROD" e a variável PROD conforme exemplo abaixo, com um espaço em branco antes e depois da igualdade. 
"""

def multiplicacao(v1, v2):
    valor1 = int(v1)
    valor2 = int(v2)
    PROD = valor1 * valor2

    return print('PROD =', PROD)

valor1 = int(input())
valor2 = int(input())

multiplicacao(valor1,valor2)