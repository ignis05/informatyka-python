# Kryptogram QEGTP XPYB PBRECBSYOMM ZFKHSQKKVIK BPORKOE został zaszyfrowany metodą Vigenere'a z wykorzystaniem słowa kluczowego KRYPTOLOGIA.
# Alfabety szyfrowe i treść wiadomości wpisz w polu odpowiedzi do zadania, oraz prześlij plik z programem pod nazwą:nazwisko.txt

alphabet = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
tempAlph = alphabet.copy()
used = []
tables = []

keyword = 'KRYPTOLOGIA'
keyword = keyword.replace(' ', '')

inp = 'QEGTP XPYB PBRECBSYOMM ZFKHSQKKVIK BPORKOE'

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
        out += alphabet[tables[x].index(a)]
        i += 1

print(out)
