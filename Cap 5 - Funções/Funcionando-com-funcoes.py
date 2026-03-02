#Fazendo a função
#def inicia a função (indica que aquilo é uma função)

def calcular_velocidade_media():
	velocidade_media = distancia / tempo
	print(f'A velocidade média do seu trajeto foi {velocidade_media}Km/h.')

distancia = float(input('Digite a distância percorrida em Km: '))
tempo = float(input('Digite o tempo da viagem em hr: '))
calcular_velocidade_media()

