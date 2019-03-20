# Baza ma przechowywać następujące informację: nazwa firmy, kod pocztowy, miasto, ulica, osoba do kontaktu, mail i telefon.
class Client:
    def __init__(self, firma, kod, miasto, ulica, osoba, mail, tel):
        self.firma = firma
        self.kod = kod
        self.miasto = miasto
        self.ulica = ulica
        self.osoba = osoba
        self.mail = mail
        self.tel = tel

    def getJSON(self):
        return {
            "firma": self.firma,
            "kod": self.kod,
            "miasto": self.miasto,
            "ulica": self.ulica,
            "osoba": self.osoba,
            "mail": self.mail,
            "tel": self.tel
        }
