import math
class Circle:
    def __init__(self, radius):
        self.radius = radius

    def Pole(self):
        return self.radius  * self.radius * math.pi
    def Obw(self):
        return 2 * self.radius * math.pi