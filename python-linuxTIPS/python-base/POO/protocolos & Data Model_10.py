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

# Um dos protocolos mais faceis de entender -> Printable

class Cor: # Base Class
    #  icon de quadrado branco
    icon = "⬜​​"
    def __str__(self):
        return self.icon

class Amarelo(Cor):
    # icon com quadrado amarelo
    icon = "🟨​"

class Azul(Cor):
    # icon com quadrado de cor azul
    icon = "🟦​"

#  emotion de quadrado amarelo
#  emotion = "\U0001F7E1"

class Vermelho(Cor):
    # icon com quadrado vermelho
    icon = "🟥​"

print("Cores Primarias")
print(Amarelo())
print(Azul())
print(Vermelho())
