# Aula 18 - Linux-Tips

# DIcionarios

#  quantos metodos há no dict: len(dir(dict)) = 46 metodos

# os DICIONARIOS são conjuntos de chave e valor.

# OBS:os dicionarios guardam dois valores, sendo uma key  que aponta para um value.

# Os DICIONARIOS são Mutaveis!

# exemplo:
#  animals = {'gato': 1, 'cachorro': 2, 'passaro': 3}

# para acessar um valor, usa-se a key
# exemplo:
# animals["passaro"]
# resposta: 3



# EXEMPLO DE JUNÇÂO DE DOIS DICIONARIOS COM DESEMPACOTAMENTO
# OBS: os dois asteriscos são porque há dois elementos que estamos fazendo referencia, ou seja, a key e o value.


# DICIONARIO COM tipos de animais:
# tipos = {'felinos': 1, 'caninos': 1, 'aves': 1}

# DICIONARIO com os animais:
# animals = {'coelho': 4, 'gato': 1, 'cachorro': 2, 'passaro': 3, 'dono': 'Eliote'}

# iterando no dicionario com a intrutura de repetição=> for:
"""

for key in animals:
    print(key)
RESULTADO:
coelho
gato
cachorro
passaro
dono

"""
# ou, agora iterando nas chaves e nos valores
"""
for key, value in animals.items():
    print(key, "->", value)
# RESULTADO:
coelho -> 4
gato -> 1
cachorro -> 2
passaro -> 3
dono -> Eliote

"""

# DESEMPACOTANDO os dicionarios e fazendo a uniao:
# final = {**tipos, **animals}

# Resultado dos dicionarios UNIDOS:
# final = {'felinos': 1,'caninos': 1,'aves': 1,'coelho': 4, 'gato': 1, 'cachorro': 2,'passaro': 3'dono':'Eliote'}


# OBS:quando é somente um elemento usa-se somente um asterisco para fazer o desempacotamento.

# exemplo com conjuntos:

# CRIando um set:
#  davi = {30,"dezembro","azul"}

# CRIANDO outro set
#  sobrenome = {"nascimento"}

# FAZENdo o desempacotamento e unindo os sets:
#  final = {*sobrenome, *davi}

#  final = {30, 'azul', 'dezembro', 'nascimento'}


# os metodos builtin podem ser usados:

# In [100]: len(dir(__builtins__.__dict__["print"]("Hello Wo
#         ⋮ rld")))
# Hello World
# Out[100]: 25

# In [101]:
