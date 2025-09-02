# Loops com While

#!/usr/bin/env python3

# While - Enquanto


# o while nao opera em cima de uma coleçao mas em uma condiçao!


n = 0
while n < 101:  # condiçao de parada
    if n % 2 != 0:
        n += 1
        continue
    print(n)
    n += 1