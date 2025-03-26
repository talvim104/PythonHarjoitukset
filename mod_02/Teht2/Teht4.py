print("Moi! Keksi kolme kokonaislukua. ")
#Jos käyttäjä laittaa desimaaliluvun, ohjelma poistaa desimaalit
luku_1 = int(float(input("Anna luku 1: ")))
luku_2 = int(float(input("Anna luku 2: ")))
luku_3 = int(float(input("Anna luku 3: ")))
summa = luku_1 + luku_2 + luku_3
tulo = luku_1 * luku_2 * luku_3
keskiarvo = round(float(luku_1 + luku_2 + luku_3) / 3)
print("Summa: ", summa)
print("Tulo: ", tulo)
print("Keskiarvo: ", keskiarvo)
