seg = int(input())
dia = int(seg) // 86400
resto = int(seg) % 86400
hora = resto // 3600
resto = resto % 3600
min = resto // 60
seg= resto % 60
print(dia)
print(hora)
print(min)
print(seg)
