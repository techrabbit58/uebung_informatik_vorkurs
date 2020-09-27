"""
Teste die 'pick()' funktion.
"""
from tag_2.p_7_satz_von_pick import pick


def test_satz_von_pick():
    assert pick(innenpunkte=37, randpunkte=42) == 57
