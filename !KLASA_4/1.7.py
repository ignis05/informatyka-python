# Podaj specyfikację i skonstruuj algorytm w postaci programu szyfrujący
# i deszyfrujący wiadomość wczytywaną z klawiatury metodą płotową dla wysokości 2.

def odszyfruj(inp):
    height = 2
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

    index = 0
    direction = 1
    out = ''
    for x in inp:
        if index + direction == len(fence) or index + direction < 0:
            direction = 0 - direction

        out += fence[index][0]
        del fence[index][0]

        index += direction

    print('Odszyfrowany tekst:')
    print('=================')
    print(out)


def szyfruj(inp):
    height = 2
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

    out = ''
    for x in fence:
        out += ''.join(x)

    print('Zaszyfrowany tekst:')
    print('=================')
    print(out)


while True:
    wybor = input('1 - zaszyfruj\n2 - odszyfruj\ncokolwiek innego - zakoncz:\n')
    if wybor == '1':
        szyfruj(input('podaj tekst do szyfrowania:\n'))
        print('=================')
    elif wybor == '2':
        odszyfruj(input('podaj tekst do odszyfrowania:\n'))
        print('=================')
    else:
        break
