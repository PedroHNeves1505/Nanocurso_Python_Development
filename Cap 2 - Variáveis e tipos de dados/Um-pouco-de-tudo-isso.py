#Ficha Cadastral de doadores de sangue
#Pedir: nome, ano, peso, altura
#tem peso e idade minimas para doar

ano = 2026

print('Olá, esta é o cadastro para doadores de sangue')
nome = input('Digite seu nome completo: ')
ano_nascimento = int(input('Digite seu ano de nascimento: '))
peso = float(input('Digite seu peso em Kg: '))
altura = float(input('Digite sua altura em cm: '))

idade = ano - ano_nascimento
tem_peso_minimo = peso > 50
tem_idade_minima = idade >= 16
print('-------------------------------------------------------------------')
print(f'\tNOME: {nome}\n\tIDADE: {idade}\n\tPESO: {peso}Kg\n\tALTURA: {altura}cm\n\tPossui peso mínimo para doar: {tem_peso_minimo}\n\tPossui idade mínima para doar: {tem_idade_minima}')
print('-------------------------------------------------------------------')

