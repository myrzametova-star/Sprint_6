from selenium.webdriver.common.by import By

class MainPageLocators:
    TOP_ORDER_BUTTON = (By.XPATH, ".//button[text()='Заказать']")
    BOTTOM_ORDER_BUTTON = (By.XPATH, ".//div[contains(@class, 'Home_FinishButton')]/button")
    COOKIE_ACCEPT_BUTTON = (By.ID, "rcc-confirm-button")

    # Новые стабильные XPATH локаторы для элементов аккордеона
    @staticmethod
    def get_question_locator(index):
        """Возвращает локатор кнопки вопроса по его индексу на странице"""
        # Индексы в XPATH начинаются с 1, поэтому делаем index + 1
        return (By.XPATH, f"(//div[@class='accordion__item'])[{index + 1}]//div[@role='button']")

    @staticmethod
    def get_answer_locator(index):
        """Возвращает локатор текстовой панели ответа по его индексу"""
        return (By.XPATH, f"(//div[@class='accordion__item'])[{index + 1}]//div[@class='accordion__panel']//p")



