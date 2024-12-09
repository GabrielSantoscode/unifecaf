# class - Classes são moldes para criar novos objetos
# As classes geram novos objetos (instâncias) que
# podem ter seus próprios atributos e métodos.
# Os objetos gerados pela classe podem usar seus dados
# internos para realizar várias ações.
# Por convenção, usamos PascalCase para nomes de
# classes.
# string = 'Luiz'  # str
# print(string.upper())
# print(isinstance(string, str))
class Pessoa:
    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome

p1 = Pessoa('Gabriel', 'Pereira')
# p1.nome = 'Gabriel'
# p1.sobrenome = 'Pereira'

p2 = Pessoa('Lorrany', 'Silva')
# # p2.nome = 'Lorrany'
# p2.sobrenome = 'Silva'

print(p1.nome)
print(p1.sobrenome)

print(p2.nome)
print(p2.sobrenome)