# exemplo de um codigo com POO de uma frutaria

class Fruit:
    """Representa a fruit"""
    def __init__(self, name, color): # metodo inicializador da classe, contem atributos mutaveis.
        self.name = name
        self.color = color

apple = Fruit("Apple", "Red")
print(apple.name, apple.color)

banana = Fruit("Banana", "Yellow")
print(banana.name, banana.color)