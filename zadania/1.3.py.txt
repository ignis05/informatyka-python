import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def Pole(self):
        return self.radius  * self.radius * math.pi
    def Obw(self):
        return 2 * self.radius * math.pi


class Walec:
    def __init__(self, radius, h):
        self.circle = Circle(radius)
        self.h = h

    def PolePowierzchni(self):
        return (2* self.circle.Pole()) + (self.circle.Obw() * self.h)

    def Objetosc(self):
        return self.circle.Pole() * self.h

walec = Walec(3,3)
print(walec.PolePowierzchni())
print(walec.Objetosc())