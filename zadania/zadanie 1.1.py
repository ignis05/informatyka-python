#zadanie 1.1 rzygotuj klasę o nazwie User. Zdefiniuj w niej dwa atrybuty (firstName i lastName), a następnie utwórz kilka innych atrybutów, które zwykle są przechowywane w profilu użytkownika. Zdefiniuj metodę o nazwie describeUser(), wyświetlającą podsumowanie informacji zebranych o użytkowniku. Utwórz jeszcze drugą metodę o nazwie greetUser(), która będzie wyświetlała użytkownikowi spersonalizowane powitanie. Utwórz kilka egzemplarzy reprezentujących różnych użytkowników, a następnie dla każdego z nich wywołaj obie metody. Po sprawdzeniu poprawności działania prześlij plik o nazwie user.txt do oceny.
class User():
    def __init__(self, firstName, lastName,email,passwd):
        self.firstName = firstName
        self.lastName = lastName
        self.email = email
        self.passwd = passwd
        self.logins = 0

    def describeUser(self):
        print("Właściwości uzytkownika "+self.firstName + " " + self.lastName + ":")
        print("firstName = "+ self.firstName)
        print("lastName = "+ self.lastName)
        print("email = "+ self.email)
        print("passwd = "+ self.passwd)

    def greetUser(self):
        print("Witaj użytkowniku " + self.firstName + " " + self.lastName + "!")

    def login(self):
        self.logins = self.logins + 1

    def resetLogins(self):
        self.logins = 0

user1 = User("Grzegorz", "Mikołajczyk","email1@gmail.com","haslo123")
print(user1.logins)

for x in range(0,5) :
    user1.login()

print(user1.logins)

user1.resetLogins()
print(user1.logins)



