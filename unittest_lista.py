# Crea una suite de tests mediante UnitTest que comprueben las 3 funciones que has
# desarrollado en los ejercicios anteriores. Procura que los tests unitarios cubran lo
# mejor posible la aparición de comportamientos no deseados. 
import unittest

class TestFunciones(unittest.TestCase):
    def test_estaEnRango_true(self):
        # Caso de prueba para estaEnRango con valor en el rango
        self.assertTrue(estaEnRango(5, 1, 10))

    def test_estaEnRango_false(self):
        # Caso de prueba para estaEnRango con valor fuera del rango
        self.assertFalse(estaEnRango(15, 1, 10))

    def test_estaEnLista_true(self):
        # Caso de prueba para estaEnLista con valor presente en la lista
        self.assertTrue(estaEnLista(11, [6, 14, 11, 3, 2, 1, 15, 19]))

    def test_estaEnLista_false(self):
        # Caso de prueba para estaEnLista con valor no presente en la lista
        self.assertFalse(estaEnLista(7, [6, 14, 11, 3, 2, 1, 15, 19]))

    def test_estaEnLista_lista_vacia(self):
        # Caso de prueba para estaEnLista con una lista vacía
        self.assertFalse(estaEnLista(5, []))

    def test_estaEnLista_tipos_mixtos(self):
        # Caso de prueba para estaEnLista con tipos de datos mixtos en la lista
        self.assertTrue(estaEnLista("apple", ["banana", 123, "apple", True]))

    def test_estaEnLista_valores_nulos(self):
        # Caso de prueba para estaEnLista con valores nulos en la lista
        self.assertTrue(estaEnLista(None, [None, "cat", 42]))

unittest.main()