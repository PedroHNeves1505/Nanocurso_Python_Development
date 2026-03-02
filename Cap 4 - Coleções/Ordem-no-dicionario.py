# Ordered dict garante que os itens do dicionario fiquem em ordem

from collections import OrderedDict

dicionario_ordenado = OrderedDict()

dicionario_ordenado['Nome'] = 'Pedro'
dicionario_ordenado['Idade'] = 18
dicionario_ordenado['Faculadade'] = 'UAM'

for key, value in dicionario_ordenado.items():
	print(f'{key} -- {value}')

dicionario_ordenado['Faculadade'] = 'Fiap'
print()

for key, value in dicionario_ordenado.items():
	print(f'{key} -- {value}')

dicionario_ordenado.pop('Idade')
print()
for key, value in dicionario_ordenado.items():
	print(f'{key} -- {value}')
	
dicionario_ordenado['Idade'] = 18
print()
for key, value in dicionario_ordenado.items():
	print(f'{key} -- {value}')
	
	
# O ordered dict preserva a ordem por alteração, mas não por deletar e depois reinserir o mesmo item.