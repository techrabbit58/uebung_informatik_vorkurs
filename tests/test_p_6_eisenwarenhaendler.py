"""
Teste das Programm p_6_eisenwarenhaendler.
"""
from tag_2.p_6_eisenwarenhaendler import Posten, hornbach


def test_ein_posten_eisenwaren_hat_den_erwarteten_wert():
    postenliste = [Posten('Schrauben', 1000), Posten('Muttern', 1000), Posten('Unterlegscheiben', 2000)]
    preisliste = {'Schrauben': 7, 'Muttern': 4, 'Unterlegscheiben': 2}
    erwarteter_betrag = (1000 * 7 + 1000 * 4 + 2000 * 2) / 100
    assert hornbach(postenliste, preisliste) == erwarteter_betrag
