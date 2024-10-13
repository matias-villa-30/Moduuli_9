class Auto():
    def __init__(self, rekisteritunnus, huippunopeus, tämänhetkinen_nopeus, kuljettu_matka):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.tämänhetkinen_nopeus = tämänhetkinen_nopeus
        self.kuljettu_matka = kuljettu_matka

    def accelerate(self, velocidad):

        self.velocidad = velocidad
        self.tämänhetkinen_nopeus += velocidad

        if self.tämänhetkinen_nopeus > 142:
            self.tämänhetkinen_nopeus = 140

        elif self.tämänhetkinen_nopeus < 0:
            self.tämänhetkinen_nopeus = 0

    def drive(self, hours_drived):
        self.hours_drived = hours_drived
        self.km_drived = self.hours_drived * self.tämänhetkinen_nopeus
        self.kuljettu_matka += self.km_drived


    def main(self):

        self.drive(1.5)

        return f"Distance travelled: {self.kuljettu_matka:.0f} km"

auto = Auto("ABC123", "142 km/h", 60, 2000)
print(auto.main())