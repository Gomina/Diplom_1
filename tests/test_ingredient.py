import pytest

from data import TD
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


class TestIngredient:

    @pytest.mark.parametrize("ingredient_type, name, price", [
    (INGREDIENT_TYPE_SAUCE, TD.SAUCE_NAME, TD.SAUCE_PRICE),  # ингредиент соус
    (INGREDIENT_TYPE_FILLING, TD.FILLING_NAME, TD.FILLING_PRICE)  # ингредиент начинка
        ])

    #Тест на успешное создание ингредиента
    # успешно создать новый ингредиент
    def test_new_ingredient(self, ingredient_type, name, price):
        ingredient = Ingredient(ingredient_type, name, price)
        assert ingredient.get_type() == ingredient_type
        assert ingredient.get_name() == name
        assert ingredient.get_price() ==  price