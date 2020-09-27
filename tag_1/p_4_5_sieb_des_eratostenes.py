"""
4 Listen (Tag 1)
4.5 Finde alle Primzahlen von 2 bis 100 mittels Sieb des Eratostenes.
"""


def sieb(limit=100):
    kandidaten = list(range(3, limit + 1, 2))
    k = kandidaten[0]
    antwort = []
    obergrenze = (limit + 1) ** 0.5
    while k < obergrenze:
        antwort.append(k)
        kandidaten = [n for n in kandidaten if n % k != 0]
        k = kandidaten[0]
    antwort += kandidaten
    return [2] + antwort


if __name__ == '__main__':
    print(sieb())
