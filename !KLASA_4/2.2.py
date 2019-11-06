# Napisz program, który sprawdzi położenie punktu względem prostej. Równanie prostej oraz współrzędne punktu podaje użytkownik
import math
print('Podaj wspolczynniki rownania prostej k: Ax + By + C = 0')
a = float(input('A: '))
b = float(input('B: '))
c = float(input('C: '))

print('Podaj wspolrzedne punktu P(x0, y0):')
x0 = float(input('x0: '))
y0 = float(input('y0: '))

xd = math.fabs(a * x0 + b * y0 + c)/math.sqrt(a*a + b*b)
print('\n')

if xd == 0:
    print("Punkt P lezy na prostej k")
else :
    print("Odleglosc punktu P od prostej k wynosi " + str(xd))
