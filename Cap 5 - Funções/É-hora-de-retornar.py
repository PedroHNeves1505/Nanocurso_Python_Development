#return serve para devolver um valor, para deixar essa função mais flexivel

def soma(a,b):
	resultado = a + b
	return resultado
	
print('Calculamos a soma entre dois valores.')
valor1 = int(input('Digite o priemiro valor: '))
valor2 = int(input('Digite o segundo valor: '))

resposta = soma(valor1, valor2)
print(f'O resultado é {resposta}!')
