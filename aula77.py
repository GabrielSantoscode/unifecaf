# Manipulando chaves e valores em dicionários
pessoa = {}

##
##

chave = 'nome'

pessoa[chave] = 'Gabriel'
pessoa['sobrenome'] = 'Pereira'


print(pessoa[chave])

pessoa[chave] = 'Lorrany'

del pessoa['sobrenome']
print(pessoa)
print(pessoa['nome'])

# print(pessoa.get('sobrenome'))
if pessoa.get('sobrenome') is None:
    print('NÃO EXISTE')
else:
    print(pessoa['sobrenome'])

# print('ISSO Não vai')