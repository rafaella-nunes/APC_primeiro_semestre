aux = int(0)
total = float(0)
dias = int(0)
esperado = 0
for i in range(0,7):
    n = float(input())
    total = total + n
    if n >= esperado:
        dias = dias + 1
    esperado = n + 0.5
print('R$ %.2f' % total)
print(dias-1)
