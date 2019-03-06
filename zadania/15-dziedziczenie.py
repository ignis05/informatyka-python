# dziedziczenie

# klasa nadrzędna
class Car():
    """klasa reprezentujaca samochód tradycyjny"""

    def __init__(self,brand,model,year):
        """inicjalizacja atrybutów"""
        self.brand = brand
        self.model = model
        self.year = year
        self.odometer = 0 # atrybut przechowujący informację o przebiegu

    def descriptiveName(self):
        """zwrot sformatowanego opisu pojazdu"""
        longName = str(self.year) + " " + self.brand + " " + self.model
        return longName.title()

    def readOdometer(self):
        """informacja o przebiegu pojazdu"""
        print('Ten samochód ma przejechane ' + str(self.odometer) + " km.")

    def updateOdometer(self,valueOdometer):
        """aktualizacja stanu licznika"""
        if valueOdometer >= self.odometer:
            self.odometer = valueOdometer
        else:
            print('Nie mozna cofnąć licznika!!!!!!')

    def incrementOdometer(self,kilometers):
        """inkrementacja licznika pojazdu"""
        self.odometer += kilometers

# klasa potomna
