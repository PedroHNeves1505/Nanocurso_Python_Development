#Dicionario padrão  dicionario que permite definir valores padrão.
#Precisa importar o defaultdict do collections
#Para importar usa a estrutura: from 'bibilioteca' import 'arquivo'
# O list entre parenteses é uma das varias repsostas padrões que dá para colocar.

from collections import defaultdict

defaultdict_lista = defaultdict(list)
defaultdict_lista['Nome'] = 'Pedro'
defaultdict_lista['Idade'] = 18

#Diferente do dicionario padrão, se eu solicitar uma key que não eciste ele não da erro, mas sim volta um valor que eu posso definir

print(defaultdict_lista['Faculdade'])
print(defaultdict_lista)

#Criando uma função para configurar a resposta padrão
def resposta_defaultdict():
	return ('Inexistente')
defaultdict_funcao = defaultdict(resposta_defaultdict)
defaultdict_funcao['Nome'] = 'Pedro'
defaultdict_funcao['Idade'] = 18

print(defaultdict_funcao)
print(defaultdict_funcao['Faculdade'])
print(defaultdict_funcao)

# Também é possivel fazer uma resposta padrão usando lambda

defaultdict_lambda = defaultdict(lambda: 'Não disponível')
defaultdict_lambda['Nome'] = 'Pedro'
defaultdict_lambda['Idade'] = 18

print(defaultdict_lambda)
print(defaultdict_lambda['Faculdade'])
print(defaultdict_lambda)
