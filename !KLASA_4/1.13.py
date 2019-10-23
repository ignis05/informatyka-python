# Stosując szyfr Vigenere'a, utwórz alfabety szyfrowe, w których zdaniem kluczowym będzie powiedzenie NIKT NIE JEST BEZ WAD.
# Korzystając z utworzonych alfabetów, zaszyfruj tekst GENIUSZ TO TYLKO SPRAWA CIERPLIWOSCI.
# Alfabety szyfrowe i kryptogram wpisz w polu odpowiedzi do zadania, oraz prześlij plik z programem pod nazwą: nazwisko.txt

alphabet = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
tempAlph = alphabet.copy()
used = []
tables = []

keyword = 'NIKT NIE JEST BEZ WAD'
keyword = keyword.replace(' ', '')

inp = 'GENIUSZ TO TYLKO SPRAWA CIERPLIWOSCI'

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
        out += tables[x][alphabet.index(a)]
        i += 1

print(out)
