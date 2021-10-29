valor = float(input())
if(valor <= 0):
    print('Nao ha conta ou funcionario suficiente para pagar a conta')
n = int(input())
if (n <= 0):
    print('Nao ha conta ou funcionario suficiente para pagar a conta')

else:
    a = float(0)
    total = float(0)
    funcionario = 'exemplo'
    for i in range(1, n+1):
        nome = str(input())
        pago = float(input())
        total = total + pago
        if (pago > a):
            a = pago
            funcionario = str(nome)
        else:
            continue

    print('%s pagou R$ %.1f' % (funcionario, a))

    excendente = total - valor
    if (excendente >= 0):
        print('Valor excedente: sobra R$  %.1f' % excendente)
    elif(excendente < 0):
        excendente = excendente * -1 
        print('Valor insuficiente: falta R$  %.1f' % excendente)
