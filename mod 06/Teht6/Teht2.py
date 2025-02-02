import random

def kuutio(kuutio_2):
    return random.randint(1, kuutio_2)

kuutio_2 = int(input("Anna tahkojen määrä: "))

luku = 0

while luku != kuutio_2:
    luku = kuutio(kuutio_2)
    print(luku)