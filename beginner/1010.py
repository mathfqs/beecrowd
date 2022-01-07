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