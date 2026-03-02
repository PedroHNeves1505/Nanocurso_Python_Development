#** permite adicionar keywords para os argumentos

def exibe_ficha(**dados):
	print('-----FICHA-----')
	for key, value in dados.items():
		print(f'{key.upper()} -- {value}')

ficha_cliente = {
	'nome' : 'Pedro',
	'estado_civil' : 'solteiro',
	'idade' : 18,
	'faculdade' : 'Fiap'
}
exibe_ficha(**ficha_cliente)

#exibe_ficha(nome='Pedro', estado_civil='Solteiro')