#loja ofrerece 2 tipos de pagamento: boleto bancário que dá 5% de desconto ou cartão de credito que permite parcelar em até 12x sem juros.
print('Boas vindas ao Saldão da Alegria!')

total_compra = float(input('Informe o valor total da compra: '))
forma_pagamento = int(input('Selecione o metodo de pagamento: 1 - Boleto 2 - Cartão de credito: '))

#if else  serve como um se não ou seja para definir caminhos dependendo do resultado de algo
if forma_pagamento == 1:
	valor_boleto = total_compra - (total_compra * 0.05)
	print(f'O total a pagar será {valor_boleto}')
else:
	qnt_parcelas =  int(input('Digite a quantidade de parcelas desejadas (até 12 parcelas): '))
	valor_parcelas_cartao = total_compra / qnt_parcelas
	print(f'Sua compra foi dividida em {qnt_parcelas}x com cada parcela custando {valor_parcelas_cartao}')