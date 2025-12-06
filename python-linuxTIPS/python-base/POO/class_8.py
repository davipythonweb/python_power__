# exemplo encapsulamento2

class Conta:
    _tipo_de_conta = 'Corrente'  # Atributo (protegido)

    def __init__(self, cliente):
        self.cliente = cliente
        self._saldo = 0  # Atributo (protegido)

    def conssultar(self):
        if self._saldo <= 0:
            print('Saldo insuficiente')
        return self._saldo
    

conta = Conta(cliente='Eliote')

print(conta.conssultar())