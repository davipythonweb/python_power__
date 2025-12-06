# POO

"""Abstraçao: Capacidade de abstrair implementaçoes."""

""" Herança:Capacidade de herdar de outras classes"""

""" Polimorfismo: Capacidade de uma implementação
    se comportar de maneira similar independente
    da dorma do objeto"""

""" Encapsulamento: Capacidade de um objeto esconder a
    sua implementação interna e expor , apenas 
    o que for conveniente."""

class Conta:
    def __init__(self, cliente):
        self.cliente = cliente

conta = Conta(cliente='Eliote')

print(dir(conta))

print(conta.cliente)
conta.cliente = 'Outro'
print(conta.cliente)