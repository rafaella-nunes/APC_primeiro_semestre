Lasanha = 8.00
Estrogonofe = 11.0
Refrigerante = 3.00
Suco = 2.50
valcomida = 0
valbebida = 0

comida = str(input()).lower()
bebida = str(input()).lower()


if (comida == 'lasanha'):
    valcomida = Lasanha

if (comida == 'estrogonofe'):
    valcomida = Estrogonofe

if (bebida == 'refrigerante'):
    valbebida = Refrigerante
    
if (bebida == 'suco'):
    valbebida = Suco

total = valcomida + valbebida
print('%.2f' % total)
