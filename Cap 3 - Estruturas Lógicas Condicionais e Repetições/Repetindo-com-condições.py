#while(enquanto)  serve para fazer um loop de repetições
senha = ''
tentativas = 0

while senha != 'python':
	senha = input('Digite a senha secreta: ')
	tentativas = tentativas + 1

print(f'Acesso concedido após {tentativas}° tentativa.')
