class Auto:
    def __init__ (self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nopeus = 0
        self.kuljettu_matka = 0

    def kiihdyta (self, nopeuden_muutos):
        self.nopeus += nopeuden_muutos
        if self.nopeus > self.huippunopeus:
            self.nopeus = self.huippunopeus
        elif self.nopeus < 0:
            self.nopeus = 0


my_auto = Auto("ABC-123", 142)

my_auto.kiihdyta(30)
my_auto.kiihdyta(70)
my_auto.kiihdyta(50)

print(f"Tämänhetkinen nopeus: {my_auto.nopeus} km/h.")

my_auto.kiihdyta(-200)

print(f"Hätäjarrutuksen jälkeen nopeus: {my_auto.nopeus} km/h.")