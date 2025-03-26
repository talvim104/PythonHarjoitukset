class Auto:
    def __init__ (self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nopeus = 0
        self.kuljettu_matka = 0

    def aseta_nopeus(self, uusi_nopeus):
        self.nopeus = min(uusi_nopeus, self.huippunopeus)

    def kulje(self, tunnit):
        self.kuljettu_matka += self.nopeus * tunnit

class Sähköauto(Auto):
    def __init__(self,rekisteritunnus, huippunopeus, akkukapasiteetti):
        self.akkukapasiteetti = akkukapasiteetti
        Auto.__init__(self, rekisteritunnus, huippunopeus)

class Polttomoottoriauto(Auto):
    def __init__(self, rekisteritunnus, huippunopeus, bensatankki):
        self.bensatankki = bensatankki
        Auto.__init__(self, rekisteritunnus, huippunopeus)

my_auto1 = Sähköauto("ABC-15",180, "52.5 kWh")
my_auto2 = Polttomoottoriauto("ACD-123", 150, "32.3 l")

my_auto1.aseta_nopeus(110)
my_auto2.aseta_nopeus(130)


my_auto1.kulje(3)
my_auto2.kulje(3)

print(f"{my_auto1.rekisteritunnus} on kulkenut {my_auto1.kuljettu_matka} km.")
print(f"{my_auto2.rekisteritunnus} on kulkenut {my_auto2.kuljettu_matka} km.")