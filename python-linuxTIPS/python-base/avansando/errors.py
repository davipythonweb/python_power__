#!/usr/bin/env python3

# a instrução abre o arquivo e o lê para
#  imprimir a quinta linha no arquivo
import os
import sys

# PRIMEIRA: LBYL => Look Before You Leap : Olhe antes de atravessar a rua, ou de pular

# LBYL => Look Before You Leap
if os.path.exists("names.txt"):
    names = open("names.txt").readlines()
else:
    print("[ERROR] Missing name in the list!")
    sys.exit(1)


# LBYL => Look Before You Leap

if len(names) >= 3:
    print(names[2])
else:
    print("[ERROR] Missing name in the list!")
    sys.exit(1)