#*argumento  aerve para indicar que aquele argumento aguenda mais de 1 variável
# *lista serve para indicar que são todos os itens da lista

def exibe_promocao(*clientes):
	for cliente in clientes:
		print(f'Olá {cliente}!\nQueremos te avisar que a nova X-Wing está em promoção!')
		print()
	
lista_cliente = ['Luke', 'Princesa Leia', 'Mestre Yoda']
exibe_promocao(*lista_cliente)




