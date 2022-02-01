# Escreva o codigo da funcao le_e_devolve_menor() na sequencia:
def le_e_devolve_menor():
   menor = int(input())
   if menor < 0:
       return 0
   while menor >=0:
       aux = int(input())
       if aux < 0:
           return menor
       elif aux < menor:
           menor = aux

# Escreva o codigo da funcao le_e_devolve_maior() na sequencia:
def le_e_devolve_maior():
    maior = int(input())
    if maior < 0:
        return 0
    while maior >= 0:
        aux = int(input())
        if aux < 0:
            return maior
        elif aux > maior:
            maior = aux


# Programa principal (ja implementado, voce nao precisa se preocupar com o codigo a partir deste ponto)
opcao = input()
if opcao == 'menor':
	menor = le_e_devolve_menor()
	print(menor)
elif opcao == 'maior':
	maior = le_e_devolve_maior()
	print(maior)
