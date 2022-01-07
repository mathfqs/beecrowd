def salario(n, h, vh):
    salario = h * float(vh)
    return print(f'NUMBER = {n}\nSALARY = U$ {salario:.2f}')

n1 = int(input())
hora = int(input())
valorHora = float(input())

salario(n1, hora, valorHora)