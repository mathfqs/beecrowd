"""
Escreva um programa que leia três valores com ponto flutuante de dupla precisão: A, B e C. Em seguida, calcule e mostre:
a) a área do triângulo retângulo que tem A por base e C por altura.
b) a área do círculo de raio C. (pi = 3.14159)
c) a área do trapézio que tem A e B por bases e C por altura.
d) a área do quadrado que tem lado B.
e) a área do retângulo que tem lados A e B.
Entrada
O arquivo de entrada contém três valores com um dígito após o ponto decimal.

Saída
O arquivo de saída deverá conter 5 linhas de dados. Cada linha corresponde a uma das áreas descritas acima, sempre com mensagem correspondente e um espaço entre os dois pontos e o valor. O valor calculado deve ser apresentado com 3 dígitos após o ponto decimal.
"""

def triangulo(base,altura):
    area = base*altura/2
    return print(f'TRIANGULO: {area:.3f}')

def circulo(raio):
    pi = pi = 3.14159
    area = pi * raio**2
    return print(f'CIRCULO: {area:.3f}')

def trapezio(base1, base2, altura):
    area = (base1 + base2) * altura / 2
    return print(f'TRAPEZIO: {area:.3f}')

def quadrado(lado):
    area = lado * lado
    return print(f'QUADRADO: {area:.3f}')

def retangulo(lado1, lado2):
    area = lado1 * lado2
    return print(f'RETANGULO: {area:.3f}')

lista = input().split(' ')
a = float(lista[0])
b = float(lista[1])
c = float(lista[2])

triangulo(a,c)
circulo(c)
trapezio(a,b,c)
quadrado(b)
retangulo(a,b)