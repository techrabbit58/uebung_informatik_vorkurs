"""
1 Einstieg (Tag 0)
1.5 Multipliziere 2 Zahlen.
"""
from hilfprogramme import float_number_input

if __name__ == '__main__':
    print('Multiplikation von zwei Zahlen: x = a * b.')
    a = float_number_input('a? ')
    b = float_number_input('b? ')
    x = a * b
    print('x =', a, '*', b, '=', x)
