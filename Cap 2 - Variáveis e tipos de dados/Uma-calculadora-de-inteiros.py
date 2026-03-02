print('Boas vindas a calculadora de inteiros!')

#int() tranforma o tipo da variavel sendo int para inteiro

primeiro_valor = int(input('Digite o primeiro valor: '))
segundo_valor = int(input('Digite o segundo valor: '))

#Para trabalhar com numeros é necessario usar operações matematicas
#Nesse exemplo está sendo usado: (+)adição (-)subtração (/)Divisão (*)multiplicação

soma = primeiro_valor + segundo_valor
subtracao = primeiro_valor - segundo_valor
divisao = primeiro_valor / segundo_valor
multiplicacao = primeiro_valor * segundo_valor

#print(f'') ou print('{}'.format) é uma forma de formatar o print, dando para colocar variáveis de uma amenira mais fácil e pratica durante o código

print('A soma dos valores resulta em {}!'.format(soma))
print(f'A soma dos valores resulta em {soma}!')
print(f'A subtração dos valores resulta em {subtracao}!')
print(f'A divisão dos valores resulta em {divisao}!')
print(f'A multiplicação dos valores resulta em {multiplicacao}!')

