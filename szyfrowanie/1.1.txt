# szyfrowanie metodą kolumnową
txt_01 = 'UCZCIWOSC ZBIERA POCHWALY I UMIERA Z ZIMNA'
klucz = '3201'
txt = ''

for i in txt_01:
    if i != ' ':
        txt += i

tab = [
    [],
    [],
    [],
    []
]

x = 0

for i in txt:
    tab[x % 4].append(i)
    x += 1


final = ''

for i in klucz:
    final += ''.join(tab[int(i)])

print('text oryginalny:\n'+txt_01+'\n')
print('text zaszyfrowany:\n'+final)
