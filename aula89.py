string = 'Gabriel'
metodo = 'upper'

if hasattr(string, metodo):
    print('existe upper')
    print(getattr(string, metodo)())
    print(string)
else:
    print('Não existe o metodo', metodo)