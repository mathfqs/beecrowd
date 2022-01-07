""""
Leia dois valores inteiros, no caso para variáveis A e B. A seguir, calcule a soma entre elas e atribua à variável SOMA. A seguir escrever o valor desta variável.

Entrada
O arquivo de entrada contém 2 valores inteiros.

Saída
Imprima a mensagem "SOMA" com todas as letras maiúsculas, com um espaço em branco antes e depois da igualdade seguido pelo valor correspondente à soma de A e B.
"""

def soma(v1, v2):
    valor1 = int(v1)
    valor2 = int(v2)
    valor3 = valor1 + valor2

    return print('SOMA =', valor3)

valor1 = int(input())
valor2 = int(input())

soma(valor1,valor2)