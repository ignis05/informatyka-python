# Odszyfruj kryptogram: BZOIJPYECYNSNEAEDOZNUZNCDOCK zaszyfrowany metodą płotową.
# Wykorzystano tutaj płot o wysokości 3. Przy szyfrowaniu pominięto spacje.
# Do oceny prześlij plik o nazwie: nazwisko.txt, a tekst odszyfrowany wpisz w polu odpowiedzi.
import math

inp = 'BZOIJPYECYNSNEAEDOZNUZNCDOCK'
height = 3

inp = input('Podaj text:\n')
height = int(input('Podaj wysokosc:\n'))

fence = []

for i in range(0, height):
    fence.append([])


partial_length = math.floor(len(inp) / (height + height-2))
rest = len(inp) % (height + height-2)

print(len(inp))
print('length:' + str(partial_length))
print('rest:' + str(rest))

xx = 1
tab = list(inp)

for i in range(0, height):
    p = partial_length
    if i != 0 and i != len(fence) - 1:
        p = partial_length * 2

    for ab in range(0, p):
        fence[i].append(tab[0])
        del tab[0]

    if i + 1 <= rest:
        fence[i].append(tab[0])
        del tab[0]

print(fence)

index = 0
direction = 1
out = ''

for x in inp:
    if index + direction == len(fence) or index + direction < 0:
        direction = 0 - direction

    out += fence[index][0]
    del fence[index][0]

    index += direction

print(out)