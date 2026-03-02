#Operadores logicos: (&)e/and  (|)ou/or  (!)não/not

conta_A = 10 == 10
conta_B = 10 > 3
conta_C = 10 < 3

if conta_A & conta_B == True:
	print('As contas A e B estão corretas')
else:
	print('As contas A e B estão erradas')

if conta_A | conta_C == True:
	print('As contas A ou B está correta')
else:
	print('As contas A ou B estão erradas')
	
if not conta_C == True:
	print('A conta C é uma afirmação falsa')
else:
	print('A conta C é uma afirmação verdadeira')
	
print('=================================================')

#Teste para acesso de conta

print('Bem vindo ao Banco Fiap')

usuario = input('Digite seu nome de usuário: ')
senha = input('Digite sua senha: ')

if usuario.upper() == 'ADMIN' and senha == '123':
	print('Acesso autorizado.')
else:
	print('Username ou Senha incorretos. Acesso negado!')