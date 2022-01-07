"""
Leia 3 valores, no caso, variáveis A, B e C, que são as três notas de um aluno. A seguir, calcule a média do aluno, sabendo que a nota A tem peso 2, a nota B tem peso 3 e a nota C tem peso 5. Considere que cada nota pode ir de 0 até 10.0, sempre com uma casa decimal.

Entrada
O arquivo de entrada contém 3 valores com uma casa decimal, de dupla precisão (double).

Saída
Imprima a mensagem "MEDIA" e a média do aluno conforme exemplo abaixo, com 1 dígito após o ponto decimal e com um espaço em branco antes e depois da igualdade.
"""

def media(valor1, valor2, valor3):

    media = (valor1 * 2 + valor2 * 3 + valor3 * 5) / (2 + 3 + 5)
    return print('MEDIA = {:.1f}'.format(media))

v1 = float(input())
v2 = float(input())
v3 = float(input())

media(v1, v2, v3)