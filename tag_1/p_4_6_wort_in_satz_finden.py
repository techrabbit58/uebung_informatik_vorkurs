"""
4 Listen (Tag 1)
4.6 Lass die Benutzerin einen Satz und ein Wort eingeben. Finde heraus, ob das Wort im Satz
vorkommt und gib das Ergebnis zurück.

Beispiel:
    - Eingabe: 'Anneliese sitzt im Home Office am PC und arbeitet.' und 'Office'
    - Antwort: Das Wort kommt im gegebenen Satz vor.
"""

if __name__ == '__main__':
    satz = list(input('Satz? '))
    wort = list(input('Wort? '))
    verneinung = ''
    for k in range(0, len(satz) - len(wort)):
        if wort == satz[k:k + len(wort)]:
            break
    else:
        verneinung = 'nicht '
    print(f'Das Wort kommt im Satz {verneinung}vor.')
