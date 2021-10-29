dia = int(input('Digite dia da semana: (1-SEG a 7-DOM)\n'))
preco = float(input('Digite preco do produto em reais:\n'))
opcao = int(input('Digite a opcao do produto: (2-prata 1-ouro)\n'))
a = 0
if dia == 1:
    a = 'seg'
if dia == 2:
    a = 'ter'
if dia == 3:
    a = 'qua'
if dia == 4:
    a = 'qui'
if dia == 5:
    a = 'sex'
if dia == 6:
    a = 'sab'
if dia == 7:
    a = 'dom'

if (dia == 1 or dia == 2 or dia == 3 and opcao == 1):
    total = preco / 2
elif (dia == 4 or dia == 5 and preco > 10 and preco < 100):
    total = preco / 3
elif (dia == 6 and opcao == 2):
    total = preco * 3
else:
    total = preco * 2

print('O preco do produto no dia %s e R$ %.2f' % (a, total))
