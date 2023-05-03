import pytest
from descifrar_clv import adivinar_clave

def test_adivinar_clave():
    lista_desordenada = [5, 2, 8, 1, 9, 0, 3, 7, 4, 6]
    lista_organizada = sorted(lista_desordenada)
    clave = [3, 5, 7, 9]
    clave_adivinada = adivinar_clave (clave, lista_organizada)

    assert clave_adivinada == "3579"