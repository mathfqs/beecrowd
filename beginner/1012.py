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