# Realiza el ejercicio 4 pero utilizando esta vez cualquier otro framework de terceros
# como por ejemplo pytest.
import pytest
from lista import estaEnRango, estaEnLista

def test_estaEnRango_true():
    assert estaEnRango(5, 1, 10) is True

def test_estaEnRango_false():
    assert estaEnRango(15, 1, 10) is False

def test_estaEnLista_true():
    assert estaEnLista(11, [6, 14, 11, 3, 2, 1, 15, 19]) is True

def test_estaEnLista_false():
    assert estaEnLista(7, [6, 14, 11, 3, 2, 1, 15, 19]) is False

def test_estaEnLista_lista_vacia():
    assert estaEnLista(5, []) is False

def test_estaEnLista_tipos_mixtos():
    assert estaEnLista("apple", ["banana", 123, "apple", True]) is True

def test_estaEnLista_valores_nulos():
    assert estaEnLista(None, [None, "cat", 42]) is True
