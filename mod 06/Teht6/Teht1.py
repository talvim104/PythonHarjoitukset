import random

def kuutio():
    return random.randint(1, 6)

luku = 0

while luku != 6:
    luku = kuutio()
    print(luku)