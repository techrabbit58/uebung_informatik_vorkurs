"""
8 Domino (Tag 2)

Schreiben Sie eine Funktion, welche Dominosteine bis zu einer gewissen Grenze N erzeugt.

Die Dominosteine können z.B. so aussehen: (1|1), (1|2), (1|3), (2|2), (2|3), (3|3), ...

Es dürfen dabei keine Duplikate auftreten. Ist beispielsweise (1|2) schon erzeugt, darf (2|1) nicht
erzeugt werden, da beide Paare als gleich angesehen werden.

Zum Vorgehen:

    - Welche Parameter erhält die Funktion?
        Ein parameter: 'grenze'

    - Wie erzeugt man die Dominosteine?
        - Laufvariable p von 1 bis N zählen.
        - Laufvariable q für jedes p von p bis N zählen.
        - Jedes (p|q) in die Ergebnisliste aufnehmen.

    - Wie verhindert man das Auftreten von Duplikaten?
        Durch das Erzeugungsverfahren wird jedes Paar nur genau einmal erstellt.

    - Welchen Rückgabewert hat die Funktion?
        Die Ergebnisliste.
"""


def domino(grenze):
    ergebnis = []
    for p in range(1, grenze + 1):
        for q in range(p, grenze + 1):
            ergebnis.append(f'({p}|{q})')
    return ergebnis


if __name__ == '__main__':
    print(', '.join(domino(6)))
