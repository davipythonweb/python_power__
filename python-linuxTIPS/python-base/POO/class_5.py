# POO

# 1º PILAR
# Abstração: capacidade de trazer as implementaçoes para o mundo real, capacidade de representar , abstrair as informaçoes em modelos que se parecem com objetos reais.
# exemplo:
class Person:
    kingdom = "animalia"

class Fruit:
    kingdom = "vegetalia"

class Animal:
    kingdom = "animalia"


# 2º PILAR
# Herança: Capacidade de criaçao de classe base e apartir dela herdar atributos e criar outros objetos.
# Herança + Abstraçao
from abc import ABC

# super classe
class Fruta(ABC):
    reino = "vegetalia" # Classe abstrata/ base
    
    def __init__(self, cores):
        self.cores = cores

# Python permite herança multipla.

class Comida(ABC):
    preço = 4.5

# derivadas (sub classe)
class Maça(Fruta, Comida):   # herança em uma classe material
    image = "🍎"

minha_maça = Maça(cores=['verde', 'branco'])
print(minha_maça.cores, minha_maça.preço)
print(minha_maça.reino)
print(minha_maça.image)

class Melancia(Fruta):
    image = "🍉"

minha_melancia = Melancia(cores=['verde', 'vermelho', 'preto'])
print(minha_melancia.cores)
print(minha_melancia.image)