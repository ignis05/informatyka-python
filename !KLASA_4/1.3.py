# Podaj specyfikację i skonstruuj algorytm w postaci programu deszyfrującego kryptogram uzyskany metodą kolumnową,
# w której wykorzystano tablicę dwuwymiarową zawierającą dowolna liczbę kolumn.
# Tekst zaszyfrowany, liczba kolumn oraz klucz mają być wprowadzane z klawiatury.

import math

txt_org = input("Podaj zaszyfrowany text\n")
key = input("Podaj klucz\n")



txt = list(txt_org)
# print(txt)


tab = []
for i in key:
    tab.append([])


partial_length = math.floor(len(txt) / len(key))
rest = len(txt) % len(key)
# print('length:'+str(partial_length))
# ('rest:'+str(rest))
xx = 1

for i in key:
    for ab in range(0, partial_length):
        tab[int(i)].append(txt[0])
        del txt[0]

    if int(i)+1 <= rest:
        tab[int(i)].append(txt[0])
        del txt[0]

# print(tab)

fin = ''
for i in range(0, partial_length +1):
    for j in range(0, len(key)):
        try:
            fin += tab[j][i]
        except:
            xdd='xd'

print('Odszyfrowany text:')
print(fin)
