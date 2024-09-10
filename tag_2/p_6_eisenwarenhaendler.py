"""
6 Eisenwarenhändler (Tag 2)

Ein Eisenwarenhändler bietet verschiedenste Waren zu unterschiedlichen Preisen an. Er führt unter anderem auch
Schrauben, Muttern und Unterlegscheiben.

Die Preise für die Artikel sind:

    - Schrauben: 7 ct
    - Muttern: 4 ct
    - Unterlegscheiben: 2 ct

A u f g a b e

Schreiben Sie eine Funktion 'hornbach()', die für eine gegebene Anzahl Schrauben, Muttern und Unterlegscheiben den
Endpreis berechnet.

Z u m  V o r g e h e n

    - Wie viele Parameter nimmt die Funktion an?
        - Zwei Parameter:
          - Eine Liste von Posten-Datensätzen (Artikel und Anzahl)
          - Eine Liste von Preis-Datensätzen (Artikel und Einzelpreis)

    - Wie genau errechnet sich der Preis?
        - Wir suchen den Gesamtpreis. Dieser ist zunächst 0 EUR
        - Für alle Sätze der Posten-Liste wird der Einzelpreis des jeweiligen Artikels aus der
          Preisliste heraus gesucht und mit der Anzahl aus der Posten-Liste multipliziert.
        - Das Ergebnis wird dem Gesamtpreis addiert.
        - Wenn alle Posten erfasst wurden, ist der Gesamtpreis das Ergebnis und
          wird an den Aufrufer der Funktion zurückgegeben.
        - Alle Werte und Berechnungen verwenden Beträge in ct.

    - Was gibt die Funktion als Rückgabewert?
        - Summe aller Einzelpreise aus der Preisliste, multipliziert mit den Artikelanzahlen
          aus der Quantitäten-Liste, geteilt durch 100, sodass sich EUR Beträge ergeben.
"""
from collections import namedtuple
from typing import List, Dict

Posten = namedtuple('Posten', 'artikel anzahl')


def hornbach(postenliste: List[Posten], preisliste: Dict[str, int]) -> float:
    gesamtpreis = 0
    for posten in postenliste:
        gesamtpreis += posten.anzahl * preisliste[posten.artikel]
    return gesamtpreis / 100
