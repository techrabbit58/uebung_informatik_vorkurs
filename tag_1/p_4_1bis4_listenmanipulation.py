"""
4 Listen (Tag 1)
"""

if __name__ == '__main__':
    # 4.1 Füge zwei vorher festgelegte Listen zu einer zusammen und gib das Resultat aus.
    A = [3, 8, 9, 2]
    B = [4, 6]
    print(f'{A=}, {B=}, {(A + B)=}')

    # 4.2 Entferne ein bestimmtes Element aus einer vorher festgelegten Liste.
    # Es sollen _alle_ Vorkommnisse des Löschkandidaten aus der Liste entfernt werden.
    A = [3, 8, 9, 5, 1, 3, 6, 4]
    E = 3
    X = [8, 9, 5, 1, 6, 4]
    Y = [y for y in A if y != E]
    print(f'{A=}, zu entfernendes Element {E=}, erwartetes Ergebnis {X=}')
    print(f'Tatsächliches Ergebnis: {Y=}')
    assert X == Y

    # 4.3 Trenne eine Lista an einer bestimmten Index-Position in zwei Teillisten.
    # Die Index-Zählung beginnt bei 0 (d.h. Index des ersten Litenelementes ist 0).
    # Es soll vor dem Eintrag an der Index-Stelle getrennt werden. Die erste Teilliste
    # bei Trennung an Index 0 wäre leer, die zweite, entspräche genau der Ausgangsliste.
    A = [1, 3, 5, 8, 9, 3]
    index = 3
    X_vorn = [1, 3, 5]
    X_hinten = [8, 9, 3]
    Y_vorn = A[:index]
    Y_hinten = A[index:]
    assert (X_vorn, X_hinten) == (Y_vorn, Y_hinten)

    # 4.4 Drehe eine vorher festgelegte Liste um. Verwende nicht die List.reverse()
    #     Methode, sondern versuche einen anderen Weg.
    A = [1, 3, 5, 8, 9, 3]
    X = [3, 9, 8, 5, 3, 1]
    Y = A[-1::-1]
    assert X == Y
