# Napisz program, który sprawdzi czy z trzech podanych boków można utworzyć trójkąt.
# Dodatkowo sprawdź czy utworzony trójkąt jest trójkątem prostokątnym. Użytkownik podaje trzy długość boków z klawiatury (zabezpiecz dodatkowo program,
# tak aby nie można było podać wartości ujemnych).
# Do oceny prześlij plik o nazwie: trojkat.txt.

while True:
    print('Podaj boki trojkata:')
    a = int(input('a = '))
    if a <= 0:
        print('Bok musi byc dodatni\n========')
        continue
    b = int(input('b = '))
    if b <= 0:
        print('Bok musi byc dodatni\n========')
        continue
    c = int(input('c = '))
    if c <= 0:
        print('Bok musi byc dodatni\n========')
        continue

    tab = [a, b, c]
    tab.sort()

    x = tab[0]
    y = tab[1]
    z = tab[2]

    if x + y <= z:
        print('Nie mozna utworzyc trojkata')
    else:
        print('Mozna utworzyc trojkat')
        if x * x + y * y == z * z:
            print('Utworzony trojkat jest prostokatny')
        else:
            print('Utworzony trojkat nie jest prostakatny')

    print('========')
