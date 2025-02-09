airports = {}

while True:
    print("Valitse toiminto:")
    print("1 - Lisää uusi lentoasema")
    print("2 - Hae lentoaseman tiedot")
    print("3 - Lopeta")

    valinta = input("Syötä 1, 2 tai 3: ")

    if valinta == "1":
        icao = input("Syötä lentoaseman ICAO-koodi: ")
        nimi = input("Syötä lentoaseman nimi: ")
        airports[icao] = nimi
        print(f"Lentoasema {nimi} tallennettu koodilla {icao}.")

    elif valinta == "2":
        icao = input("Syötä ICAO-koodi: ")
        if icao in airports:
            print(f"Lentoasema: {airports[icao]}")
        else:
            print("Lentoasemaa ei löytynyt.")

    elif valinta == "3":
        print("Ohjelma lopetettu.")
        break
