"""
2 If-Abfragen (Tag 1)
2.6 Die Firma "It Wasn't Me" hat folgende Anweisung an ihre Mitarbeiter ausgegeben:
    (vgl. das Diagramm p_2_6_handlungsanweisung.puml/.png)
    Erstelle ein Computerprogramm anhand des Ablaufplans.
"""
from hilfprogramme import yes_no_input

if __name__ == '__main__':
    print('H A N D L U N G S A N W E I S U N G')
    print('===================================')
    if yes_no_input('Funktioniert das System? ', 'ja/nein') == 'ja':
        print('Fummel nicht daran herum.')
        print('Alles wird gut.')
    elif yes_no_input('Bist Du schuld? ', 'ja/nein') == 'ja':
        print('Du Idiot!')
        if yes_no_input('Hat es jemand gemerkt? ') == 'ja':
            print('Du bist im Arsch!')
            if yes_no_input('Kannst Du jemand Anderem die Schuld zuschieben? ') == 'nein':
                print('Du bist wirklich im Arsch!')
            else:
                print('Keine Sorge, jemand anderes ist im Arsch.')
        else:
            print('Man wird Dich nie finden.')
    else:
        print('Dich trifft es nicht.')
