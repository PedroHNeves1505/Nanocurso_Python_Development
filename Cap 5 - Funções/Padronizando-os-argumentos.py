#è possivel indicar qual é o tipo do argumento com: argumento:tipo
#Só serve para ajudar outros deves com o código
#Também dá para definir um valor padrão com argumento = 'valor padrão'

def calcular_velocidade_media(distancia:float, tempo:float, unidade_de_medida='km/h'):
	velocidade_media = distancia / tempo
	print(f'A velocidade média do seu trajeto foi {velocidade_media}{unidade_de_medida}.')

calcular_velocidade_media(300,3)
