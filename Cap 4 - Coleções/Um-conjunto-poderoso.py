#set() retira todos os itens identicos de uma lista ou outros agrupadores de itens
lista = ['Marcos', 'Antonio', 'Pedro', 'Marcos']
print(lista)
set = set(lista)
print(set)

#Também pode ser usada na formação da lisat, trocando [] por {}

lista_set = {'Marcos', 'Antonio', 'Pedro', 'Marcos'}
print(lista_set)

#Para adicionar um elemento usa-se .add()
lista_set.add('Julia')
print(lista_set)

#Para retirar itens identicos um set com o outro usasse .difference_update()

lista_set2 = {'Julia', 'Danielle', 'Otto'}
lista_set.difference_update(lista_set2)
print(lista_set)

# Para retirar um item de um conjunto usa-se .remove()

lista_set2.remove("Otto")
print(lista_set2)