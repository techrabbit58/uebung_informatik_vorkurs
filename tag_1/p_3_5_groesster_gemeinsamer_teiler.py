"""
3 for/while-Schleifen (Tag 1)
3.5 Berechne für zwei Zahlen den GGT unter Verwendung einer Variante des euklidischen Algorithmus.

Beispiel: Ergebnis für 7 und 9 ist 1, für 5 und 10 ist 5, für 24 und 87 ist 3.
"""


def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


if __name__ == '__main__':
    assert gcd(7, 9) == 1
    assert gcd(5, 10) == 5
    assert gcd(24, 87) == 3
