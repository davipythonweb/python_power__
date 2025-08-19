# AULA 17 - LInuxTipss
# tipo de dado chamado Sets , ou CONJUNTOS.

# OBS:Cria uma coleção desordenada de ELEMENTOS UNICOS

#  quantos metodos há no set: len(dir(set)) = 57 metodos


# criando um set:
# c1 = set( (1, 2, 3) )
# ou 
# c1 = set( [, 2, 3])


# c2 = set("banana")
# c2= {'a', 'b', 'n'}

# no exemplo acima: FOI RETIRADO DO CONJUNTO TODOS OS REPETIDOS. 

# exemplo de união de set:

# CRIANDO DUAS LISTAS:
# conjunto_a = [1, 2, 3, 4, 5]
# conjunto_b = [4, 5, 6, 7, 8]

# CONVERTENDO AS LISTAS PARA CONJUNTO E FAZENDO A UNIÂO.
# set(conjunto_a) | set(conjunto_b)
# {1, 2, 3, 4, 5, 6, 7, 8}

# ou usando o metodo union:
# set(conjunto_a).union(set(conjunto_b))
# {1, 2, 3, 4, 5, 6, 7, 8}

# COMPARAR UM PARA MUITOS ELEMENTOS
# O(n)

# COMPARAR UM PARA TODOS OS ELEMENTOS DE UM set
# O(1) => operação constante
# OBS: o python utiliza o Hash Table para 
# comparar ou buscar em conjuntos(deixando a busca mais rapida.)