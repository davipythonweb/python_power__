# python moderno - type anotation e dataclasses

# ex. carrinho de compras

produto = "Playstation 5"
preco = 4500.00
quantidade = 5

def calcula_total(valor, qtd):
    return valor * qtd

total = calcula_total(preco, quantidade)
print(f"O total do carrinho é R$ {total:.2f}")