# Operacje jakie możemy wykonać na bazie to: dodawanie nowego wpisu, wyszukiwanie, usuwanie wpisów. Dane mają być zapisywane w pliku zewnętrznym np. *.json, *.txt.
from Client import *
import json
from pprint import pprint


class Database:
    # def __init__(self):
    #     with open('data.json', 'w') as outfile:
    #         json.dump({"table":[]}, outfile)

    def insert(self, firma, kod, miasto, ulica, osoba, mail, tel):
        with open('data.json') as f:
            data = json.load(f)
            client = Client(firma, kod, miasto, ulica, osoba, mail, tel).getJSON()
            data['table'].append(client)
            with open('data.json', 'w') as outfile:
                json.dump(data, outfile)

    def delete(self, klucz, wartosc):
        with open('data.json') as f:
            data = json.load(f)
            i = 0
            for entry in data["table"]:
                if entry[klucz] == wartosc:
                    del data["table"][i]
                i += 1
            with open('data.json', 'w') as outfile:
                json.dump(data, outfile)

    def get(self, klucz, wartosc):
        with open('data.json') as f:
            data = json.load(f)
            for entry in data["table"]:
                if entry[klucz] == wartosc:
                    print(entry)
                    return entry

    def getAll(self, ):
        with open('data.json') as f:
            data = json.load(f)
            pprint(data)


db = Database()

while True:
    print("0 - wyjscie")
    print("1 - wyswietl baze danych")
    print("2 - wyszukaj wpis w bazie danych")
    print("3 - dodaj wpis do bazy danych")
    print("4 - usuń wpis z bazy danych")
    co = int(input("Co chesz zrobic?\n"))
    if co == 0:
        break
    if co == 1:
        db.getAll()
    if co == 2:
        key = input("Podaj klucz wyszukiwania\n")
        value = input("Podaj wartosc klucza\n")
        db.get(key, value)
    if co == 3:
        firma = input("Podaj nazwe firmy\n")
        kod = input("Podaj kod pocztowy\n")
        miasto = input("Podaj miasto\n")
        ulica = input("Podaj ulicę\n")
        osoba = input("Podaj osobę do kontaktu\n")
        mail = input("Podaj kadres email\n")
        tel = input("Podaj numer telefonu\n")
        db.insert(firma, kod, miasto, ulica, osoba, mail, tel)
    if co == 4:
        key = input("Podaj klucz wyszukiwania wpisu do usunięcia\n")
        value = input("Podaj wartosc klucza\n")
        db.delete(key, value)
