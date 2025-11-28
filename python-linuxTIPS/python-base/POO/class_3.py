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
print(jim.name, jim.balance)

pam = Person()
pam.name = "Pam Besly"
pam.role = "Receptionist"
pam.add_points(100)
print(pam.name, pam.balance)