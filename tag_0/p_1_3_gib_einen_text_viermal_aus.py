"""
1 Einstieg (Tag 0)
1.3 Gib einen Text viermal aus.
Hinweis: Mit etwas herumprobieren geht das sehr schnell, ohne den Text 4-mal zu kopieren.
"""

if __name__ == '__main__':
    text = input('Bitte Text eingeben: ')
    print((text + '\n') * 4, end='')
