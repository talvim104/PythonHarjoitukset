class Hissi:
    def __init__(self,alin,ylin):
        self.alin = alin
        self.ylin = ylin
        self.nykyinen_kerros = alin

    def kerros_ylos(self,):
            if self.nykyinen_kerros < self.ylin:
                self.nykyinen_kerros += 1
                print(f"Hissi on kerroksessa {self.nykyinen_kerros}")

    def kerros_alas(self):
        if self.nykyinen_kerros > self.alin:
            self.nykyinen_kerros -= 1
            print(f"Hissi on kerroksessa {self.nykyinen_kerros}")

    def siirry_kerrokseen(self, uusi_kerros):
        while self.nykyinen_kerros < uusi_kerros:
            self.kerros_ylos()
        while self.nykyinen_kerros > uusi_kerros:
            self.kerros_alas()


class Talo:
    def __init__(self, alin_kerros, ylin_kerros, hissien_lukumaara):
        self.hissit = []
        for i in range(hissien_lukumaara):
            hissi = Hissi(alin_kerros, ylin_kerros)
            self.hissit.append(hissi)

    def aja_hissia(self, numero, kerros):
        hissi = self.hissit[numero]
        hissi.siirry_kerrokseen(kerros)

talo = Talo(1, 7, 2)

talo.aja_hissia(0, 5)
talo.aja_hissia(1, 7)
talo.aja_hissia(0, 1)