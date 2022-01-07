def media(valor1, valor2, valor3):

    media = (valor1 * 2 + valor2 * 3 + valor3 * 5) / (2 + 3 + 5)
    return print('MEDIA = {:.1f}'.format(media))

v1 = float(input())
v2 = float(input())
v3 = float(input())

media(v1, v2, v3)