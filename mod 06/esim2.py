# Funktio, joka saa alkuarvon eli parametrin.
#funktio ei palauta mitään.
def tuplaus(luku):
    print(f"Sain alkuarvoksi luvun {luku}")
    tulos = 2 * luku
    print(f"Alkuarvo eri parametrin arvo "
          f"tuplana {tulos} ")

print("Pääohjelma alkaa")
tuplaus(3)

print("Ollaan takaisin pääohjelmassa")