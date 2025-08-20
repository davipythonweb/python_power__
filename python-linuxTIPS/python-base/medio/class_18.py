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

# DICIONARIO COM tipos de animais:
# tipos = {'felinos': 1, 'caninos': 1, 'aves': 1}

# DICIONARIO com os animais:
# animals = {'coelho': 4, 'gato': 1, 'cachorro': 2, 'passaro': 3, 'dono': 'Eliote'}

# DESEMPACOTANDO os dicionarios e fazendo a uniao:
# final = {**tipos, **animals}

# Resultado dos dicionarios UNIDOS:
# final = {'felinos': 1,'caninos': 1,'aves': 1,'coelho': 4, 'gato': 1, 'cachorro': 2,'passaro': 3'dono':'Eliote'}