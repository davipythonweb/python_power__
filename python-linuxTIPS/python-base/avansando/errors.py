#!/usr/bin/env python3

# a instrução abre o arquivo e o lê para
#  imprimir a quinta linha no arquivo
names = open("names.txt").readlines()
print(names[4])