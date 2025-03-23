class Hissi:
    def __init__(self,alin,ylin):
        self.alin = alin
        self.ylin = ylin
        self.nykyinen_kerros = alin

    def kerros_ylos(self,):
            if self.nykyinen_kerros < self.ylin:
                self.nykyinen_kerros += 1
                print(f"Hissi on nyt kerroksessa {self.nykyinen_kerros}")

    def kerros_alas(self):
        if self.nykyinen_kerros > self.alin:
            self.nykyinen_kerros -= 1
            print(f"Hissi on nyt kerroksessa {self.nykyinen_kerros}")

    def siirry_kerrokseen(self, uusi_kerros):
        while self.nykyinen_kerros < uusi_kerros:
            self.kerros_ylos()
        while self.nykyinen_kerros > uusi_kerros:
            self.kerros_alas()


class Talo:
    def __init__(self, alin_kerros, ylin_kerros, hissien_lukumaara):
        self.alin_kerros = alin_kerros
        self.ylin_kerros = ylin_kerros
        self.hissit = []

        for i in range(hissien_lukumaara):
            uusi_hissi = Hissi(alin_kerros, ylin_kerros)
            self.hissit.append(uusi_hissi)




    def aja_hissia(self):








h = Hissi(1, 7)

h.siirry_kerrokseen(5)
h.siirry_kerrokseen(1)
