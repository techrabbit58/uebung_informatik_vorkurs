"""
4 Listen (Tag 1)
4.6 Schreibe ein Programm, das als Eingabe einen Geldbetrag in EUR entgegennimmt und daraus
die Art und Anzahl an Geldscheinen und/oder Münzen ermittelt, die erforderlich sind, um den
gegebenen Betrag in Bar zu begleichen.
"""
from hilfprogramme import float_number_input

s_werte = [20000, 10000, 5000, 2000, 1000, 500]
m_werte = [200, 100, 50, 20, 10, 5, 2, 1]
werte = s_werte + m_werte

scheine = ['200 EUR', '100 EUR', '50 EUR', '20 EUR', '10 EUR', '5 EUR']
muenzen = ['2 EUR', '1 EUR', '50 Cent', '20 Cent', '10 Cent', '5 Cent', '2 Cent', '1 Cent']
stuecke = scheine + muenzen

assert len(werte) == len(stuecke)

if __name__ == '__main__':
    betrag = round(float_number_input('Betrag in Euro? ', german=True), 2)
    betrag = int(betrag * 100)
    print('Betrag in Euro-Cent:', betrag)
    index = 0
    ergebnis = []
    while betrag > 0:
        anzahl = betrag // werte[index]
        betrag %= werte[index]
        if anzahl > 0:
            ergebnis.append(str(anzahl) + ' mal ' + stuecke[index])
        index += 1
    print(ergebnis)
