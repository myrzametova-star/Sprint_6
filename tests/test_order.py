import pytest
import allure
from pages.main_page import MainPage
from pages.order_page import OrderPage

class TestOrderFlow:

    @allure.title("Позитивный сценарий заказа самоката")
    @allure.description("Проверка оформления заказа через разные кнопки входа с разными наборами данных")
    @pytest.mark.parametrize(
        "button_type, name, surname, address, metro_station, phone, date, duration, comment",
        [
            ("top", "Иван", "Петров", "ул. Ленина, д. 10", "Черкизовская", "79991112233", "12.05.2027", "сутки", "Позвонить за час"),
            ("bottom", "Анна", "Смирнова", "проспект Мира, д. 25, кв. 4", "Сокольники", "89995556677", "15.06.2027", "двое суток", "")
        ]
    )
    def test_scooter_order_flow(self, driver, button_type, name, surname, address, metro_station, phone, date, duration, comment):
        main_page = MainPage(driver)
        order_page = OrderPage(driver)

      
        main_page.open()
        main_page.accept_cookies()

      
        if button_type == "top":
            driver.find_element(*main_page.TOP_ORDER_BUTTON).click()
        else:
            bottom_btn = driver.find_element(*main_page.BOTTOM_ORDER_BUTTON)
            driver.execute_script("arguments.scrollIntoView();", bottom_btn)
            bottom_btn.click()

        order_page.fill_rent_info(date, duration, comment)

        success_text = order_page.get_success_modal_text()
        assert "Заказ оформлен" in success_text, f"Окно успешного заказа не появилось. Фактический текст: {success_text}"
        