vuosi = int(input("Anna vuosiluku: "))
if vuosi % 4 == 0:
    print("Vuosi on karkausvuosi!")
elif vuosi % 400 == 0 and vuosi % 100 == 0:
    print("Vuosi on karkausvuosi!")
else:
    print("Vuosi ei ole karkausvuosi!")
