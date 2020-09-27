"""
1 Einstieg (Tag 0)
1.4 Dividiere 2 Zahlen. Was passiert, wenn Du durch Null teilst?
"""
from hilfprogramme import float_number_input

if __name__ == '__main__':
    print('Division von zwei Zahlen: x = a / b.')
    a = float_number_input('a? ')
    b = float_number_input('b? ')
    try:
        x = a / b
    except ZeroDivisionError as err:
        print('Teilen durch Null ist nicht erlaubt und führt zum Programmabbruch.')
        print('*** Abbruch des Programms:', err, '***')
    else:
        print('x =', a, '/', b, '=', x)
        print('*** Normales Programmende ***')
