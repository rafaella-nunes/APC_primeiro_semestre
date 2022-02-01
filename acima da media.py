a = float(input())
b = float(input())
c = float(input())

quant = int(0)
med = (a + b + c)/3

if(a > med):
    quant = quant + 1
if (b > med):
    quant = quant + 1
if(c > med):
    quant = quant + 1

print(quant)
