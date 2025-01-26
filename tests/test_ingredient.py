import pytest
from praktikum.ingredient import Ingredient

@pytest.mark.parametrize("ingredient_type, name, price", [
    ("vegetable", "Lettuce", 0.5),
    ("vegetable", "Tomato", 0.7),
    ("dairy", "Cheese", 1.0)
])
def test_ingredient_initialization(ingredient_type, name, price):
    ingredient = Ingredient(ingredient_type, name, price)
    assert ingredient.get_type() == ingredient_type
    assert ingredient.get_name() == name
    assert ingredient.get_price() == price
