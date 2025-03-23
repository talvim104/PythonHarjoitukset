import math

def pizza(hinta, halkaisija):
    radius = halkaisija / 200
    pinta_ala = math.pi * radius**2
    return hinta / pinta_ala

pizza_1 = float(input("Pizzan hinta euroina: "))
pizza_2 = float(input("Pizzan halkaisija: "))
pizza_3 = float(input("Toisen pizzan hinta euroina: "))
pizza_4 = float(input("Toisen pizzan halkaisija: "))
hinta1 = pizza(pizza_1, pizza_2)
hinta2 = pizza(pizza_3, pizza_4)

print(f"Ensimmäisen pizzan yksikköhinta: {hinta1:.2f} €/m²")
print(f"Toisen pizzan yksikköhinta:  {hinta2:.2f} €/m²")

if hinta1 < hinta2:
    print("Ensimmäinen pizza on edullisempi!")
elif hinta1 > hinta2:
            print("Toinen pizza on edullisempi!")
