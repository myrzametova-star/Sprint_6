import pytest
import allure
from pages.main_page import MainPage
from data import ACCORDION_ANSWERS

class TestAccordion:

    @allure.title("Проверка выпадающего списка 'Вопросы о важном'")
    @allure.description("Проверяем, что при клике на стрелочку открывается соответствующий текст ответа")
    @pytest.mark.parametrize(
        "index, expected_text",
        enumerate(ACCORDION_ANSWERS)
    )
    def test_accordion_questions_and_answers(self, driver, index, expected_text):
        main_page = MainPage(driver)
      
        main_page.open()
        main_page.accept_cookies()
        
        actual_text = main_page.get_answer_text(index)
 
        assert actual_text == expected_text, f"Текст ответа для элемента {index} не совпадает!"
        