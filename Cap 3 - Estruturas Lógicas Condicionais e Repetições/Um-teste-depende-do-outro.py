#Uma companhia aárea possui 3 tipos de clientes: premium, gold e silver. Os clientes do tipo premium podem levar malas de até 32kg sem custo adicional, os clientes gold podem levar malas de até 28kg sem custos adicioanis e os clientes silver devem pagar por qualquer bagagem adicional.
print('Bem vindo a companhia voos Fiap')

tipo_de_cliente = input('Informe seu tipo de cliente: PREMIUM, GOLD OU SILVER: ')
peso_bagagem = float(input('Informe o peso de sua bagagem adicional em Kg: '))

verificar_bagagem_premium = peso_bagagem <= 32
verificar_bagagem_gold = peso_bagagem <= 28

#elif quando um if else precisar de 3 ou mais comparações é preciso usar o elif para criar um caminho entre if e else

if tipo_de_cliente.upper() == 'PREMIUM':
	if verificar_bagagem_premium == True:
		print('Sua bagagem extra não precisará de custos adicionais.')
	else:
		print('Sua bagagem extra ultrapassa o peso limite, será necessario o pagamento de uma taxa para o despachamento.')
elif tipo_de_cliente.upper() == 'GOLD':
	if verificar_bagagem_gold == True:
		print('Sua bagagem extra não precisará de custos adicionais.')
	else:
		print('Sua bagagem extra ultrapassa o peso limite, será necessario o pagamento de uma taxa para o despachamento.')
else:
	print('Precisará ser pago uma taxa para o despachamento de sua bagagem extra.')
