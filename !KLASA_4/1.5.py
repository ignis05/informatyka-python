# Odszyfruj kryptogram: BZOIJPYECYNSNEAEDOZNUZNCDOCK zaszyfrowany metodą płotową.
# Wykorzystano tutaj płot o wysokości 3. Przy szyfrowaniu pominięto spacje.
# Do oceny prześlij plik o nazwie: nazwisko.txt, a tekst odszyfrowany wpisz w polu odpowiedzi.
import math

inp = 'BZOIJPYECYNSNEAEDOZNUZNCDOCK'
height = 3

inp = input('Podaj text:\n')
height = int(input('Podaj wysokosc:\n'))

fence = []
lengths = []
for i in range(0, height):
    fence.append([])
    lengths.append([])

index = 0
direction = 1
for x in inp:
    if index + direction == len(lengths) or index + direction < 0:
        direction = 0 - direction
    lengths[index].append(x)
    index += direction

index = 0
for i in range(0, height):
    for j in range(0, len(lengths[i])):
        fence[i].append(inp[index])
        index += 1

print('fence:')
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
