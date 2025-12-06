# exemplo2 encapsulamento

class Conta:
    _tipo_de_conta = 'Corrente'  # Atributo (protegido)

    def __init__(self, cliente):
        self.cliente = cliente
        self._saldo = 0  # Atributo (protegido)
    
    # encapsulando o atributo _saldo dentro dos métodos da classe
    def depositar(self, valor):
        self._saldo += valor

    def sacar(self, valor):
        if valor > self._saldo:
            print('Saldo insuficiente')
        else:
            self._saldo -= valor

    def consultar(self):
        if self._saldo <= 0:
            print('Saldo insuficiente')
        return self._saldo
    

conta = Conta(cliente='Eliote')
conta.depositar(500)
print(conta.consultar())

conta.sacar(100)
print(conta.consultar())