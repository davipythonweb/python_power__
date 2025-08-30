#!/usr/bin/env python3

# a instrução abre o arquivo e o lê para
#  imprimir algo

import os
import sys

# Existem duas abordagens para resolver erros:
# PRIMEIRA: LBYL => Look Before You Leap : Olhe antes de atravessar a rua, ou de pular

# LBYL => Look Before You Leap
# VERIFICANDO SE EXISTE O ARQUIVO.
if os.path.exists("names.txt"):
    names = open("names.txt").readlines()
else:
    print("[ERROR 1] File names.txt not found!")
    sys.exit(1)

    
# LBYL => Look Before You Leap
# VERIFICANDO O NUMERO DE LINHAS
if len(names) >= 3:
    print(names[2])
else:
    print("[ERROR 2] Missing name in the list!")
    sys.exit(1)