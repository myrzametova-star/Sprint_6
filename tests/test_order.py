import pytest
import allure
from pages.main_page import MainPage
from pages.order_page import OrderPage

class TestOrderFlow:

    @allure.title("Заказ самоката через верхнюю кнопку 'Заказать' в хедере")
    @allure.description("Проверяем весь флоу оформления заказа, начиная с нажатия на кнопку вверху страницы")
    @pytest.mark.parametrize(
        "name, surname, address, metro_station, phone, date, duration, comment",
        [
            ("Иван", "Петров", "ул. Ленина, д. 10", "Черкизовская", "79991112233", "12.05.2027", "сутки", "Позвонить за час")
        ]
    )
    def test_scooter_order_via_top_button(self, driver, name, surname, address, metro_station, phone, date, duration, comment):
        main_page = MainPage(driver)
        order_page = OrderPage(driver)

        main_page.open()
        main_page.accept_cookies()
        main_page.click_top_order_button()

        order_page.fill_client_info(name, surname, address, metro_station, phone)
        order_page.fill_rent_info(date, duration, comment)

        success_text = order_page.get_success_modal_text()
        assert "Заказ оформлен" in success_text, f"Окно успешного заказа не появилось. Фактический текст: {success_text}"


    @allure.title("Заказ самоката через нижнюю кнопку 'Заказать'")
    @allure.description("Проверяем весь флоу оформления заказа, начиная со скролла и нажатия на кнопку внизу страницы")
    @pytest.mark.parametrize(
        "name, surname, address, metro_station, phone, date, duration, comment",
        [
            ("Анна", "Смирнова", "проспект Мира, д. 25, кв. 4", "Сокольники", "89995556677", "15.06.2027", "двое суток", "")
        ]
    )
    def test_scooter_order_via_bottom_button(self, driver, name, surname, address, metro_station, phone, date, duration, comment):
        main_page = MainPage(driver)
        order_page = OrderPage(driver)

        main_page.open()
        main_page.accept_cookies()
        main_page.click_bottom_order_button()

        order_page.fill_client_info(name, surname, address, metro_station, phone)
        order_page.fill_rent_info(date, duration, comment)

        # Добавили недостающий assert для второго теста
        success_text = order_page.get_success_modal_text()
        assert "Заказ оформлен" in success_text, f"Окно успешного заказа не появилось. Фактический текст: {success_text}"
