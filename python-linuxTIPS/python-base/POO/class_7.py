# POO

"""Abstraçao: Capacidade de abstrair implementaçoes."""

""" Herança:Capacidade de herdar de outras classes"""

""" Polimorfismo: Capacidade de uma implementação
    se comportar de maneira similar independente
    da dorma do objeto"""

""" Encapsulamento: Capacidade de um objeto esconder a
    sua implementação interna e expor , apenas 
    o que for conveniente."""

# Exemplo de encapsulamento
class Conta:
    _tipo_de_conta = 'Corrente' # Atributo (protegido) 

    def __init__(self, cliente):
        self.cliente = cliente

conta = Conta(cliente='Eliote')

print(dir(conta)) # Mostra todos os atributos e métodos do objeto
print(len(dir(conta))) # Mostra a quantidade de atributos e métodos do objeto

# mostrar quantidade de atributos e métodos públicos
publicos = [i for i in dir(conta) if not i.startswith('_')]
print(len(publicos))

# mostrar quantidade de atributos e métodos privados
privados = [i for i in dir(conta) if i.startswith('_')]
print(len(privados))


print(conta.cliente)
conta.cliente = 'Outro'
print(conta.cliente)
