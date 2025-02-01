luku_1 = True

luku = int(input("Anna kokonaisluku: ") )
for a in range(2, luku):
    if luku % a == 0:
        luku_1 = False
        break

if (luku_1):
    print("Luku on alkuluku")
else:
    print("Luku ei ole alkuluku")