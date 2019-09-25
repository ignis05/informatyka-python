# Zaszyfruj metodą płotową tekst: WLASNE MALE OGNISKO CENNIEJSZE OD STOSU ZLOTA. Zastosuj płot o wysokości 2.
# Przy szyfrowaniu pomiń spacje.
# Do oceny prześlij plik o nazwie: nazwisko.txt, a tekst zaszyfrowany wpisz w polu odpowiedzi.

inp = 'WLASNE MALE OGNISKO CENNIEJSZE OD STOSU ZLOTA'
height = 2

# replace spaces
inp = inp.replace(' ', '')

fence = []

for i in range(0, height):
    fence.append([])

index = 0
direction = 1

for x in inp:
    if index + direction == len(fence) or index + direction < 0:
        direction = 0 - direction
    fence[index].append(x)
    index += direction

print(fence)

out = ''
for x in fence:
    out += ''.join(x)

print(out)
