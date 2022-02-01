a = float(input('Digite o coeficiente A:\n'))
b = float(input('Digite o coeficiente B:\n'))
c = float(input('Digite o coeficiente C:\n'))

r1 = int(0)
r2 = int(0)
delta = ((b**2) - 4 * a * c)

if (delta < 0):
    print('A funcao nao tem raizes reais')
else:
    r1 = ((b * -1) + delta) / (2 * a)
    r2 = ((b * -1) - delta) / (2 * a)
    n = int(r1)
    m = r1 * 10
    s = n * 10
    if(m == s):
        print('Primeira raiz: %.0f'% r1)
        print('Segunda raiz: %.0f'% r2)
    else:
        print('Primeira raiz:', r1)
        print('Segunda raiz:', r2)
