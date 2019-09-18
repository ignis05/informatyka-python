# szyfrowanie metodą kolumnową
txt_01 = 'UCZCIWOSC ZBIERA POCHWALY I UMIERA Z ZIMNA XD'
key = '3201'
txt = ''

# input mode
txt = input("Podaj text\n")
key = input("Podaj klucz\n")


tab = []
for i in key:
    tab.append([])

x = 0
for i in txt:
    tab[x % len(key)].append(i)
    x += 1


final = ''

for i in key:
    final += ''.join(tab[int(i)])

print('text zaszyfrowany:\n'+final)
