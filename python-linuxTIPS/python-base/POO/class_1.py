# POO - PROGRAMAÇAO ORIENTADA A OBJETOS com PYTHON

# PARADIGMA IMPERATIVO ou PROCIDURAL


# exemplo para iniciar a aula de POO

# exemplo de programaçao com paradigma imperativo

people = [
    {
        "name":"Eliote Alderson",
        "balance":500,
        "role":"Engenier"
    },
    {
        "name":"Roger",
        "balance":450,
        "role":"Manager"
    }
]

def add_points(person, value):
    if person["role"] == "Manager":
        value *=  2
    person["balance"] += value

for person in people:
    add_points(person, 100)

print(people)