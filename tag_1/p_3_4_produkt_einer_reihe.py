"""
3 for/while-Schleifen (Tag 1)
3.4 Lass Dir das Produkt einer Reihe berechnen und gib das Ergebnis aus, z.B.:

        produkt(k=1, limit=n, ausdruck=(x + 1)/x)

Beispiel: Ergebnis für n=20 ist 21
"""


def produkt(k, limit, ausdruck):
    antwort = 1
    for x in range(1, limit + 1):
        antwort *= ausdruck(x)
    return antwort


if __name__ == '__main__':
    print('Das Produkt über (x + 1)/x für x in 1 bis 20 ist:', produkt(k=1, limit=20, ausdruck=lambda x: (x + 1) / x))
