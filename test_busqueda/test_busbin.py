import pytest

from descifrar_clv import busqueda_binaria

def test_busqueda_binaria():
    assert busqueda_binaria([1, 2, 3, 4, 5], 4) == 3
    assert busqueda_binaria([1, 2, 3, 4, 5], 6) == -1
    assert busqueda_binaria([1, 2, 3, 4, 5], 0) == -1
    assert busqueda_binaria([], 1) == -1