def contaDigitos():
    if valor < 1000 or valor > 9999:
        print('Ano invalido')


def ehBissexto():
    if valor == 2020:
        print('O ano %d eh bissexto' % valor)
    elif valor > 2020 and valor > 999:
        if valor % 4 == 0 and valor % 100 != 0 or valor % 400 == 0:
            print('O ano %d serah bissexto' % valor)
        else:
            print('O ano %d NAO eh bissexto' % valor)


def Mensagem():
    if valor < 2020 and valor > 999:
        if valor % 4 == 0 and valor % 100 != 0 or valor % 400 == 0:
            print('O ano %d foi bissexto' % valor)
        else:
            print('O ano %d NAO eh bissexto' % valor)


ano = input().split(' ')
for i in ano:
    valor = int(i)
    contaDigitos()
    ehBissexto()
    Mensagem()
