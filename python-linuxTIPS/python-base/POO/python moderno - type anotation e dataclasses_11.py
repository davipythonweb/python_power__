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



def calcula_total(valor, quantidade):
    return valor * quantidade # chama o protocolo : __mul__

if cliente_especial:
    valor = 4.3 #BUG

total = calcula_total(valor, quantidade)

print("Tipo:", type(total))
print(f"O total do carrinho é R$ {total:.2f}")