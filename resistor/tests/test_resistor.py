import pytest
from resistor.Resistor import Resistor


def test_resistance_1():
    resistor = Resistor("красный", "черный")
    assert resistor.resistance() == 20

def test_resistance_2():
    resistor = Resistor("синий", "красный", "желтый")
    assert resistor.resistance() == 62

def test_resistance_3():
    resistor = Resistor("черный", "коричневый", "красный", "оранжевый")
    assert resistor.resistance() == 1000

def test_resistance_4():
    resistor = Resistor("красный", "желтый", "зеленый", "синий", "фиолетовый")
    assert resistor.resistance() == 48000000

def test_resistance_5():
    resistor = Resistor("синий", "бежевый", "желтый")
    assert KeyError


def test_tolerance_1():
    resistor = Resistor("красный", "желтый", "зеленый")
    assert resistor.tolerance() == None

def test_tolerance_2():
    resistor = Resistor("черный", "коричневый", "красный", "оранжевый", "зеленый")
    assert resistor.tolerance() == 0.5

def test_tolerance_3():
    resistor = Resistor("синий", "красный", "желтый", "красный")
    assert resistor.tolerance() == 2

def test_tolerance_4():
    resistor = Resistor("красный", "желтый", "зеленый", "желтый", "золотой")
    assert resistor.tolerance() == 5

def test_tolerance_5():
    resistor = Resistor("красный", "желтый", "зеленый", "желтый", "серебро")
    assert resistor.tolerance() == 10


def test_tolerance_and_resistance_1():
    resistor = Resistor("красный", "желтый", "зеленый", "желтый", "серебро")
    assert resistor.resistance() == 240002
    assert resistor.tolerance() == 10

def test_tolerance_and_resistance_2():
    resistor = Resistor("зеленый", "зеленый", "красный")
    assert resistor.resistance() == 55
    assert resistor.tolerance() == None

def test_tolerance_and_resistance_3():
    resistor = Resistor("синий", "красный", "черный", "белый")
    assert resistor.resistance() == 62000000000
    assert resistor.tolerance() == None

def test_tolerance_and_resistance_4():
    resistor = Resistor("синий", "красный", "черный", "белый", "золотой")
    assert resistor.resistance() == 62000000006
    assert resistor.tolerance() == 5

def test_tolerance_and_resistance_5():
    resistor = Resistor("белый", "белый", "белый", "белый", "серебро")
    assert resistor.resistance() == 99000000010
    assert resistor.tolerance() == 10


if __name__ == "__main__":
    pytest
