"""
Teste die Cäsar-Verschlüsselungsfunktion.
"""
import pytest

from tag_3.p_12_caesar_verschluesselung import caesar


@pytest.mark.parametrize('wort, k, resultat',
                         [('Caesar', 3, 'fdhvdu'),
                          ('HAL', 1, 'ibm'),
                          ('Shrdlu', 13, 'fueqyh'),
                          ('Barbados', 13, 'oneonqbf'),
                          ('Brutus', 3, 'euxwxv')
                          ])
def test_wortliste(wort, k, resultat):
    assert caesar(wort, k) == resultat
