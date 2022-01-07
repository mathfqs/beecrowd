def media(kilometros, litros):
    medio = kilometros/litros
    return print(f'{medio:.3f} km/l')

a = int(input())
b = float(input())

media(a, b)