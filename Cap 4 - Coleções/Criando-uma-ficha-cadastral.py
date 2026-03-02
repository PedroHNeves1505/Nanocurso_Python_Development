opcao = 0
ficha_cadastral = {}
valor = 1

while opcao != 4:
	print('FICHA CADASTRAL')
	print('1 - Adcionar informação')
	print('2 - Recuperar informação')
	print('3 - Exibir a ficha completa')
	print('4 - Sair')
	opcao = int(input('Digite a opção desejada: '))
	
	if opcao == 1:
		key = input('Digite a palavra chave que você quer adicionar: ')
		value = input('Digite o conteúdo que deseja adicionar: ')
		ficha_cadastral.update({key:value})
	elif opcao == 2:
		print('Os campos para recuperar são:')
		for repeticao in ficha_cadastral.keys():
			print(f'\t{repeticao}')
		print('-----------------------')
		chave = input('Digite a chave que deseja recuperar: ')
		if chave in ficha_cadastral:
			print(f'O campo {chave} contém o dado {ficha_cadastral.get(chave)}')
		else:
			print('Chave inexistente.')
	elif opcao == 3:
		print('------------------------------------------')
		print('Ficha Cadastral')
		for key, value in ficha_cadastral.items():
			print(f'{key} - {value}')
		print('------------------------------------------')
	elif opcao == 4:
		print('Obrigado pela preferencia. Volte sempre!')

	else:
		print('Opição inexistente, tente uma valida')
		