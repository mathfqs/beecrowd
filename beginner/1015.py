def distancia(x1,y1,x2,y2):
    distancia = ((x2 - x1)**2 + (y2 - y1)**2)**0.5
    return print(f'{distancia:.4f}')

p1 = input().split(' ')
a = float(p1[0])
b = float(p1[1])

p2 = input().split(' ')
c = float(p2[0])
d = float(p2[1])

distancia(a,b,c,d)