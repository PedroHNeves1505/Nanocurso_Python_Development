#mode'r' para leitura do arquivo
#.read() serve para pegar os itens do arquivo
#.readline() serve para mostrar 1 linha
#.readlines() serve para mostrar cada linha como se fosse uma lista
#read().splitlines() mostra como uma lista mas com menos informações


with open('arquivo.txt', mode='r', encoding='UTF-8')as arquivo:
	print(arquivo.read())
	print(arquivo.readline())
	print(arquivo.readlines())
	print(arquivo.read().splitlines())