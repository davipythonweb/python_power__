# POO

# Protocolos / Data Model


# protocolos são um conjunto de regras e convenções que definem como os objetos interagem entre si em Python.

# Eles são implementados através de métodos especiais (métodos mágicos) que começam e terminam com dois underlines (__).

# Esses métodos permitem que os objetos se comportem de maneira específica em determinadas situações, como operações
# aritméticas, comparações, iteração, entre outras.

# Ao implementar esses métodos em suas classes, você pode definir como os objetos dessas classes devem se comportar
# em diferentes contextos, tornando-os mais integrados e compatíveis com o restante do ecossistema Python.

# Exemplos comuns de métodos especiais incluem:
# __init__: Inicializa um objeto.
# __str__: Define a representação em string de um objeto.
# __add__: Define o comportamento do operador de adição (+) para objetos.
# __len__: Retorna o comprimento de um objeto.
# __repr__: Fornece uma representação oficial de um objeto.

# Um dos protocolos mais faceis de entender -> Printable -> imprimir objetos

print("protocolo Printable" + "\n")

class Cor: # Base Class
    english_name = "color"
    icon = "⬜​​"

    # reescrevendo o método __str__
    def __str__(self):
        return f"{self.english_name} - {self.icon}"

class Amarelo(Cor):
    icon = "🟨​"
    english_name = "yellow"

class Azul(Cor):
    icon = "🟦​"
    english_name = "blue"

class Vermelho(Cor):
    icon = "🟥​"
    english_name = "red"



print("Cores Primarias")
print(Amarelo())
print(Azul())
print(Vermelho())

print("-" * 20)

# Outro Protocolo
# Addible -> somar objetos

print("protocolo Addible" + "\n")

print( 1 + 1 )
print("Eliote " + "Alderson")
print([1, 2] + [3, 4])

