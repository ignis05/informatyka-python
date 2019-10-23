# Podaj specyfikację oraz skonstruuj algorytm w postaci programu szyfrujący i deszyfrujący metodą Vigenere'a wiadomość wprowadzana z klawiatury.
# Słowo kluczowe (po usunięciu spacji i powtarzających się znaków) należy wpisać z klawiatury.
# Program powinien wypisywać tekst jawny, kryptogram oraz utworzone alfabety szyfrowe. Do oceny prześlij plik z programem pod nazwą: nazwisko.txt
while True:
    alphabet = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    tempAlph = alphabet.copy()
    used = []
    tables = []

    option = input('Wpisz 1 aby szyfrowac, wpisz 2 aby deszyfrowac:\n')

    if option != '1' and option != '2':
        break

    keyword = input('Podaj slowo kluczowe:\n')
    keyword = keyword.upper().replace(' ', '')

    inp = input('Podaj text wejsciowy:\n').upper()

    for a in keyword:
        if a not in used:
            used.append(a)
            tempAlph = alphabet.copy()
            for i in range(0, alphabet.index(a)):
                tempAlph.append(tempAlph.pop(0))
            print(tempAlph)
            tables.append(tempAlph.copy())

    out = ''
    i = 0
    for a in inp:
        if a == ' ':
            out += a
        else:
            x = i % len(tables)
            if option == '1':
                out += tables[x][alphabet.index(a)]
            else:
                out += alphabet[tables[x].index(a)]
            i += 1

    print(out)
    print('\n\n\n')
