import pytest
from app import dividir, DivisionPorCeroError


def test_division_exacta():
    assert dividir(10, 2) == 5


def test_division_con_decimales():
    assert dividir(7, 2) == 3.5


def test_division_numeros_negativos():
    assert dividir(-10, 2) == -5


def test_division_por_cero_lanza_excepcion():
    with pytest.raises(DivisionPorCeroError):
        dividir(5, 0)


def test_tipo_invalido_lanza_typeerror():
    with pytest.raises(TypeError):
        dividir("10", 2)


def test_booleano_no_es_valido():
    with pytest.raises(TypeError):
        dividir(True, 2)


@pytest.mark.parametrize("a,b,esperado", [
    (100, 4, 25),
    (9, 3, 3),
    (1, 4, 0.25),
    (-8, -2, 4),
])
def test_division_parametrizada(a, b, esperado):
    assert dividir(a, b) == esperado
