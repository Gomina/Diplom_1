from data import TD
from praktikum.bun import Bun

class TestBun:

    # Тест на успешное создание новой булки с заданным названием
    def test_new_bun_name_bun(self):
        bun = Bun(TD.BUN_NAME, TD.BUN_PRICE)
        assert bun.get_name() == TD.BUN_NAME


    # Тест на успешное создание новой булки с заданной стоимостью
    def test_new_bun_price(self):
        bun = Bun(TD.BUN_NAME, TD.BUN_PRICE)
        assert bun.get_price() == TD.BUN_PRICE