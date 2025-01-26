import pytest
from unittest.mock import Mock
from praktikum.bun import Bun
from praktikum.ingredient import Ingredient
from praktikum.burger import Burger

class TestBurger:

    def test_burger_initialization(self):
        burger = Burger()
        assert burger.bun is None
        assert len(burger.ingredients) == 0


    def test_burger_set_buns(self):
        bun = Bun("Sesame", 1.5)
        burger = Burger()
        burger.set_buns(bun)
        assert burger.bun == bun


    def test_burger_add_ingredient(self):
        ingredient = Ingredient("Lettuce", 0.5, "vegetable")
        burger = Burger()
        burger.add_ingredient(ingredient)
        assert len(burger.ingredients) == 1
        assert burger.ingredients[0] == ingredient


    def test_burger_remove_ingredient(self):
        ingredient1 = Ingredient("Lettuce", 0.5, "vegetable")
        ingredient2 = Ingredient("Tomato", 0.7, "vegetable")
        burger = Burger()
        burger.add_ingredient(ingredient1)
        burger.add_ingredient(ingredient2)
        burger.remove_ingredient(0)
        assert len(burger.ingredients) == 1
        assert burger.ingredients[0] == ingredient2


    def test_burger_move_ingredient(self):
        ingredient1 = Ingredient("Lettuce", 0.5, "vegetable")
        ingredient2 = Ingredient("Tomato", 0.7, "vegetable")
        burger = Burger()
        burger.add_ingredient(ingredient1)
        burger.add_ingredient(ingredient2)
        burger.move_ingredient(0, 1)
        assert burger.ingredients[0] == ingredient2
        assert burger.ingredients[1] == ingredient1


    @pytest.mark.parametrize(
        "bun_name, bun_price, ingredient1_name, ingredient1_price, ingredient2_name, ingredient2_price, expected_price",
        [
            ("Sesame", 1.5, "Lettuce", 0.5, "Tomato", 0.7, 4.2),
            ("Gluten Free", 1.0, "Avocado", 0.3, "Chicken", 0.4, 2.7),
            ("Whole Wheat", 2.0, "Cheese", 1.0, "Bacon", 0.7, 5.7)
        ])
    def test_burger_get_price(self, bun_name, bun_price, ingredient1_name, ingredient1_price, ingredient2_name,
                              ingredient2_price, expected_price):
        bun = Mock(spec=Bun)
        bun.get_name.return_value = bun_name
        bun.get_price.return_value = bun_price

        ingredient1 = Mock(spec=Ingredient)
        ingredient1.get_name.return_value = ingredient1_name
        ingredient1.get_price.return_value = ingredient1_price
        ingredient1.get_type.return_value = "vegetable"

        ingredient2 = Mock(spec=Ingredient)
        ingredient2.get_name.return_value = ingredient2_name
        ingredient2.get_price.return_value = ingredient2_price
        ingredient2.get_type.return_value = "vegetable"

        burger = Burger()
        burger.set_buns(bun)
        burger.add_ingredient(ingredient1)
        burger.add_ingredient(ingredient2)

        actual_price = burger.get_price()
        assert actual_price == pytest.approx(expected_price, rel=1e-2)


    @pytest.mark.parametrize(
        "bun_name, bun_price, ingredient1_name, ingredient1_price, ingredient1_type, ingredient2_name, ingredient2_price, ingredient2_type, expected_receipt",
        [
            ("Sesame", 1.5, "Lettuce", 0.5, "vegetable", "Tomato", 0.7, "vegetable",
             "(==== Sesame ====)\n= vegetable Lettuce =\n= vegetable Tomato =\n(==== Sesame ====)\n\nPrice: 4.2"),
            ("Whole Wheat", 2.0, "Cheese", 1.0, "dairy", "Bacon", 1.5, "meat",
             "(==== Whole Wheat ====)\n= dairy Cheese =\n= meat Bacon =\n(==== Whole Wheat ====)\n\nPrice: 6.5"),
            ("Gluten Free", 1.0, "Avocado", 0.3, "vegetable", "Chicken", 0.4, "meat",
             "(==== Gluten Free ====)\n= vegetable Avocado =\n= meat Chicken =\n(==== Gluten Free ====)\n\nPrice: 2.7")
        ])
    def test_burger_get_receipt(self, bun_name, bun_price, ingredient1_name, ingredient1_price, ingredient1_type,
                                ingredient2_name, ingredient2_price, ingredient2_type, expected_receipt):
        bun = Mock(spec=Bun)
        bun.get_name.return_value = bun_name
        bun.get_price.return_value = bun_price

        ingredient1 = Mock(spec=Ingredient)
        ingredient1.get_name.return_value = ingredient1_name
        ingredient1.get_price.return_value = ingredient1_price
        ingredient1.get_type.return_value = ingredient1_type

        ingredient2 = Mock(spec=Ingredient)
        ingredient2.get_name.return_value = ingredient2_name
        ingredient2.get_price.return_value = ingredient2_price
        ingredient2.get_type.return_value = ingredient2_type

        burger = Burger()
        burger.set_buns(bun)
        burger.add_ingredient(ingredient1)
        burger.add_ingredient(ingredient2)

        receipt = burger.get_receipt()
        actual_price = burger.get_price()
        assert actual_price == pytest.approx(float(expected_receipt.split("Price: ")[-1]), rel=1e-2)

