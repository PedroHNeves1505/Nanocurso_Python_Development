texto_para_gravar = 'Esse texto será gravado'

# Essa estrutura serve para abir e salvar informações em arquivos
#with  serve para trabalhar com arquivos que precisam ser abertos
#open() serve para abrir e manipular um arquivo
#mode  serve para definir o modo em que irá abrir o arquivo (W == write)
#enconding  Serve para tratar a codificação dos itens colocados no arquivo
#as  serve para definir a variavel responsável pelo arquivo

with open('arquivo.txt', mode='w', encoding='UTF-8') as arquivo:
	arquivo.write(texto_para_gravar)
	
#.write() serve para escrever uma informação no arquivo

print('Texto salvo...')