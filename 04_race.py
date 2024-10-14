import random
autos = []
i = 1

while i <= 10:
    autos.append(f"ABC-{i}")
    i += 1


class Auto():
    def __init__(self, rekisteritunnus, huippunopeus, tämänhetkinen_nopeus, kuljettu_matka):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.tämänhetkinen_nopeus = tämänhetkinen_nopeus
        self.kuljettu_matka = kuljettu_matka

    def accelerate(self, velocidad):

        self.velocidad = velocidad
        if self.velocidad > 0:
            self.tämänhetkinen_nopeus = min(self.huippunopeus, self.tämänhetkinen_nopeus + velocidad)

        else:
            self.tämänhetkinen_nopeus = max(0, self.tämänhetkinen_nopeus + self.velocidad)

    def drive(self, hours_drived):
        self.hours_drived = hours_drived
        self.km_drived = self.hours_drived * self.tämänhetkinen_nopeus
        self.kuljettu_matka += self.km_drived


    def main(self):

        self.velocidad = random.randint(-15, 10)
        self.accelerate(self.velocidad)
        self.drive(1)



        return f"{self.rekisteritunnus:10} | {self.huippunopeus:10} | {self.tämänhetkinen_nopeus:15} | {self.kuljettu_matka:15}"


for item in autos:
    max_speed = random.randint(100, 200)

    item = Auto(item, max_speed, 0, 0)
    while item.kuljettu_matka <= 10000:
        print(item.main())

