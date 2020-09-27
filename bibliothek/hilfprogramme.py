"""
Hilfsprogramme.
"""


def float_number_input(prompt, german=False):
    while True:
        result = input(prompt)
        if german:
            result = result.replace(',', '.')
        try:
            result = float(result)
        except ValueError:
            print('Fehler. Das war keine Zahl. Bitte nochmal.')
        else:
            return result


def yes_no_input(prompt, yes_no='ja/nein'):
    answer = None
    while answer not in yes_no.split('/'):
        answer = input(prompt + '(' + yes_no + ') => ')
    return answer
