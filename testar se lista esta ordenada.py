# Escreva a funcao lista_esta_ordenada(lista) abaixo:
def lista_ordenada(sequencia):
    a = sorted(sequencia)
    if a == sequencia:
        return True
    else:
        return False




# Programa principal: NAO altere o codigo abaixo. Ele serve apenas para testar a sua funcao.
class RestrictedList(list):

	def __init__(self, sequence):
		for item in sequence:
			self.append(item)

	def reverse(self):
		raise AttributeError('Proibido o uso do metodo reverse()')

	def sort(self, reverse=False):
		raise AttributeError('Proibido o uso do metodo sort()')

	def index(self, value):
		raise AttributeError('Proibido o uso do metodo index()')

def min(x):
	raise NameError('Proibido o uso da funcao min()')

def max(x):
	raise NameError('Proibido o uso da funcao max()')

def sum(x):
	raise NameError('Proibido o uso da funcao sum()')

def list(x):
	raise NameError('Proibido o uso da funcao list()')

def sorted(x):
	raise NameError('Proibido o uso da funcao sorted()')

def main():
	sequencia = eval(input())
	resultado = lista_esta_ordenada(RestrictedList(sequencia))
	print(str(resultado))
main()

