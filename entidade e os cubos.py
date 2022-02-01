r = int(1)
a = int(1)
n = int(input())

for i in range(0, 100000000):
    r += 2 + i
    if a + r <= n:
        a += r
    else:
        print(i + 1)
        break
