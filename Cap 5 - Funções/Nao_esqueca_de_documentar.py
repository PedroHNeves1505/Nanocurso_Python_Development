# """""" serve para fazer um cmentario/ uma documentação sobre o que tal função do codigo faz

def somar(a:float, b:float):
	"""Função que realiza a soma entre dois valores e retorna o resultado, argumentos a e b são obrigatorios e são do tipo float"""
	return a + b
	
# O diferencial da documentação é que é possivel acessar ela com um codigo usando __doc__
# também é possivel acessar com o help()

print(somar.__doc__)
print(help(somar))