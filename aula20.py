v1= input('Digite um valor: ')
v2= input('Digite outro valor: ')

if v1 > v2:
    print('O primeiro valor é maior')
else:
    print('O segundo valor é maior')


primeiro_valor = input('Digite um valor: ')
segundo_valor = input('Digite outro valor: ')

if primeiro_valor >= segundo_valor:
    print(
        f'{primeiro_valor=} é maior ou igual '
        f'ao que {segundo_valor=}'
    )
else:
    print(
        f'{segundo_valor=} é maior '
        f'do que {primeiro_valor=}'
    )