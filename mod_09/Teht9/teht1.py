class Auto:
    def __init__ (self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nopeus = 0
        self.kuljettu_matka = 0

my_auto = Auto("ABC-123", 142)
print(f"Auton rekisteritunnus on {my_auto.rekisteritunnus}, huippunopeus on {my_auto.huippunopeus} km/h "
      f"ja tämänhetkinen nopeus on {my_auto.nopeus} km/h. Kuljettu matka on {my_auto.kuljettu_matka} km.")