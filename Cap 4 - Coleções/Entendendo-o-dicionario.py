#Dicionario  para criar basta criar uma variavel e colocar um {} em branco

dicionario = {
	'nome': 'Pedro', 'idade': 18, 'Faculdade': 'Fiap', 'Curso': 'Ciência da Computação'
}

print(dicionario)

print(dicionario['nome'])

dicionario['Gênero'] = 'Masculino'

print(dicionario)

#para mostrar as keys do dicionario usa-se .keys()

print(dicionario.keys())
for repeticao_key in dicionario.keys():
	print(repeticao_key)

#para mostrar os valores do dicionario usa-se .values()

print(dicionario.values())
for repeticao_value in dicionario.values():
	print(repeticao_value)
	
#para mostrar em lista as keys com os valores usa-se .items()

for repeticao_items_keys, repeticao_items_values in dicionario.items():
	print(f'{repeticao_items_keys} --- {repeticao_items_values}')
	
#para testar se no dicionario existe uma key especifica usa-se .get()

print(dicionario.get('CPF'))

#.setdefault() serve para criar uma item no dicionario caso ele ainda não exista, caso já exista ele não altera.

#.update() serve para adcionar/atualizar o dicionario

dicionario.setdefault('Estudando', 'Python')
dicionario.setdefault('Estudando', 'Java')
print(dicionario)
