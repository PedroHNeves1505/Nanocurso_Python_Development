#for(por x vezes) ele é um laço de repetição, mas ao invez do while que é enquanto uma condição for feita no for é por quantidade de vezes
#break, ele querba a sequancia.

for contadora in range(10,100,1):
	print(contadora)
	if contadora == 20:
		break
		
print('======================================')
print('Essa é uma calcualdora de fatorial.')
numero = int(input('Digite o valor que você deseja obter o fatorial: '))
valor = 1
contadora = 1

for contadora in range(1,numero + 1,1):
	valor = valor * contadora

print(f'O valor fatorial do numero {numero} é {valor}')
