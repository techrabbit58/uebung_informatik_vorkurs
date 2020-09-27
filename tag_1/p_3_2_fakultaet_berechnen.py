"""
3 for/whils-Schleifen (Tag 1)
3.2 Schreibe ein Programm, das für eine vorher festgelegte Zahl die Fakultät berechnet.

Beispiele:
    - 5! = 120
    - 10! = 3628800
"""


def fakultaet(n):
    antwort = 1
    while n > 1:
        antwort *= n
        n -= 1
    return antwort


if __name__ == '__main__':
    assert fakultaet(5) == 120
    assert fakultaet(10) == 3628800
