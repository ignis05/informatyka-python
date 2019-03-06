from kulaModule import *

promien = int(input("Podaj promień figury: "))
co = input("Wybierz zo chesz obliczyć:\n 1 - obwód koła\n 2 - pole koła\n 3 - pole powierzchni kuli\n 4 - objetosc kuli\n")
if co == "1":
    print("obwód koła:")
    print(Circle(promien).Obw())
if co == "2":
    print("pole koła:")
    print(Circle(promien).Pole())
if co == "3":
    print("pole powierzchni kuli:")
    print(Kula(promien).PolePow())
if co == "4":
    print("objetosc kuli:")
    print(Kula(promien).Obj())

