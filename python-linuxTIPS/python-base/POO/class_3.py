class Person: # Nas classes usa-se: pascalCase , UpperCamelCase
    """ Representa uma pessoa"""
    # aqui os atributos de classe imutaveis
    company_name = "Dunder Mifflin" # variaveis usa-se: snake_Case
    work_address = "Rua Stanton. Pensilvania"
    balance = 0 # atributo de classe imutavel

    # pela convençao o metodo dentro de uma classe eh chamado de > self
    # Python Data Model - Metodo Dunder ou Metodos Mágicos
    # metodo __init__() eh o inicializador da classe
    # aqui os atributos de classe mutaveis
    def __init__(self, name, role='Undefined', prefered_colors=None):
        self.name = name
        self.role = role
        self.prefered_colors = prefered_colors or []

    # nunca defina um valor mutavel como atributo de classe!
    prefered_colors = []  # atributo de classe mutavel

    # Nas funçoes dentro das classes[metodos] usa-se: snake_Case
    # Injeçao de dependencia -1 arg metodo = a propria instancia
    def add_points(self, value): # funçao dentro de uma classe eh um: Método.
        if self.role == "Manager":
            value *= 2
        self.balance += value

jim = Person("Jim Halpert", role="Salesman", prefered_colors=["Blue"])
jim.add_points(500)
jim.work_address = "Home"
print(jim.name, jim.balance, jim.prefered_colors, jim.work_address, jim.role)

pam = Person("Pam Besly", role="Receptionist")
pam.add_points(100)
print(pam.name, pam.balance, pam.prefered_colors, pam.work_address, pam.role)
