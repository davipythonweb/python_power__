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
    
    def __add__(self, other):
        mixtable = [
            ((Amarelo, Vermelho), Laranja),
            ((Azul, Amarelo), Verde),
            ((Vermelho, Azul), Violeta),
        ]
        for mix, result in mixtable:
            if isinstance(self, mix) and isinstance(other, mix):
                return result()

class Amarelo(Cor):
    icon = "🟨​"
    english_name = "yellow"

class Azul(Cor):
    icon = "🟦​"
    english_name = "blue"

class Vermelho(Cor):
    icon = "🟥​"
    english_name = "red"

class Laranja(Cor):
    icon = "🟧​"
    english_name = "orange"

class Verde(Cor):
    icon = "🟩​"
    english_name = "green"

class Violeta(Cor):
    icon = "🟪​"
    english_name = "violet"





print("Cores Primarias")
print(Amarelo())
print(Azul())
print(Vermelho())

print("-" * 20)

# Outro Protocolo
# Addible -> somar objetos
# ele tem dois metodos especiais: [atua in left] __add__ e [atua in right]__radd__

print("protocolo Addible" + "\n")

print( 1 + 1 )
print(5 .__add__(3)) # mesmo que 5 + 3
print("Eliote " + "Alderson")
print([1, 2] + [3, 4])

print("-" * 20)

print("Cores Primarias")
amarelo = Amarelo()
azul = Azul()
vermelho = Vermelho()
print(amarelo, azul, vermelho)

print("-" * 20)

print("Cores Secundarias")
print("Amarelo + Vermelho", amarelo + vermelho)  # Laranja
print("Azul + Amarelo", azul + amarelo)      # Verde
print("Vermelho + Azul", vermelho + azul)     # Violeta     

print("-" * 20) 
# Protocolo __contains__
# Ele é usado para definir o comportamento do operador de associação 'in' em objetos personalizados.
# sempre retorna True ou False

class Paleta:
    def __init__(self, *cores):
        self._cores = cores

    def __iter__(self):
        return iter([cor for cor in  self._cores])
    
    def __contains__(self, item):
        return item in [cor.icon for cor in self._cores]
    
print("-" * 20)

rgb = Paleta(Vermelho(), Verde(), Azul())
print("🟦​" in rgb)
print("🟥​" in rgb)
print("🟩​" in rgb)
