# Napisz program, który sprawdzi czy podany przez użytkownika punkt należy do podanego obszaru na płaszczyźnie.
# Użytkownik podaje współrzędne wyznaczające obszar na płaszczyźnie i współrzędne punku do sprawdzenia
# Do oceny prześlij plik o nazwie: punktObszar.txt.

print('Podaj wsporzedne obszaru:')
x1 = input('x1:')
y1 = input('y1:')
x2 = input('x2:')
y2 = input('y2:')
print('\nPodaj wspolrzedne punktu:')
x = input('x:')
y = input('y:')


if x2 < x1:
    x1, x2 = x2, x1
if y2 < y1:
    y1, y2 = y2, y1
if (x1 <= x <= x2) and (y1 <= y <= y2):
    print('Punkt należy do obszaru')
else:
    print('Punkt nie nalezy do obszaru')
