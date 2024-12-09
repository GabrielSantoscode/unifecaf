# Problema dos parâmetros mutáveis em funções Python
def adiciona_clientes(nome, lista=None):
    if lista is None:
        lista = []
    lista.append(nome)
    return lista

lista1 = []
cliente_1 = adiciona_clientes('Gabriel', lista1)
adiciona_clientes('Lorrany', cliente_1)
print(cliente_1)

cliente_2 = adiciona_clientes('Peter')
adiciona_clientes('Parker', cliente_2)
print(cliente_2)