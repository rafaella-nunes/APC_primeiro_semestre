d,r,l,p,g = input().split(" ")

d = int(d)
r = int(r)
l = int(l)
p = int(p)
g = int(g)

a = l * 10
km = (d - a) / 10
gasolina = km * g
disp = d // (p + 1)

if(d <= a):
    r = r - gasolina
    print('Pode viajar.')
    print('R$: %.0f' % r)

elif(d > a >= disp and r >= gasolina):
    r = r - gasolina
    print('Pode viajar.')
    print('R$: %.0f' % r)

else:
    print('Nao pode viajar.')

