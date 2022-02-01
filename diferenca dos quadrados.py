d = int(1)
a = int(0)
b = int(0)
c = int(0)

while (d != 0):
    d = int(input())
    a = ((d - 1) / 2)
    b = (a + 1) ** 2
    c = a**2 
    b = (a + 1) ** 2
    if (d == 0):
      break
    print("%d - %d"% (b, c))
