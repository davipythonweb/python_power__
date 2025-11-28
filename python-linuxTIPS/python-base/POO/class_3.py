class Person: # Nas classes usa-se: pascalCase , UpperCamelCase
    """ Representa uma pessoa"""
    # aqui os atributos de classe imutaveis
    company_name = "Dunder Mifflin" # variaveis usa-se: snake_Case
    work_address = "Rua Stanton. Pensilvania"
    balance = 0 # atributo de classe imutavel

    # Python Data Model - Metodo Dunder ou Metodos Mágicos
    # metodo __init__() eh o inicializador da classe
    # aqui os atributos de classe mutaveis
    def __init__(person, name):
        person.name = name

    # nunca defina um valor mutavel como atributo de classe!
    prefered_colors = []  # atributo de classe mutavel

    # Nas funçoes dentro das classes[metodos] usa-se: snake_Case
    # Injeçao de dependencia -1 arg metodo = a propria instancia
    def add_points(person, value): # funçao dentro de uma classe eh um: Método.
        if person.role == "Manager":
            value *= 2
        person.balance += value

jim = Person(name="Jim Halpert")
jim.role = "Salesman"
jim.add_points(100)
jim.prefered_colors.append("Blue")
jim.work_address = "Home"
print(jim.name, jim.balance, jim.prefered_colors, jim.work_address)

pam = Person(name="Pam Besly")
pam.role = "Receptionist"
pam.add_points(100)
pam.prefered_colors.append("Purple")
print(pam.name, pam.balance, pam.prefered_colors, pam.work_address)
