from praktikum.bun import Bun

class TestBun:

    # Тест на успешное создание новой булки с заданным названием
    def test_new_bun_name_bun(self):
        bun = Bun("Булка смерти", 405)
        assert bun.get_name() == "Булка смерти"


    # Тест на успешное создание новой булки с заданной стоимостью
    def test_new_bun_price(self):
        bun = Bun("Булка смерти", 405)
        assert bun.get_price() == 405