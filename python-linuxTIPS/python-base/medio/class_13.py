# Aula 13

# FORMATAÇAO DE TEXTOS

# Concatenaçao-> concatenando str com float
# nome = "Davi"
# saldo = 30.0
# "O saldo do " + nome + " eh de " + str(saldo)
# resposta: 'O saldo do Davi eh de 30.0'

# Interpolaçao
# nome = "Davi"
# saldo = 30.0
# template = "O saldo do %s eh o total de %.2f"
# resposta: 'O saldo do Davi eh o total de 30.000000'

# str.format
# exemplo:
# msg = "Olá, {} voce eh o player n {} e voce tem {} pontos"
# msg = "Olá, {} voce eh o player n {:03d} e voce tem {:.3f} pontos"
# mgs.format("Davi", 3, 987.3)
# resposta: 'Ola, Davi voce tem 3 pontos'

# exemplos de str.format:
"""
atribuir nome
In [50]: "{}".format("Eliote")
Out[50]: 'Eliote'

centralizar
In [51]: "{:^11}".format("Eliote")
Out[51]: '  Eliote   '

justificar a direita
In [52]: "{:>11}".format("Eliote")
Out[52]: '     Eliote'

justificar a esquerda
In [53]: "{:<11}".format("Eliote")
Out[53]: 'Eliote     '

centralizar e separar com traços
In [56]: "{:-^20}".format("Eliote")
Out[56]: '-------Eliote-------'
"""