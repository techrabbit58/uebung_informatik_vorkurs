"""
2 If-Anweisungen (Tag 1)
2.5 Lass den Benutzer Temperatur (warm, kalt) und Wetter eingeben (regnerisch, verschneit, sonnig) und gib
    ihm einen Vorschlag zurück, wie er sich dem Wetter entsprechend kleiden soll.

Beispiel:
    -   Eingabe: Warm und sonnig
    -   Ausgabe: Ein T-Shirt reicht für heute völlig.
"""

temperatur = {'warm', 'kalt'}
wetter = {'regnerisch', 'verschneit', 'sonnig'}

if __name__ == '__main__':
    print('Wie sind Temperatur und Wetter heute?')
    print('Temperatur:', temperatur)
    print('Wetter:', wetter)
    print('Ist es heute eher regnerisch, schneit es, oder ist es verschneit? Oder ist es eher sonnig?')
    wetterbericht = input('Wie ist das Wetter heute? ').lower().split()
    if 'warm' in wetterbericht:
        if 'regnerisch' in wetterbericht:
            print('Du solltest Gummistiefel und eine Regenjacke anziehen.')
        elif 'verschneit' in wetterbericht:
            print('Ich empfehle festes Schuhwerk und eine leichte Winterjacke.')
        elif 'sonnig' in wetterbericht:
            print('Ein T-Shirt reicht für heute völlig.')
        else:
            print('Ein Daunenmantel ist heute eher nicht zu empfehlen.')
    elif 'kalt' in wetterbericht:
        if 'regnerisch' in wetterbericht:
            print('Am besten wird wohl sein: feste Schuhe, warmer Pullover und Regenjacke.')
        elif 'verschneit' in wetterbericht:
            print('Für den kalten Wintertag sind Pullover und eine warme Daunenjacke empfehlenswert.')
        elif 'sonnig' in wetterbericht:
            print('Feste Schuhe, Wintermantel und Sonnenbrille sind angesagt.')
        else:
            print('Ziehe Dich bitte warm an.')
    else:
        print('Diese Temperatur kenne ich nicht.')
