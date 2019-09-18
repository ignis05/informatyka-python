# Odszyfruj kryptogram: AWYKWIAPCSSOYERAZTZCZ zaszyfrowany metodą kolumnową.
# Wykorzystano tutaj tablicę dwuwymiarową zawierającą 3 kolumny oraz klucz: 2, 0, 1.
# Podczas szyfrowania pominięto spacje. Do oceny prześlij plik o nazwie: nazwisko.txt, a tekst odszyfrowany wpisz w polu odpowiedzi.

txt = 'AWYKWIAPCSSOYERAZTZCZ'
key = '201'


tab = [
    [],
    [],
    []
]

aa = int(len(txt) / len(key))
xx = 1
zz = 0

for i in key:
    while zz < aa * xx:
        tab[int(i)].append(txt[zz])
        zz += 1
    xx += 1

print(tab)

fin = ''
for i in range(0,aa):
    for j in range(0, len(key)):
        fin += tab[j][i]


print(fin)
