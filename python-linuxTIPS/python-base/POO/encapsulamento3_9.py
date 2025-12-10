# POO

# encapsulamento - parte 3 usandpo propriedades
# propriedades protegem atributos
# 1 underline menos protegido (privado)
# 2  underlines mais protegido (privado)

# Os 4 Pilares da orientação a objetos
# 1 Abstração
# 2 Herança
# 3 Polimorfismo
# 4 Encapsulamento => proteção de atributos e métodos de uma classe (publico[pode acessar fora da classe], protegido, privado[com anderline])

# # propriedades getter, setter e deleter,
from abc import ABC # Abstract Base Class

class Conta(ABC):
    def __init__(self, cliente):
        self.cliente = cliente
        self._saldo = 0  # Atributo (privado)


class ContaCorrente(Conta):
    _id_interno = 123456  # Atributo (privado)

    @property # propriedade getter para o atributo privado _saldo
    def saldo(self):
        if self._saldo <= 0:
            print('Saldo insuficiente ou zero!')
        return self._saldo
    
    @saldo.setter  # propriedade setter para o atributo privado _saldo
    def saldo(self, valor):
        self._saldo += valor

    @saldo.deleter  # propriedade deleter para o atributo privado _saldo
    def saldo(self):
        self._saldo = 0
    

conta = ContaCorrente(cliente='Noah')
print(conta.cliente)  # Acesso permitido
print(conta.saldo) # Acesso permitido via propriedade

# deposito
conta.saldo = 500  # Usando o setter para modificar o saldo
print('depositado =',conta.saldo)

conta.saldo = 200
print('deposito de 200 =',conta.saldo)

# saque
conta.saldo = -50
print('saque de 50 =',conta.saldo)

# zerando saldo
del conta.saldo
print('conta zerada! =',conta.saldo)

# verificando atributos e métodos da classe
# print(dir(conta))