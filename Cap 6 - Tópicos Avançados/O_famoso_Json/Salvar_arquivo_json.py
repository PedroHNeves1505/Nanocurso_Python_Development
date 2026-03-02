import json

dicionario = {'nome': 'pedro', 'idade': 18}

#json.dumps() armazena uma string em formato json
#ensure_ascii=  garante que os acentos não sejam corrompidos ou bugados
#indent=  serve para indicar quantos espaços antes do texto tenha

conteudo = json.dumps(dicionario, ensure_ascii=False, indent=4)
with open('arquivo.json', mode='w', encoding='UTF-8') as arquivo:
	arquivo.write(conteudo)

print('Testo salvo em Json salvo corretamente!')


