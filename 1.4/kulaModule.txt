from koloModule import *

class Kula:
    def __init__(self, radius):
        self.radius = radius

    def PolePow(self):
        return Circle(self.radius).Pole() * 4
    def Obj(self):
        return 4/3 *  self.radius * Circle(self.radius).Pole()