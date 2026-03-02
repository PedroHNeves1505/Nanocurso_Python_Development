def calcular_velocidade_media(distancia:float, tempo:float, unidade_medida='km.h'):
	if tempo == 0 or distancia == 0:
		return 0
	else:
		velocidade_media = distancia / tempo
	return(f'{velocidade_media}{unidade_medida}')

def calcular_conversao_temperatura(temperatura:float, unidade_medida = 'celcius'):
	if unidade_medida.lower() == 'celcius':
		return temperatura * 1.8 + 32
	elif unidade_medida.lower() == 'fahrenheit':
		return (temperatura - 32) / 1.8
	else:
		return 0
	
def exibir_menu():
	print('MENU')
	print('1 - Calcular velocidade média')
	print('2 - Converter Temperatura')
	print('3 - Sair')
	
def chamar_funcoes():
	opicao = 0
	while opicao != 3:
		exibir_menu()
		opicao = int(input('Qual opição deseja?: '))
		if opicao == 1:
			distancia = float(input('Digite a distancia percorrida: '))
			tempo = float(input('Digite o tempo da viajem: '))
			unidade_medida = input('Informe a unidade de medida usada: ')
			print(f'A velocidade média é {calcular_velocidade_media(distancia, tempo, unidade_medida)} ')
			print()
		elif opicao == 2:
			unidade_medida = input('informe a unidade de medida: ')
			temperatura = float(input(f'Digite a temperatura em {unidade_medida}: '))
			if unidade_medida.lower() == 'celcius':
				unidade_medida_calculada = 'fahrenheit'
			else:
				unidade_medida_calculada = 'celcius'
			print(f'{temperatura}° {unidade_medida} -- {calcular_conversao_temperatura(temperatura, unidade_medida):.2f}°{unidade_medida_calculada}')
			print()
		elif opicao == 3:
			print('Saindo do sistema')
		else:
			print('Opição inválida')
			print()
