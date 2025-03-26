class Julkaisu:
    def __init__(self, nimi):
        self.nimi = nimi

class Kirja(Julkaisu):
    def __init__(self,nimi, kirjoittaja, sivumaara):
        self.kirjoittaja = kirjoittaja
        self.sivumaara = sivumaara
        Julkaisu.__init__(self,nimi)

    def tulostaa_tiedot(self):
        print(f"Kirjan nimi on {my_book.nimi}, kirjoittaja on {my_book.kirjoittaja}, sivumäärä on {my_book.sivumaara} sivua.")

class Lehti(Julkaisu):
    def __init__(self, nimi, paatoimittaja):
        self. paatoimittaja =  paatoimittaja
        Julkaisu.__init__(self, nimi)

    def tulostaa_tiedot(self):
        print(f"Lehden nimi on {my_magazine.nimi} ja päätoimittaja on {my_magazine.paatoimittaja}.")

my_book = Kirja("Hytti No6", "Rosa Liksom", 200)
my_magazine = Lehti("Aku Ankka", "Aki Hyyppä")

my_book.tulostaa_tiedot()
my_magazine.tulostaa_tiedot()






