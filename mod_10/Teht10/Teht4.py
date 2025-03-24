import random

class Auto:
    def __init__ (self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nopeus = 0
        self.kuljettu_matka = 0

    def kiihdyta(self, nopeuden_muutos):
        self.nopeus += nopeuden_muutos
        if self.nopeus > self.huippunopeus:
            self.nopeus = self.huippunopeus
        elif self.nopeus < 0:
            self.nopeus = 0

    def kulje(self, tunnit):
        self.kuljettu_matka += tunnit * self.nopeus


class Kilpailu:
    def __init__(self, nimi, pituus, autot):
        self.nimi = nimi
        self.pituus = pituus
        self.autot = autot

    def tunti_kuluu(self):
        for auto in self.autot:
            nopeuden_muutos = random.randint(-10, 15)
            auto.kiihdyta(nopeuden_muutos)
            auto.kulje(1)

    def tulosta_tilanne(self):
        print("Tilanne:")
        for auto in self.autot:
            print(f"{auto.rekisteritunnus}: nopeus {auto.nopeus} km/h, matka {int(auto.kuljettu_matka)} km")
        print()

    def kilpailu_ohi(self):
        for auto in self.autot:
            if auto.kuljettu_matka >= self.pituus:
                return True
        return False

autot = []
for i in range(1, 11):
    rek = f"ABC-{i}"
    huippu = random.randint(100, 200)
    autot.append(Auto(rek, huippu))

kisa = Kilpailu("Suuri romuralli", 8000, autot)

tunti = 0
while not kisa.kilpailu_ohi():
    kisa.tunti_kuluu()
    tunti += 1
    if tunti % 10 == 0:
        print(f"Tunti: {tunti}")
        kisa.tulosta_tilanne()

print(f"Kilpailu päättyi {tunti} tunnin jälkeen!")
kisa.tulosta_tilanne()
