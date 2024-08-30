"""
9 Lotto (Tag 2)

Schreiben Sie eine Funktion 'lotto()', welche sechs Zufallszahlen von 1 bis 49 ausgibt.

- Wie generiert man Zufallszahlen?
    Verwendung der Python-Standadbibliothek 'random'.

- Wie garantiert man, dass diese im gewünschten Zahlenbereich sind?
    1 - Liste der Zahlen 1 bis 49 erstellen
    2 - Mittels random.shuffle() die Reihenfolge zufällig wählen
    3 - die ersten sechs Zahlen der Liste ausgeben

    Da jede Zahl nur einmal in der Liste stand und zum gewünschten Bereich gehört und
    keine Zahlen außerhalb des Bereiches vorkommen, ist eine gültige Ausgabe garantiert.

- Wie garantiert man, dass nur sechs Zahlen gezogen werden?
    Das Ziehungsverfahren stellt sicher, dass genau sechs Zahlen aus 49 erhalten werden.

- Welchen Rückgabewert hat die Funktion?
    Eine Liste mit 6 wie oben beschrieben gezogenen Zahlen aus 1 bis 49
"""
import random


def lottoziehung():
    trommel = list(range(1, 49 + 1))
    random.shuffle(trommel)
    return trommel[:6]


if __name__ == '__main__':
    print(lottoziehung())
