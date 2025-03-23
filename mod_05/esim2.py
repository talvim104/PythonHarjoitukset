nimet = []

nimi = input("Anna ensimmäinen nimi tai lopeta painamalla Enter: ")
while nimi!="":
    nimet.append(nimi)
    nimi = input("Anna seuraava nimi tai lopeta painamalla Enter: ")

print(nimet)