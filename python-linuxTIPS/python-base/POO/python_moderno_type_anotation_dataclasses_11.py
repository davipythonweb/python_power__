# python moderno - type anotation e dataclasses
# type anotation se estabilizou apartir do python 3.5 e foi melhorada nas versões seguintes.

# ex. carrinho de compras
# sempre para trabalhar com valores monetarios, usar a biblioteca decimal

"""
exemplo de type anotations:

nome: str = "Caneta"
numero: int = 10
quantiade: float = 5.5
active: bool = True

def soma(a: int, b: int) -> int:
    return a + b

class Pessoa:
    nome: str
    idade: int


print(Pessoa.__annotations__) onde ficam as anotaçoes de tipos

onde usar: assinatura de funçao,def classe, metodos.
"""

from decimal import Decimal


produto = "Caneta"
valor = Decimal(4.5)
quantidade = 5

# exemplo errado
cliente_especial = True


# criando um contrato (protocolo) para o tipo valor
def calcula_total(valor: Decimal, quantidade: int) -> Decimal:
    return valor * quantidade # chama o protocolo : __mul__

""" 
def calcula_total(valor, quantidade):
    return valor * quantidade # chama o protocolo : __mul__

if cliente_especial:
    valor = 4.3 #BUG
"""


if cliente_especial:
    valor = Decimal(4.3) #CORRETO


total = calcula_total(valor, quantidade)

print("Tipo:", type(total))
print(f"O total do carrinho é R$ {total:.2f}")


print("-" * 50)
# exemplo de classes sem usar dataclasses
"""
class Pessoa:
    def __init__(self, pk: str, name: str, points: int):
        self.pk = pk        
        self.name = name
        self.points = points
"""

# exemplo com dataclasses
from dataclasses import dataclass

@dataclass
class Pessoa:
    pk: str
    name: str
    points: int


def funcao(dados: Pessoa):
    pass

dados = Pessoa(pk="luiz@gmail", name="Luiz", points=10)

print(dados.name)

funcao(dados)
