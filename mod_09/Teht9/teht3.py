class Auto:
    def __init__ (self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nopeus = 0
        self.kuljettu_matka = 2000

    def kiihdyta (self, nopeuden_muutos):
        self.nopeus += nopeuden_muutos
        if self.nopeus > self.huippunopeus:
            self.nopeus = self.huippunopeus
        elif self.nopeus < 0:
            self.nopeus = 0


    def kulje (self, tunnit):
        self.kuljettu_matka += tunnit * self.nopeus

my_auto = Auto("ABC-123", 142)

my_auto.kiihdyta(60)
print(f"Tämänhetkinen nopeus: {my_auto.nopeus} km/h ja kuljettu matka on {my_auto.kuljettu_matka} km.")

my_auto.kulje(1.5)
print(f"Kuljettu matka on {my_auto.kuljettu_matka:.0f} km.")
