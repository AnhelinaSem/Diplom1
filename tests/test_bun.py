import pytest
from praktikum.bun import Bun

@pytest.mark.parametrize("name, price", [
    ("Sesame", 1.5),
    ("Whole Wheat", 2.0),
    ("Gluten Free", 2.5)
])
def test_bun_initialization(name, price):
    bun = Bun(name, price)
    assert bun.name == name
    assert bun.price == price

@pytest.mark.parametrize("name, price", [
    ("Sesame", 1.5),
    ("Whole Wheat", 2.0),
    ("Gluten Free", 2.5)
])
def test_bun_get_name(name, price):
    bun = Bun(name, price)
    assert bun.get_name() == name

@pytest.mark.parametrize("name, price", [
    ("Sesame", 1.5),
    ("Whole Wheat", 2.0),
    ("Gluten Free", 2.5)
])
def test_bun_get_price(name, price):
    bun = Bun(name, price)
    assert bun.get_price() == price
