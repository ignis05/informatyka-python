# szyfrowanie metodą kolumnową
txt_01 = 'UCZCIWOSC ZBIERA POCHWALY I UMIERA Z ZIMNA XD'
key = '3201'
txt = ''

# input mode
txt_01 = input("Podaj text\n")
key = input("Podaj klucz\n")

for i in txt_01:
    if i != ' ':
        txt += i


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

print(tab)
print('text oryginalny:\n'+txt_01+'\n')
print('text zaszyfrowany:\n'+final)
