"""
2 If-Abfragen (Tag 1)
2.2 Bestimme die größte von drei vorher festgelegten Zahlen und gib diese Zahl aus.
"""
from hilfprogramme import float_number_input

if __name__ == '__main__':
    print('Bestimmung der größten von drei Zahlen a, b und c.')
    a = float_number_input('a? ')
    b = float_number_input('b? ')
    c = float_number_input('c? ')
    print('a =', a, '| b =', b, '| c =', c)
    if a >= b and a >= c:
        answer = a
    elif b >= a and b >= c:
        answer = b
    else:
        answer = c
    print('Die größte Zahl ist', answer)
