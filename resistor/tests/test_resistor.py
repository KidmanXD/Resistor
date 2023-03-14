import pytest
from resistor.Resistor import Resistor


def test_resistance_1():
    resistor = Resistor("красный", "желтый", "зеленый")
    assert resistor.resistance() == 24


def test_resistance_2():
    resistor = Resistor("черный", "коричневый", "красный", "оранжевый", "желтый")
    assert resistor.resistance() == 2000


def test_resistance_3():
    resistor = Resistor("красный", "желтый", "зеленый", "синий", "фиолетовый")
    assert resistor.resistance() == 48000000


def test_resistance_4():
    resistor = Resistor("синий", "красный", "желтый")
    assert resistor.resistance() == 62


def test_resistance_5():
    resistor = Resistor("синий", "бежевый", "желтый")
    assert KeyError


def test_tolerance_1():
    resistor = Resistor("красный", "желтый", "зеленый")
    assert resistor.tolerance() == None


def test_tolerance_2():
    resistor = Resistor("черный", "коричневый", "красный", "оранжевый", "зеленый")
    assert resistor.tolerance() == None


def test_tolerance_3():
    resistor = Resistor("синий", "красный", "желтый", "красный")
    assert resistor.tolerance() == 20


def test_tolerance_4():
    resistor = Resistor("красный", "желтый", "зеленый", "желтый", "золотой")
    assert resistor.tolerance() == 5


def test_tolerance_5():
    resistor = Resistor("красный", "желтый", "зеленый", "желтый", "серебро")
    assert resistor.tolerance() == 10


if __name__ == "__main__":
    pytest
