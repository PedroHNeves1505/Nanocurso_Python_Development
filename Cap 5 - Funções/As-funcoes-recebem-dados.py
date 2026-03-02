#Para evitar que dé problema fora da minha maquina e garantir que a função receba os dados pedidos, preciso indicar na função quais dados, fora da função, ela usa

def calcular_velocidade_media(distancia, tempo):
	velocidade_media = distancia / tempo
	print(f'A velocidade média do seu trajeto foi {velocidade_media}Km/h.')

#Mesmo se o nome for diferente, ao criar argumentos, ele transforma (em ordem) as variaveis colocadas com as variaveis pedidas

dist_digitada = float(input('Digite a distância percorrida em Km: '))
tempo_digitado = float(input('Digite o tempo da viagem em hr: '))
calcular_velocidade_media(dist_digitada, tempo_digitado)

calcular_velocidade_media(300,3)



