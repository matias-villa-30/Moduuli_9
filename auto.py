class Auto():
    def __init__(self, rekisteritunnus, huippunopeus, tämänhetkinen_nopeus=0, kuljettu_matka=0):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.tämänhetkinen_nopeus = tämänhetkinen_nopeus
        self.kuljettu_matka = kuljettu_matka

    def main(self):
        return self.rekisteritunnus, self.huippunopeus, self.tämänhetkinen_nopeus, self.kuljettu_matka


auto = Auto("ABC123", "142 km/h")

print(auto.main())