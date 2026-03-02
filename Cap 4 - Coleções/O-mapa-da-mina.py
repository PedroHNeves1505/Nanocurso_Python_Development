lista = ['Python', 'Java', 'JS', 'C++', 'C#']
print(f'Criamos a segyinte lista\n{lista}')

#map  faz com que um comando seja executado em cada item da lista
#Para o resultado de map sair, é oreciso transformalo em list()

mapa = list(map(len, lista))
print(mapa)