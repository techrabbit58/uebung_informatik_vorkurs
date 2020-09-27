"""
2 If-Abfragen (Tag 1)
2.1 Sortiere zwei vorher festgelegte Zahlen nach Größe und gib sie in der richtigen Reighenfolge aus.
"""
from hilfprogramme import float_number_input

if __name__ == '__main__':
    print('Vergleich von zwei Zahlen a und b und Ausgabe in aufsteigender Reihenfolge.')
    a = float_number_input('a? ')
    b = float_number_input('b? ')
    if a < b:
        print(a, '<', b)
    elif b < a:
        print(b, '<', a)
    else:
        print('Beide Zahlen sind gleich:', a)
