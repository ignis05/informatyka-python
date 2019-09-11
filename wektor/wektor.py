# wektor
import math


class Wektor:
    def __init__(self):
        self.x = 0
        self.y = 0

    def utworz(self, x, y):
        self.x = x
        self.y = y

    def wyswietl(self):
        print("[" + str(self.x) + " ; " + str(self.y) + "]")

    def dlugosc(self):
        dl = math.sqrt(self.x * self.x + self.y * self.y)
        return dl


class Wektory(Wektor):
    def __init__(self, x1, y1, x2, y2):
        self.wektor1 = Wektor()
        self.wektor2 = Wektor()

        self.wektor1.utworz(x1, y1)
        self.wektor2.utworz(x2, y2)

    def suma(self):
        sumaX = self.wektor1.x + self.wektor2.x
        sumaY = self.wektor1.y + self.wektor2.y
        sumaWektor = Wektor()
        sumaWektor.utworz(sumaX, sumaY)
        sumaWektor.wyswietl()

    def iloczyn(self, ktoryWektor, iloczyn):
        if ktoryWektor == 1:
            wektor = self.wektor1
        else:
            wektor = self.wektor2
        ilX = wektor.x * iloczyn
        ilY = wektor.y * iloczyn
        iloczynWektor = Wektor()
        iloczynWektor.utworz(ilX, ilY)
        iloczynWektor.wyswietl()


xd = Wektor()
xd.utworz(1, 5)
xd.wyswietl()

w = Wektory(1, 2, 3, 4)
w.suma()
w.iloczyn(1, 5)
w.iloczyn(2, 5)
