#!/usr/bin/env python3

# a instrução abre o arquivo e o lê para
#  imprimir a quinta linha no arquivo

import sys

names = open("names.txt").readlines()

# Existem duas abordagens para resolver erros:
# PRIMEIRA: LBYL => Look Before You Leap : Olhe antes de atravessar a rua, ou de pular

if len(names) >= 3:
    print(names[2])
else:
    print("[ERROR] Missing name in the list!")
    sys.exit(1)