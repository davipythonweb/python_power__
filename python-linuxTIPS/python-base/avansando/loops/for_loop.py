# loops com for

#!/usr/bin/env python3

original = [1, 2, 3]

# Programação estruturada,Imperativa
# For loops / Laço for
dobrada = []
for n in original:
    dobrada.append(n * 2)
print(dobrada)

# Programaçao Funcional
# List Comprehension
dobrada = [n * 2 for n in original]
print(dobrada)

# Dict comprehension
dados = {
    line.split(":")[0]: line.split(":")[1].strip()
    for line in open("post.txt")
    if ":" in line
}

# o for direto
dados = {}
for line in open("post.txt"):
    if ":" in line:
        key, valor = line.split(":")
        dados[key] = valor.strip()

print(dados)

# imprimindo somente os numeros pares
for num in range(1, 20):
    if num % 2 != 0:
        continue # joga o codigo la pra cima
    print(num)