# python moderno - type anotation e dataclasses

# ex. carrinho de compras
# sempre para trabalhar com valores monetarios, usar a biblioteca decimal
from decimal import Decimal


produto = "caneta BIC"
preco = Decimal("2.50")
quantidade = 5

def calcula_total(valor, qtd):
    return valor * qtd

total = calcula_total(preco, quantidade)
print(f"O total do carrinho é R$ {total:.2f}")