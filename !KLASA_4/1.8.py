
morse = {
    "0": "-----",
    "1": ".----",
    "2": "..---",
    "3": "...--",
    "4": "....-",
    "5": ".....",
    "6": "-....",
    "7": "--...",
    "8": "---..",
    "9": "----.",
    "a": ".-",
    "b": "-...",
    "c": "-.-.",
    "d": "-..",
    "e": ".",
    "f": "..-.",
    "g": "--.",
    "h": "....",
    "i": "..",
    "j": ".---",
    "k": "-.-",
    "l": ".-..",
    "m": "--",
    "n": "-.",
    "o": "---",
    "p": ".--.",
    "q": "--.-",
    "r": ".-.",
    "s": "...",
    "t": "-",
    "u": "..-",
    "v": "...-",
    "w": ".--",
    "x": "-..-",
    "y": "-.--",
    "z": "--..",
    ".": ".-.-.-",
    ",": "--..--",
    "?": "..--..",
    "!": "-.-.--",
    "-": "-....-",
    "/": "-..-.",
    "@": ".--.-.",
    "(": "-.--.",
    ")": "-.--.-",
    " ": " ",
}

morse_inv = {value: key for key, value in morse.items()}

# - . ... -   .- -... -.-.


def toMorse(text):
    out = ''
    for letter in text:
        out += morse[letter] + ' '
    return out[:-1]


def fromMorse(text):
    try:
        out = ''
        arr = text.split('   ')
        for i in arr:
            for j in i.split(' '):
                out += morse_inv[j]
            out += ' '
        return out
    except:
        return '( Błędny format )'


while True:
    op = input("==========\nPodaj operacje:\n1 - text -> morse\n2- morse -> text\n")
    if op == '1':
        print(toMorse(input("Podaj text:\n")))
    elif op == '2':
        print(fromMorse(input("Podaj kod morse'a\n")))
    else:
        break
