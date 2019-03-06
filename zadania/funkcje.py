import math

def kwardratowe(a,b,c):
    delta = (b*b) - 4 * a * c
    if delta == 0:
        print(str(-b / (2*a)))
    elif  delta > 0:
        x1 = (-b - math.sqrt(delta)) / (2 * a)
        x2 = (-b + math.sqrt(delta)) / (2 * a)
        print(x1)
        print(x2)
    else:
        print("brak")
kwardratowe( int(input("a")),int(input("b")),int(input("c")) )