print('Bem vinod ao calculador de velocidade média')

#float() outro transt=formador de tipo, mas dessa vez para o flutuante (número que permite casas decimais)

distancia_percorrida = float(input('Informe, em km, a distancia percorrida: '))
tempo_de_percurso = float(input('Digite, em horas, o tempo até a conclusão do percurso: '))

velocidade_media = distancia_percorrida / tempo_de_percurso

#:.2f  limita a quantidade de casas decimais

print(f'A velociade média do percurso foi {velocidade_media:.2f}')

