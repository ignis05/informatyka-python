# Stosując metodę Cezara zaszyfruj tekst KLAMSTWO MA KROTKIE NOGI. Zastosuj klucz równy 9. Podaj alfabet szyfrowy i kryptogram utajnionej wiadomości.
# Alfabet szyfrowy i kryptogram wpisz w polu odpowiedzi do zadania, oraz prześlij plik z programem pod nazwą: nazwisko.txt

alph = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
key = 5
# key = int(input('Podaj klucz:\n'))
alph2 = alph.copy()

txt = 'SF SFZPJ SNLID SNJ OJXY EF UTEST'
# txt = input('Podaj text:\n')
txt = txt.lower()

for a in range(0, key):
    alph2.append(alph2.pop(0))

print(alph)
print(alph2)

out = []
for a in txt:
    try:
        out.append(alph[alph2.index(a)])
    except:
        out.append(a)

print(''.join(out))