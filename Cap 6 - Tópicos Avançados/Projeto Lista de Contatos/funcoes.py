import json
agenda = []

def exibir_menu(agenda):
	print('-----------Lista de Contatos-----------')
	print('1 - Incluir contato na agenda')
	print('2 - Incluir uma forma de contato')
	print('3 - Alterar o nome de um contato')
	print('4 - Alterar forma de contato')
	print('5 - Exibir contato')
	print('6 - Exibir toda a agenda')
	print('7 - Excluir um contato')
	print('8 - Exportar agenda para txt')
	print('9 - Exportar agenda para json')
	print('10 - Importar agenda para json')
	print('11 - Sair')
	print('---------------------------------------')
	opicao = int(input('Digite a opição desejada: '))
	while opicao != 11:
		if opicao == 1:
			adicionar_contato(agenda)
		elif opicao == 2:
			incluir_forma_contato(agenda)
		elif opicao == 3:
			alterar_nome_contato(agenda)
		elif opicao == 4:
			alterar_forma_contato(agenda)
		elif opicao == 5:
			exibir_contato(agenda)
		elif opicao == 6:
			exibir_agenda(agenda)
		elif opicao == 7:
			excluir_contato(agenda)
		elif opicao == 8:
			exportar_agenda_txt(agenda)
		elif opicao == 9:
			exportar_agenda_json(agenda)
		elif opicao == 10:
			importar_agenda_json()
		elif opicao == 11:
			print('Saindo do sistema. Volte sempre!')
		else:
			print('Opição inválida!')
			

def adicionar_contato(agenda):
	contatos = {}
	contatos['Nome'] = input('Digite o nome do contato: ')
	nome = contatos['Nome']
	print(f'Deseja adicionar um telefone para {nome}')
	tem_telefone = input('Sim ou Não -> ')
	
	contagem = 1
	while tem_telefone.lower() != 'não':
		contatos[f'Telefone {contagem}'] = int(input('Digite o telefone dele(a): '))
		contagem += 1
		print('Deseja adicionar mais um telefone a esse contato? ')
		tem_telefone = input('Sim ou Não -> ')
	print(f'Deseja adicionar um e-mail para {nome} ')
	tem_email = input('Sim ou Não -> ')
	
	contagem = 1
	while tem_email.lower() != 'não':
		contatos[f'e-mail {contagem}'] = input('Digite o e-mail dele(a): ')
		contagem += 1
		print('Deseja adicionar mais um e-mail a esse contato')
		tem_email = input('Sim ou Não -> ')
	print(f'Deseja adicionar um endereço para {nome}? ')
	tem_endereco = input('Sim ou Não -> ')
	
	contagem = 1
	while tem_endereco.lower() != 'não':
		contatos[f'endereço {contagem}'] = input('Digite o endereço dele(a): ')
		contagem += 1
		print('Deseja adicionar mais um endereço a esse contato')
		tem_endereco = input('Sim ou Não -> ')
	agenda.append(contatos)
	print('--- Contato Salvo! ---')
	print('---------------------------------------')
	exibir_menu(agenda)
	

def incluir_forma_contato(agenda):
	encontrar_contato = input('Digite o nome do contato: ')
	
	for contatos in agenda:
		if contatos['Nome'].lower() == encontrar_contato.lower():
			nome = contatos['Nome']
			print(f'Deseja adicionar um telefone para {nome}')
			contagem = 0
			for key in contatos.keys():
				if 'Telefone' in key:
					contagem += 1
				
			tem_telefone = input('Sim ou Não -> ')
			while tem_telefone.lower() != 'não':
				contatos[f'Telefone {contagem}'] = int(input('Digite o telefone dele(a): '))
				contagem += 1
				print('Deseja adicionar mais um telefone a esse contato? ')
				tem_telefone = input('Sim ou Não -> ')
			print(f'Deseja adicionar um e-mail para {nome} ')
			tem_email = input('Sim ou Não -> ')
			contagem = 0
			
			for key in contatos.keys():
				if 'e-mail' in key:
					contagem += 1
			while tem_email.lower() != 'não':
				contatos[f'e-mail {contagem}'] = input('Digite o e-mail dele(a): ')
				contagem += 1
				print('Deseja adicionar mais um e-mail a esse contato')
				tem_email = input('Sim ou Não -> ')
			print(f'Deseja adicionar um endereço para {nome}? ')
			tem_endereco = input('Sim ou Não -> ')
			
			for key in contatos.keys():
				if 'endereço' in key:
					contagem += 1
			while tem_endereco.lower() != 'não':
				contatos[f'endereço {contagem}'] = input('Digite o endereço dele(a): ')
				contagem += 1
				print('Deseja adicionar mais um endereço a esse contato')
				tem_endereco = input('Sim ou Não -> ')
			agenda.append(contatos)
			print('--- Informações de contato atualizadas! ---')
			print('---------------------------------------')
			exibir_menu(agenda)
			
			
			
def alterar_nome_contato(agenda):
	encontrar_contato = input('Digite o nome do contato: ')
	
	for contatos in agenda:
		if contatos['Nome'].lower() == encontrar_contato.lower():
			novo_nome = input('Digite o novo nome do contato: ')
			contatos['Nome'].update(novo_nome)
	exibir_menu(agenda)
	
def alterar_forma_contato(agenda):
	encontrar_contato = input('Digite o nome do contato: ')
	
	for contatos in agenda:
		if contatos['Nome'].lower() == encontrar_contato.lower():
			nome = contatos['Nome']
			alterar_contato = input('Qual forma de contato você deseja alterar(Telefone, e-mail, endereço): ')
			
			if alterar_contato.lower() == 'telefone':
				del contatos['Telefone']
				print(f'Deseja adicionar um telefone para {nome}')
				tem_telefone = input('Sim ou Não -> ')
				contagem = 1
				while tem_telefone.lower() != 'não':
					contatos[f'Telefone {contagem}'] = int(input('Digite o telefone dele(a): '))
					contagem += 1
					print('Deseja adicionar mais um telefone a esse contato? ')
					tem_telefone = input('Sim ou Não -> ')
			
			elif alterar_contato.lower() == 'e-mail':
				del contatos['e-mail']
				print(f'Deseja adicionar um e-mail para {nome} ')
				tem_email = input('Sim ou Não -> ')
				contagem = 1
				while tem_email.lower() != 'não':
					contatos[f'e-mail {contagem}'] = input('Digite o e-mail dele(a): ')
					contagem += 1
					print('Deseja adicionar mais um e-mail a esse contato')
					tem_email = input('Sim ou Não -> ')
				
			elif alterar_contato.lower() == 'endereço':
				del contatos['endereço']
				print(f'Deseja adicionar um endereço para {nome}? ')
				tem_endereco = input('Sim ou Não -> ')
				contagem = 1
				while tem_endereco.lower() != 'não':
					contatos[f'endereço {contagem}'] = input('Digite o endereço dele(a): ')
					contagem += 1
					print('Deseja adicionar mais um endereço a esse contato')
					tem_endereco = input('Sim ou Não -> ')
			else:
				print('Forma de contato não encontrada! ')
			agenda.append(contatos)
			print('--- Contato Atualizado! ---')
			print('---------------------------------------')
			exibir_menu(agenda)


def exibir_contato(agenda):
	encontrar_contato = input('Digite o nome do contato: ')
	
	for contatos in agenda:
		if contatos['Nome'].lower() == encontrar_contato.lower():
			print('--- Contato encontrado! ---')
			for key, value in contatos.items():
				print(f'{key} -- {value}')
		else:
			print('Contato não encontrado!')
	exibir_menu(agenda)
	
def exibir_agenda(agenda):
	print('--- Agenda ---')
	for repeticao in agenda:
		print(repeticao)
	exibir_menu(agenda)


def excluir_contato(agenda):
	encontrar_contato = input('Digite o nome do contato: ')
	
	for contatos in agenda:
		if contatos['Nome'].lower() == encontrar_contato.lower():
			agenda.remove(contatos)
			print('Contato removido com sucesso!')
			break
	else:
		print('Contato não encontrado!')
	exibir_menu(agenda)
			

def exportar_agenda_txt(agenda):
	agenda_txt = agenda
	with open('contatos.txt', mode='w', encoding='UTF-8') as arquivo_contatos:
		arquivo_contatos.write(agenda_txt)
	print('Arquivo expotado com sucesso!')
	exibir_menu(agenda)
	
def exportar_agenda_json(agenda):
	agenda_json = json.dumps(agenda, ensure_ascii=False, indent=4)
	with open('contatos.json', mode='w', encoding='UTF-8' )as arquivo_contatos:
		arquivo_contatos.write(agenda_json)
	print('Arquivo expotado com sucesso!')
	exibir_menu(agenda)
	
def importar_agenda_json():
	with open('contatos.json', mode='r', encoding='UTF-8') as arquivo_contato:
		json.load(arquivo_contato)
	exibir_menu(agenda)
