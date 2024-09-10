"""
3 for/while-Schleifen (Tag 1)
3.1 Bilde folgende Summe für ein vorher festgelegtes n:

            summe(k=1, limit=n, ausdruck=1 / x)

Beispiel:
    - n = 100
    - Ergebnis der Summierung: 5.187377517639621

Hinweis:
    - Die Lösung kann sowohl mit 'for' als auch mit 'while' realisiert werden.
"""


def summef(*, k, limit, ausdruck):
    antwort = 0
    for x in range(k, limit + 1):
        antwort += ausdruck(x)
    return antwort


def summew(*, k, limit, ausdruck):
    antwort = 0
    x = k
    while x <= limit:
        antwort = antwort + ausdruck(x)
        x = x + 1
    return antwort


if __name__ == '__main__':
    n = 100
    print('n =', n)
    print('Summe/for   |', summef(k=1, limit=n, ausdruck=lambda x: 1 / x))
    print('Summe/while |', summew(k=1, limit=n, ausdruck=lambda x: 1 / x))
