#tupla ()  funciona como a lista mas diferente dele na tupla quando são colocados informações dentro dela, essas informações não podem ser alteradas.
tupla = ('Pedro', '18 anos' , 'Fiap')

print(tupla)

for repeticao in tupla:
	print(repeticao)

print('==============================')
# Coordenadas batalha naval
#É possivel adicionar tuplas em listas fazendo: lista = [(tupla), (tupla)]
inimigos = [(1, 'A'), (5, 'C'), (9, 'D'), (8, 'A'), (2, "I")]
adiversario = 1

#Ao usar 2 variaveis no for, estou desempacotando as tuplas
for x, y in inimigos:
	print(f'Cordenada do adiversario {adiversario} é: X={x} e Y={y}')
	adiversario = adiversario + 1

print('Bem vindo a batalha naval. Para atacar digite a coordenada nas opções abaixo\n\tCoordenadas X= 0 a 9\n\tCoordenadas Y= A a I')

x = int(input('Digite a coordenada X: '))
y = input('Digite a coordenada Y: ')

while len(inimigos) == 0:
	if (x, y) in inimigos:
		print('Parabéns, você acertou um barco inimigo')
		inimigos.remove(x, y)
	else:
		print('Você não acertou ninguem. Tente novamente!')
		
print('Parabéns, você venceu o jogo!')
