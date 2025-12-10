# POO

# 3º Pilar do POO

# Polimorfismo : independente da forma do objeto, a gente consegue aplicar operações nele, desde que, esteja de acordo com determinada interface ou protocolo.

# Em python , os protocolos nao sao nominais, e sim estruturais.

"""
nome = "Bruno"
print("B" in nome) # Container - __contains__

cores = ["red", "green", "orange"]
print("green" in cores)

"""


# exemplo com polimorfismo
class Dog:
    def make_sound(self):
        return "woof woof"

class Cat:
    def make_sound(self):
        return "meow meow"    

def print_sound(obj):
    if not hasattr(obj, "make_sound"):
        raise TypeError(f"{obj} nao faz som")
    print(obj.make_sound())

rex = Dog()
print_sound(rex)

frajola = Cat()
print_sound(frajola)

# print_sound(42)



# o polimorfismo esta baseado em uma caracteristica chamada => 

# Duck Typing
"""
se o objeto anda como um pato,
parece um pato, faz quack como um pato,
entao eh um pato!
"""

# Outro exemplo de polimorfismo
def funcao(*args):
    ret = 0
    for arg in args:
        ret += arg
    return ret

print(funcao(1, 2, 3))
print(funcao(1, 2, 3, 4))
print(funcao(1, 2, 3, 4, 5))
print(funcao())

# a funçao funciona para todos os exemplos