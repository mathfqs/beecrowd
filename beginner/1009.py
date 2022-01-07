def salario(salario, venda):
    salarioFinal = salario + venda * 0.15
    return print(f'TOTAL = R$ {salarioFinal:.2f}')

nome = input()
s = float(input())
v = float(input())

salario(s,v)