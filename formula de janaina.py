a = int(input())
b = int(input())

for i in range(a, b+1):
    x = int(i)
    x1 = int(x ** 2)
    x2 = int(4 * x)
    x = x1 - x2 + 5
    print(x)
