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

autot = []

for i in range(1, 11):
    rekisteritunnus = f"ABC-{i}"
    huippunopeus = random.randint(100, 200)
    auto = Auto(rekisteritunnus, huippunopeus)
    autot.append(auto)

#for auto in autot:
    #print(f"{auto.rekisteritunnus}: {auto.huippunopeus} km/h")

tunti = 0
kilpailu  = True

while kilpailu:
    tunti += 1
    for auto in autot:
        nopeuden_muutos = random.randint(-10, 15)
        auto.kiihdyta(nopeuden_muutos)
        auto.kulje(1)

        if auto.kuljettu_matka >= 10000:
            kilpailu = False

print(f"Kilpailu päättyi {tunti} tunnin jälkeen!")
print()
print("Tulokset:")

for auto in autot:
    print(f"Rekisteri: {auto.rekisteritunnus}")
    print(f"Huippunopeus: {auto.huippunopeus} km/h")
    print(f"Tämänhetkinen nopeus: {auto.nopeus} km/h")
    print(f"Kuljettu matka: {int(auto.kuljettu_matka)} km")
    print()
