n = int(input())
p = float(input())
aux = int(0)
alunos = int(0)

while(aux < n):
    aux = aux + 1
    prova1 = float(input())
    prova2 = float(input())
    total = float(prova1 + prova2)
    if prova1 == 0 or prova2 == 0:
        alunos = alunos + 0
    elif total >= p:
        alunos = alunos + 1
    else:
        alunos = alunos + 0

print(alunos)
