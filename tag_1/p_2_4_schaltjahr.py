"""
2 If-Abfragen (Tag 1)
2.4 Überprüfe, ob ein vorher festgelegtes Jahr ein Schaltjahr ist.

Hinweise:
    - Jahreszahl nicht durch 4 teilbar: kein Schaltjahr
    - Jahreszahl durch 4 teilbar: Schaltjahr
    - Jahreszahl durch 100 teilbar: kein Schaltjahr
    - Jahreszahl durch 400 teilbar: Schaltjahr

Beispiele:
    - 2000, 2004 sind Schaltjahre
    - 1900, 2006 sind keine Schaltjahre
"""


def ist_schaltjahr(jahr):
    return (jahr % 4 == 0 and jahr % 100 != 0) or jahr % 400 == 0


if __name__ == '__main__':
    print(f'Das Jahr 1900 ist', " ein" if ist_schaltjahr(1900) else "kein", 'Schaltjahr.')
    print(f'Das Jahr 2000 ist', " ein" if ist_schaltjahr(2000) else "kein", 'Schaltjahr.')
    print(f'Das Jahr 2001 ist', " ein" if ist_schaltjahr(2001) else "kein", 'Schaltjahr.')
    print(f'Das Jahr 2004 ist', " ein" if ist_schaltjahr(2004) else "kein", 'Schaltjahr.')
    print(f'Das Jahr 2006 ist', " ein" if ist_schaltjahr(2006) else "kein", 'Schaltjahr.')
