import math
pienin = math.inf
suurin = -math.inf
luku = input("Anna luku: ")
while luku != "":
    luku = float(luku)
    if luku < pienin:
        pienin = luku
    if luku > suurin:
        suurin = luku
    luku = input("Anna seuraava luku: ")

print(f"Suurin antamasi luku: {suurin}")
print(f"Pienin antamasi luku: {pienin}")
