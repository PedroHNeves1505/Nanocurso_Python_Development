import json

with open('arquivo.json', mode='r', encoding='UTF-8') as arquivo:
	obter = arquivo.read()

#json.loads()  serve para converter o string do json em dicionario

conteudo_convertido = json.loads(obter)

print(conteudo_convertido)
