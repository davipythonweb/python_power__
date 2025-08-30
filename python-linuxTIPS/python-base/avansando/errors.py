#!/usr/bin/env python3

# a instrução abre o arquivo e o lê para
#  imprimir a quinta linha no arquivo

import sys

names = open("names.txt").readlines()

# Existem duas abordagens para resolver erros:
# PRIMEIRA: LBYL => Look Before You Leap : Olhe antes de atravessar a rua, ou de pular

if len(names) >= 3:
    print(names[4])
else:
    print("O nome nao esta na lista!")
    sys.exit(1)