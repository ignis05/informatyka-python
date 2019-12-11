# Napisz program, który sprawdzi położenie punktu względem odcinka.
# Użytkownik podaje współrzędne początkowe i końcowe odcinka oraz współrzędne punktu.
# Program należy zabezpieczyć przed podaniem współrzędnych określających długość odcinka równą 0.
import math

def distance(a,b):
    return math.sqrt((a.x - b.x)**2 + (a.y - b.y)**2)

def is_between(a,c,b):
    return distance(a,c) + distance(c,b) == distance(a,b)

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

print('Podaj wspolrzedne odcinka:')
a = Point(float(input('x1:')), float(input('y1:')))
b = Point(float(input('x2:')), float(input('y2:')))
print('Podaj wspolrzedne punktu:')
c = Point(float(input('x1:')), float(input('y1:')))

if distance(a,b) == 0:
    print('Dlugosc odcinka wynosi 0')
else:
    if is_between(a,c,b):
        print('Punkt nalezy do odcinka')
    else :
        print('Punkt nie nalezy do odcinka')



