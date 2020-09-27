"""
2 If-Abfragen (Tag 1)
2.3 Sortiere drei vorher festgelegte Zahlen und gib sie in der richtigen Reihenfolge aus.
Hinweis: Zeichne dazu zuerst ein Ablaufdiagramm oder Flussdiagramm.
"""
from hilfprogramme import float_number_input

if __name__ == '__main__':
    print('Aufsteigende Sortierung von drei Zahlen a, b und c.')
    a = float_number_input('a? ')
    b = float_number_input('b? ')
    c = float_number_input('c? ')
    print('a =', a, '| b =', b, '| c =', c)
    if a <= c <= b:
        b, c = c, b
    elif b <= a <= c:
        a, b = b, a
    elif b <= c <= a:
        a, b, c = b, c, a
    elif c <= a <= b:
        a, b, c = c, a, b
    elif c <= b <= a:
        a, c = c, a
    else:
        pass
    print('Sortierte Reihenfolge: ', a, '->', b, '->', c)
