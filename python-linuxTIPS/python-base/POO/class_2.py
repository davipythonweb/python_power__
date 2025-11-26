# PROGRAMAÇAO ORIENTADA A OBJETOS
# POO
# SURGIOU POR VOLTA DE 1970, com um matematico da empresa XEROX, o Allan Key

# CLasses 'class' - MaterialdeEscritorio, Eletronico, Gadget, Frutas
# Objetos - Intancias criadas apartir da classe - caneta, tv, relogio, uva
# Atributos - valores definidos na classes e nos objetos(instancia)
# Métodos - Funçao definida no escopo da classse

class Person: # Nas classes usa-se: pascalCase , UpperCamelCase
    """ Representa uma pessoa"""
    company_name = "Dunder Mifflin" # variaveis usa-se: snake_Case
    work_address = "Rua Stanton. Pensilvania"
    balance = 0

    # Nas funçoes dentro das classes[metodos] usa-se: snake_Case
    def add_points(person, value): # funçao dentro de uma classe eh um: Método.
        if person.role == "Manager":
            value *= 2
        person.balance += value

jim = Person()
jim.name = "Jim Halpert"
jim.role = "Salesman"
jim.add_points(100)

print(id(jim))
print(jim.company_name)
print(jim.name)
print(jim.balance)

print("*" *10)

print(Person.__dict__) # por debaixo dos panos o python armazena as classes como dicionarios.
print(jim.__dict__) # tambem eh outro dicionario, mesmo sendo um atributo de um objeto da classe.