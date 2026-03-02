# \n serve para fazer uma quebra de linha. \t serve para fazer uma tabulação
#essas são função que estruturam o texto, possuem outras com a mesmo modelo \(letra que representa a função)
texto = "Este texto possui querbra de linha\n.\tE aqui uma tabulação"
print(texto)

#existe alguns comandos que mexem/analisam um texto
#sua estrutura é feita com (TEXTO.FUNÇÃO)
texto = 'Texto em minúsculas AINDA É texto'
print(texto.capitalize())

print(texto.upper())
print(texto.lower())
print(texto.startswith('Tex'))
print(texto.endswith('to'))
print(texto.count('@'))
print('em' in texto)
print(texto.replace('AINDA', 'com certeza'))
#.replace não altera a váriavel

