class Auto():
    def __init__(self, rekisteritunnus, huippunopeus, tämänhetkinen_nopeus=0, kuljettu_matka=0):
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



    def main(self):
        self.accelerate(30)
        self.accelerate(70)
        self.accelerate(50)
        print(f"Current speed is: {self.tämänhetkinen_nopeus} km/h")
        self.accelerate(-200)
        return f"Final speed is {self.tämänhetkinen_nopeus} km/h"

auto = Auto("ABC123", "142 km/h")
print(auto.main())