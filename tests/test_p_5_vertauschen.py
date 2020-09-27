"""
Test der "tauschen()" Funktion aus p_5_vertauschen.py
"""
from tag_2.p_5_vertauschen import tauschen


def test_tausch_mit_zahlen():
    a, b = 1, 2
    assert b, a == tauschen(a, b)


def test_tausch_mit_strings():
    a, b = 'hello', 'world'
    assert b, a == tauschen(a, b)


def test_tausch_mit_listen():
    a, b = [1, 2, 3], [4, 5, 6]
    assert b, a == tauschen(a, b)
