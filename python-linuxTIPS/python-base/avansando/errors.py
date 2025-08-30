#!/usr/bin/env python3

# a instrução abre o arquivo e o lê para
#  imprimir algo

import os
import sys

# Existem duas abordagens para resolver erros:
# PRIMEIRA: LBYL => Look Before You Leap : Olhe antes de atravessar a rua, ou de pular
# OBS: Estas OPERAÇOES de IO(input/output)
# podem demorar. Exemplo, usar(if,else) para verificar errors.
# ESTA OPÇAO causa o (Race Condition) , corrida de leitura entre arquivos, por exemplo doi programas que acessao o mesmo arquivo.


# LBYL => Look Before You Leap
# VERIFICANDO SE EXISTE O ARQUIVO.
"""
if os.path.exists("names.txt"):
    input("...") # Race Condition
    names = open("names.txt").readlines()
else:
    print("[ERROR 1] File names.txt not found!")
    sys.exit(1)
"""

# LBYL => Look Before You Leap
# VERIFICANDO O NUMERO DE LINHAS
"""
if len(names) >= 3:
    print(names[2])
else:
    print("[ERROR 2] Missing name in the list!")
    sys.exit(1)

"""

# ===>ESTA ABORDAGEM para errors EH A MELHOR!<=====
# SEGUNDA: EAFP => Easy to Ask Forgiveness than permission : É mais fácil pedir perdão do que permissão. usa-se o try, except.
# OBS: tratamento de erro tem que ser sempre ESPECIFICO!!!


# EAFP => Easy to Ask Forgiveness than permission
# VERIFICANDO SE EXISTE O ARQUIVO.
"""
try:
    names = open("names.txt").readlines() # FileNotFoundError
    1 / 0 # ZeroDivisionError
    print(names.banana) # AtributeError
except: # Bare except(pega qualquer erro que acontecer)
    print("[ERROR 1] File names.txt not found!")
    sys.exit(1)
"""

try:
    names = open("names.txt").readlines() # FileNotFoundError
    1 / 1 # ZeroDivisionError
    print(names.append) # AttributeError
except FileNotFoundError:
    print("[ERROR 1] File names.txt not found!")
    sys.exit(1)
except ZeroDivisionError:
    print("[ERROR 2] You cant divide by zero!")
    sys.exit(1)
except AttributeError:
    print("[ERROR 3] List doesn't have banana!")
    sys.exit(1)


# PEGANDO A MENSSAGEM ESPECIFICA DO ERRO E IMPRIMINDO:
"""
try:
    names = open("names.txt").readlines() # FileNotFoundError
except FileNotFoundError as e:
    print(f" {str(e)}.")
    sys.exit(1)
""" #TODO: Usar o retry

# EAFP => Easy to Ask Forgiveness than permission
# VERIFICANDO O NUMERO DE LINHAS
try:
    print(names[2])
except:
    print("[ERROR 4] Missing name in the list!")
    sys.exit(1)