# POO - PROGRAMAÇAO ORIENTADA A OBJETOS com PYTHON

# PARADIGMA[forma como a gente se expressa e declara as coisas no nosso programa] IMPERATIVO ou PROCIDURAL
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

# def add_points(person, value):
#     if person["role"] == "Manager":
#         value *=  2
#     person["balance"] += value

# for person in people:
#     add_points(person, 100)
    

# print(people)


# misturando paradigma imperativo com funcional
# a programaçao funcional, são puras= no side effects
def add_points(person, value):
    data = person.copy() # aqui seria o (no side effects, porque uma copia do objeto['person'] sera mudado), a "data".
    if data["role"] == "Manager":
        value *=  2
    data["balance"] += value
    return data
  
    
result = map(lambda person: add_points(person, 100), people)
# funcional
# declarativa
# lazy valuation = ou seja,  sao avaliadas somente quanto eh consumido o objeto.

# consindo o map , passando para um iterator(objeto capaz de consumir um iterador) , no caso o list.
print(list(result))
print(people)