class Hissi:
    def __init__(self, alin, ylin):
        self.alin_kerros = alin
        self.ylin_kerros = ylin
        self.nykyinen_kerros = self.alin_kerros

    def siirryy_kerrokseen(self):




    def kerros_ylös(self):
        self.nykyinen_kerros = self.nykyinen.kerros + 1
        print(f"Olen keroksessa {self.nykyinen_kerros}")


my_hissi = Hissi(1, 7)

print(f"Hissi on {my_hissi.nykyinen_kerros} keroksessa")
