class Auto:
    def __init__ (self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nopeus = 0
        self.kuljettu_matka = 0

    def kiihdytä (self, nopeuden_muutos):
        self.nopeus = self.nopeus + nopeuden_muutos
        if nopuden_muutos < 0:
            self.nopeus = 0
        elif nopeuden_muutos > self.huippunopeus:
            self.nopeus = self.huippunopeus


my_auto = Auto("ABC-123", 142)


print(f"Auton rekisteritunnus on {my_auto.rekisteritunnus}, huippunopeus on {my_auto.huippunopeus} km/h "
      f"ja tämänhetkinen nopeus on {self.nopeus} km/h. Kuljettu matka on {my_auto.kuljettu_matka} km.")