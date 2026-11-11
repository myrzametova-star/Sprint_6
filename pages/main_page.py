from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators
from data import BASE_URL 

class MainPage(BasePage):
    
    def open(self):
        """Открыть главную страницу"""
        self.open_url(BASE_URL)

    def open_main_page(self):
        self.open()

    def accept_cookies(self):
        """Принять куки, если кнопка появится, иначе просто продолжить тест"""
        try:
            self.click_element(MainPageLocators.COOKIE_ACCEPT_BUTTON, timeout=3)
        except Exception:
            pass

    def click_top_order_button(self):
        """Кликнуть по верхней кнопке 'Заказать'"""
        self.click_element(MainPageLocators.TOP_ORDER_BUTTON)

    def click_bottom_order_button(self):
        """Кликнуть по нижней кнопке 'Заказать'"""
        element = self.find_element(MainPageLocators.BOTTOM_ORDER_BUTTON)
        self.driver.execute_script("arguments.scrollIntoView();", element)
        self.click_element(MainPageLocators.BOTTOM_ORDER_BUTTON)

    def get_answer_text(self, index):
        """Скроллит к вопросу, кликает по нему и возвращает текст ответа"""
        question_locator = MainPageLocators.get_question_locator(index)
        answer_locator = MainPageLocators.get_answer_locator(index)

        question_element = self.find_element(question_locator)
        self.driver.execute_script("arguments.scrollIntoView();", question_element)

        self.click_element(question_locator)

        answer_element = self.find_element(answer_locator)
        return answer_element.text
