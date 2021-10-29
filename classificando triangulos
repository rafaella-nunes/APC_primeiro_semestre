ler = 0

while(ler != 'FIM'):
    aux = 0
    ler = input()
    if(ler != 'FIM'):
        ler = ler.split(' ')
        a = int(ler[0])
        b = int(ler [1])
        c = int(ler[2])
        if (b - c) < a < (b + c):
            aux = aux + 1
        if (a - c) < b < (a + c):
            aux = aux + 1
        if (a - b) < c < (a + b):
            aux = aux + 1
        if(aux == 3):
            if a == b == c:
                print('EQUILATERO')
            elif a == b or b == c or a == c:
                print('ISOSCELES')
            elif a != b != c:
                print('ESCALENO')
        elif(aux != 3):
            print('INVALIDO')
