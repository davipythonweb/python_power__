# python moderno - type anotation e dataclasses
# type anotation se estabilizou apartir do python 3.6

# ex. carrinho de compras
# sempre para trabalhar com valores monetarios, usar a biblioteca decimal
from decimal import Decimal


produto = "Caneta"
valor = Decimal(4.5)
quantidade = 5

# exemplo errado
cliente_especial = True



def calcula_total(valor, qtd):
    return valor * quantidade # chama o protocolo : __mul__

if cliente_especial:
    valor = 4.3 #BUG

total = calcula_total(valor, quantidade)

print("Tipo:", type(total))
print(f"O total do carrinho é R$ {total:.2f}")