"""
7 Satz von Pick (Tag 2)

Der Satz von Pick hilft bei der Berechnung der Fläche, die durch eine gerasterte Abbildung eingenommen wird.

Voraussetzung für die Anwendbarkeit ist, dass alle Punkte der Abbildung auf Rasterpunkten der Abbildungsfläche
liegen, und die Rasterpunkte regelmäßige Größe und horizontale und vertikale Ausrichtung haben (Zeilen- und
Spalten-Punkte).

Satz von Pick:

    Sei i die Anzahl der innen liegenden Bildpunkte und sei r die Anzahl der Randpunkte eines Polygonzuges.
    Dann ist die Fläche des Bildes:
                                         A = i + r / 2 - 1

Schreibe eine Funktion 'pick()', die o.g. Formel berechnet.
"""


def pick(innenpunkte, randpunkte):
    return innenpunkte + randpunkte / 2 - 1
