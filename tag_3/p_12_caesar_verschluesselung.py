"""
12 Cäsar-Verschlüsselung (Tag 3)

Programmiere eine Funktion, die einen String und eine Zahl k als Parameter entgegennimmt
und die Cäsar-Verschlüsselung zurückliefert. Bei dem sehr einfachen Verschlüsselungsverfahren
wird jeder Buchstabe zyklisch mit dem Buchstaben ersetzt, der im Alphabet k Buchstaben
weiter hinten steht.

Wie sollte ich dabei Groß- und Kleinschreibung behandeln?
    - Eingabe normalisieren, z.B. alle Eingaben mit str.lower() zu Kleinschreibung wandeln.

Die Funktion sollte mit einem oder mehreren Wörtern getestet werden.

Beispiel: caesar -- k=3 --> fdhvdu
"""


def caesar(s, k):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    eingabe = s.lower()
    ausgabe = ''
    for c in eingabe:
        i = (alphabet.index(c) + k) % len(alphabet)
        ausgabe += alphabet[i]
    return ausgabe
