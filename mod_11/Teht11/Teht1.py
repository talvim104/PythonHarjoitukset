class Julkaisu:
    def __init__(self, nimi):
        self.nimi = nimi

class Kirja(Julkaisu):
    def __init__(self,nimi, kirjoittaja, sivumaara):
        self.kirjoittaja = kirjoittaja
        self.sivumaara = sivumaara
        Julkaisu.__init__(self,nimi)

    def tulosta_tiedot(self):
        print(f"Kirjan nimi on {self.nimi}, kirjoittaja on {self.kirjoittaja}, sivumäärä on {self.sivumaara} sivua.")

class Lehti(Julkaisu):
    def __init__(self, nimi, paatoimittaja):
        self. paatoimittaja =  paatoimittaja
        Julkaisu.__init__(self, nimi)

    def tulosta_tiedot(self):
        print(f"Lehden nimi on {self.nimi} ja päätoimittaja on {self.paatoimittaja}.")

my_book = Kirja("Hytti No6", "Rosa Liksom", 200)
my_magazine = Lehti("Aku Ankka", "Aki Hyyppä")

my_book.tulosta_tiedot()
my_magazine.tulosta_tiedot()






