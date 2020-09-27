"""
3 for/while-Schleifen (Tag 1)
3.3 Lass Dir für eine festgelegte Basis und Exponenten eine feste Potenz berechnen.

Beispiele: 2^10 = 1024, 3^4 = 81
"""


def potenz(basis, exponent):
    antwort = basis
    for _ in range(1, exponent):
        antwort *= basis
    return antwort


if __name__ == '__main__':
    assert potenz(basis=2, exponent=10) == 1024
    assert potenz(basis=3, exponent=4) == 81
