#= [] Cria uma lista. Igual uma variavel, mas ela armazena informações, só que mais de uma.

lista = ['já estou aqui!']

#.insert() serve para adicionar um item na posição que você deseja
lista.insert(0,'Teste insert')

#.append() serve para adcionar um item no final da lista
lista.append('Teste append')

print(lista) #Mostra todos os itens da lista de forma brusca
print(lista[1]) #Mostra um, ou mais, itens selecionados de forma suave
print(lista[-1]) #Ultimo item da lista, -2 penultimo...

#Com looping
for repeticao in lista:
	print(repeticao)
	
#.pop() remove um item da lista
lista.pop(1)
print(lista)

#.remove() indica o item que quer remover
lista.append(12)
print(lista)
lista.remove(12)
print(lista)

#len() descobre o tamanho da lista
print(len(lista))

print('================================================================')
# Programa que calcula quantas calorias o usuário consumiu no dia
print('Seja bem vindo ao caloric Fiap')
opicao = 0
lista_caloria = []

while opicao != 3:
	print('1 - Adicionar calorias')
	print('2 - Remova calorias')
	print('3 - Receber resultado')
	opicao = int(input('Digite a opição desejada: '))
	if opicao == 1:
		caloria = float(input('Digite a quantidade de calorias consumida: '))
		lista_caloria.append(caloria)
	elif opicao == 2:
		print(lista_caloria)
		remover = int(input('Qual posição está a caloria adicionada erroniamente: '))
		remover = remover - 1
		lista_caloria.pop(remover)
	else:
		print('Opição inválida! Digite outra opição.')

calorias_total = 0

for repeticao in lista_caloria:
	calorias_total = calorias_total + repeticao

media_calorias = calorias_total / len(lista_caloria)

print(f'A quantidade de calorias consumida hoje foi: {calorias_total}')
print(f'A média calórica de cada refeição foi: `{media_calorias}')


