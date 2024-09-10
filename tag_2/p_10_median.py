"""
10 Median (Tag 2)

Schreibe eine Funktion, die den Median berechnet.

Gegeben sei eine Reihe von Zahlen x[1], x[2], ..., x[n] und aufsteigend nach Wert sortiert.

Der Median sei definiert, wie folgt:

                 | x[(n + 1) // 2]                      falls n ungerade
    median(x) := <
                 | 0.5 * (x[n // 2] + x[(n // 2) + 1])   falls n gerade

    ACHTUNG! Weil in Python Listenelemente aufsteigend nicht mit 1, 2, 3, ...
    sondern mit 0, 1, 2, ... gezählt werden, müssen die errechneten Indizes jeweils um 1
    reduziert werden!

- Was für Parameter nimmt die Funktion entgegen?
    Eine Liste von n Zahlen

- Wie kann man die Funktion für beliebig viele Zahlen anwenden?
    Durch Verwendung einer Liste (oder eines Tupels etc.) als Parameter, da solche
    iterierbaren Strukturen definitionsgemäß beiebig viele Elemente haben können.

- Wie wird gewährleistet, dass die Zahlen sortiert sind?
    Die erhaltene Liste wird von der Funktion zunächst aufsteigend sortiert.
    Dafür wird die eingebaute Funktion 'sorted()' von Python angewendet.

- Wie unterscheidet man, ob n gerade oder ungerade ist?
    Feststellen der Listenlänge mit 'len()' und Fallunterscheidung mit 'if ...'

- Was gibt die Funktion zurück?
    Den erechneten Median gemäß Definition, d.h. eine einzelne Zahl.
"""
import random


def median(reihe_):
    reihe_ = sorted(reihe_)
    laenge = len(reihe_)
    if laenge % 2:  # laenge ist ungerade
        m = reihe_[(laenge + 1) // 2 - 1]
    else:           # laenge ist gerade
        m = (reihe_[laenge // 2 - 1] + reihe_[laenge // 2]) / 2
    return m


if __name__ == '__main__':

    reihe = [2, 3, 5, 7, 11]
    random.shuffle(reihe)
    assert median(reihe) == 5

    reihe = [2, 5, 11, 17, 101, 103]
    random.shuffle(reihe)
    assert median(reihe) == 14
