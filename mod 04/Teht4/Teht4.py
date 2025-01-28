import random

luku = random.randint(1, 10)
luku_2 = int(input("Arvaa luku väliltä 1..10: "))
while luku != luku_2:
    if luku_2 < luku:
        print("Liian pieni arvaus")
    else:
        print ("Liian suuri arvaus")
    luku_2 = int(input("Arvaa luku väliltä 1..10:"))

print("Oikein!")
