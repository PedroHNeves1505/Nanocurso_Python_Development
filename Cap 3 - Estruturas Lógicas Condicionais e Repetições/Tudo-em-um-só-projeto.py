#Projeto menu de opições
opicao = 0

while opicao != 3:
	print('1 - Receber um elogio.')
	print('2 - Resolver um fatorial.')
	print('3 - Sair')
	opicao = int(input('Selecione a opição desejada: '))
	if opicao == 1:
		print('--------------------------')
		print('Você é inteligente!')
		print('--------------------------')
	elif opicao == 2:
		fatorial = 1
		print('--------------------------')
		numero = int(input('Digite o valor que deseja saber o fatorial: '))
		for multiplicador in range(1, numero + 1, 1):
			fatorial = fatorial * multiplicador
		print(f'O fatorial de {numero} é {fatorial}.')
		print('--------------------------')
	elif opicao == 3:
		print('--------------------------')
		print('Agradecemos pela preferencia. Volte sempre!')
	else:
		print('--------------------------')
		print('Opição não valida, tente outra opição.')
		print('--------------------------')
		
