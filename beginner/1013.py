lista = input().split(' ')
lista = [int(i) for i in lista]

maior = max(lista,key=int)

print(f'{maior} eh o maior')
