# Napisz program, który sprawdzi czy dwa odcinki, które podaje użytkownik, przecinają się na płaszczyźnie.
# Jako element wyznaczający płaszczyznę można wybrać kartezjański układ współrzędnych.


def przeciwnie_do_wskazowek_zegara(A, B, C):
    return (C.y - A.y) * (B.x - A.x) > (B.y - A.y) * (C.x - A.x)


def przecinanie(A, B, C, D):
    return przeciwnie_do_wskazowek_zegara(A, C, D) != przeciwnie_do_wskazowek_zegara(B, C, D) and przeciwnie_do_wskazowek_zegara(A, B, C) != przeciwnie_do_wskazowek_zegara(A, B, D)


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


print('Podaj wspolrzedne pierwszego odcinka:')
a = Point(float(input('x1:')), float(input('y1:')))
b = Point(float(input('x2:')), float(input('y2:')))
print('Podaj wspolrzedne drugiego odcinka:')
c = Point(float(input('x1:')), float(input('y1:')))
d = Point(float(input('x2:')), float(input('y2:')))

if przecinanie(a, b, c, d):
    print('Przecinaja sie')
else:
    print('Nie przecinaja sie')
