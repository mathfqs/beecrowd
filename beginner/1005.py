def media(valor1, valor2):

    media = (valor1 * 3.5 + valor2 * 7.5) / (3.5 + 7.5)
    return print('MEDIA = {:.5f}'.format(media))

v1 = float(input())
v2 = float(input())

media(v1, v2)