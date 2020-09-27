"""
14 Game of Life (Tag 3)

Programmiere die Simulation Game of Life von Conway. In dieser Simulation wird das
Wachstum von Zellkulturen modellhaft nachgeahmt. Das Zellen-Modell ist sehr einfach.
Es werden Zellen simuliert, deren Leben von ihren Nachbarfeldern abhängt. Außer der
Eigenschaft "lebendig" haben diese Zellen keine weiteren Eigenschaften oder
Fähigkeiten.

Die Zellen siedeln auf einem in gleich große Felder eingeteilten Raster, das in Zeilen
und Spalten organisiert ist. Jede Feld hat eine durch ein Zahlenpaar (x, y) gekennzeichnete
Positionskennung (Koordinaten). Die Koordinaten zweier benachbarter Zellen liegen bezüglich
x und y maximal um 1 voneinander entfernt.

    (x-1, y+1) | (x, y+1) | (x+1, y+1)
    (x-1, y)   | (x, y)   | (x+1, y)
    (x-1, y-1) | (x, y-1) | (x+1, y-1)

Das Raster erstreckt sich in jeder Richtung ohne Begrenzung. x und y einer Koordinate sind
immer ganze Zahlen. Jede Rasterposition kann maximal 1 Zelle aufnehmen. Jede Rasterposition
ist einmalig.

Für das Zellwachstum gelten folgende Regeln:

-   Eine Zelle entsteht an einer Rasterposition, wenn genau drei Nachbarpositionen lebende
    Zellen enthalten.
-   Eine Zelle stirbt an Vereinsamumg, wenn sie weniger als zwei lebende unmittelbare Nachbarn
    besitzt.
-   Eine Zelle überlebt, sofern sie zwei oder drei lebende Nachbarn besitzt.
-   Eine Zelle stirbt wegen Überbevölkerung, wenn sie mehr als drei Nachbarn besitzt.

Zu Beginn der Simulation wird eine Ausgangssituation in Form einer bestehenden Zellkolonie
(d.h. Rasterbelegung) gesetzt. Daraus wird in der ersten Runde eine Folgebesiedlung erzeugt,
und dann rundenbasiert immer so weiter.

Eine Folgebesiedlung entsteht durch Errechnung des Folgezustandes (tot, lebendig) für jede
einzelne Zelle der aktuellen Besiedlung und Erzeugung einer neuen Besiedlung (d.h. das Raster
wird nicht geändert, sondern ein Nachfolge-Raster erstellt. Danach wird das erste Raster
verworfen. Die Folgebesiedlung wird zur Ausgangesituation für die nächste Runde.

Eine interessante Ausgangssituation, als Muster dargestellt, ist z.B. der sogenannte
"Glider" (. für "nicht belegt", * für "lebende Zelle"):
                                                           . * .
                                                           . . *
                                                           * * *

In der Rasterregion (0, 0, 3, 3) kann dies wie folgt notiert werden:

    { (0, 1), (1, 2), (2, 0), (2, 1), (2, 2) }

Wegen der Einzigartigkeit der Rasterpunkte kann man das Feld als Set speichern. Zu Beginn
wird die Ausgangssituation als Menge von Koordinaten-Tupeln im Set eingetragen.

Eine Folgebesiedlung wird als neues Set je Runde erstellt und wird als neue Ausgangssituation
der nächsten Runde festgelegt. Die vorherige Ausgangssituation wird "vergessen".

Im Set werden nur die Koordinaten der lebenden Zellen gespeichert. Ist eine Koordinate nicht im
Set enthalten, ist der Rasterunkt nicht besetzt und es lebt dort keine Zelle.

Das unendlich große Raster kann nicht insgesamt visualisiert werden. Stattdessen wird genau immer
der Teil des Rasters am Anfang und danach nach jeder Runde angezeigt, der lebende Zellen enthält.
Im minimalen Rastersegment, das Zellen enthält, werden die lebenden Zellen als "*" dargestellt,
und dazwischen liegende unbesetzte Rasterpunkte als ".". Die Darstellung folgt dem oben gegebenen
Beispiel einer Ausgangssituation.

Nachbarfelder werden je in den aktuellen Grenzen des besiedelten Segmentes enthaltener Koordinate
geprüft, indem die Nachbarkoordinaten aufgezählt und bei Vorhandensein im Set gezählt werden. Eine
Zelle kann jederzeit 0 bis 8 Nachbarn haben. Daraus wird die Folgebelegung des betreffenden
Rasterpunktes ermittelt. Da das Raster nicht begrenzt ist, kann es bei der Nachbarschaftsprüfung
keine Bereichsüberschreitung bei x und y geben. Jede ganze Zahl inklusive 0 ist zulässig.

-   Neue oder überlebende Zelle: Die Koordinate wird dem Set der Folgebesiedlung hinzugefügt.
-   Zelle stirbt: Die Folgebesiedlung enthält diese Koordinate nicht, d.h. die Koordinate wird
    nicht hinzugefügt.

Es sollen mindestens die folgenden Klassen und Funktionen definiert werden, um die Ausführung der
Simulationsregeln und die Visualisierung des Rasters zu ermöglichen:

    Pair = namedtuple('Pair', 'x y')                # Eine einzelne Koordinate
    Area = namedtuple('Area', 'x y width height')   # Ursprungskoordinate und Größe eines
                                                    # Rastersegmentes
    Colony = Set[Pair]                        # Die Koordinaten der besiedelten Rasterpunkte

    init() -> Colony                          # Festlegen der Ausgangssituation
    area(colony: Colony) -> Area              # Ursprungskoordinate und Größe des besiedelten
                                              # Rastersegment ermitteln
    neighbour_count(pos: Pair, colony: Colony) -> int   # Die Anzahl der Nachbarn eines
                                                        # Rasterpunktes
    neighbours(pos: Pair) -> Pair, ...        # Generator, der die Nachbar-Positionen
                                              # eines Rasterpunktes aufzählt
    visualize(colony: Colony) -> str          # Erzeuge eine druckbare Representation des
                                              # besiedelten Rastersegmentes
    next_generation(colony: Colony): Colony   # Berechnet die Ausgangssituation für die nächste
                                              # Runde

Die Simulation soll zunächst die im Programm fest vorgegebene Ausgangssituation anzeigen und
danach Runde für Runde die Entwicklung der Kolonie berechnen und ausgeben. Zu Beginn jeder Runde
soll ein am Anfang zu 0 (Null) gesetzter Rundenzähler geprüft werden.

Steht der Rundenzähler auf 0, wird zuerst eine Rundenzahl erfragt.

Enhält der Rundenzähler eine natürliche Zahl größer 0, wird er um 1 vermindert, dann ein neuer
Besiedlungszustand der Kolonie errechnet und als neue Ausgangssituation gesetzt.

Wird eine neue Rundenzahl erfragt und als 0 (Null) eingegeben, beendet dies die Simulation
und das Programm endet.
"""
import time
from typing import Set, NamedTuple, Generator


class Pair(NamedTuple):
    x: int
    y: int


class Area(NamedTuple):
    x: int
    y: int
    width: int
    height: int


Colony = Set[Pair]


def init() -> Colony:
    x_, y_ = 0, 0
    return {
        Pair(x=x, y=y) for x, y in [[x_, y_ + 1], [x_ + 1, y_ + 2], [x_ + 2, y_], [x_ + 2, y_ + 1], [x_ + 2, y_ + 2]]
    }


def area(colony: Colony) -> Area:
    all_x = [x_ for x_, _ in colony]
    all_y = [y_ for _, y_ in colony]
    min_x = min(all_x)
    max_x = max(all_x)
    min_y = min(all_y)
    max_y = max(all_y)
    return Area(x=min_x, y=min_y, width=1 + max_x - min_x, height=1 + max_y - min_y)


def visualize(colony: Colony) -> str:
    x, y, width, height = area(colony)
    viz = []
    for x_ in range(x, x + width):
        row = []
        for y_ in range(y, y + height):
            row.append('*' if (x_, y_) in colony else '.')
        viz.append(' '.join(row) + '\n')
    return str((x, y)) + '\n' + ''.join(viz)


def neighbours(pos: Pair) -> Generator:
    yield Pair(pos.x - 1, pos.y - 1)
    yield Pair(pos.x, pos.y - 1)
    yield Pair(pos.x + 1, pos.y - 1)
    yield Pair(pos.x - 1, pos.y)
    yield Pair(pos.x + 1, pos.y)
    yield Pair(pos.x - 1, pos.y + 1)
    yield Pair(pos.x, pos.y + 1)
    yield Pair(pos.x + 1, pos.y + 1)


def neighbour_count(pos: Pair, colony: Colony) -> int:
    return len([p for p in neighbours(pos) if p in colony])


def next_generation(colony: Colony) -> Colony:
    """
    Für die Erzeugung der nächsten Generation muss rund um die Kolonie ein Wachstumsstreifen der Breite 1
    bereitgestellt werden, und der Ursprung muss um -1 in x- und y- Richtung verschoben werden.
    """
    x, y, width, height = area(colony)
    x -= 1
    y -= 1
    width += 2
    height += 2
    nexgen = set()
    for x_ in range(x, x + width):
        for y_ in range(y, y + height):
            pos = Pair(x_, y_)
            nc = neighbour_count(pos, colony)
            if nc == 3 or nc == 2 and pos in colony:
                nexgen.add(pos)
    return nexgen


if __name__ == '__main__':
    colony = init()
    print(visualize(colony))
    while True:
        s = input('Anzahl Runden (.le. 0 für Stop)? ')
        try:
            rounds_to_go = int(s)
        except ValueError:
            print('Ungeeignete Eingabe. Bitte eine positive ganze Zahl oder 0 eingeben.')
            continue
        if rounds_to_go <= 0:
            break
        for _ in range(0, rounds_to_go):
            colony = next_generation(colony)
            print(visualize(colony))
            time.sleep(.25)
    print('Auf Wiedersehen!')
