import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class MainPage:
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://praktikum-services.ru"

    TOP_ORDER_BUTTON = (By.XPATH, ".//button[text()='Заказать']")
    BOTTOM_ORDER_BUTTON = (By.XPATH, ".//div[contains(@class, 'Home_FinishButton')]/button")
    COOKIE_ACCEPT_BUTTON = (By.ID, "rcc-confirm-button")

    def get_question_locator(self, index):
        return (By.ID, f"accordion__heading-{index}")

    def get_answer_locator(self, index):
        return (By.ID, f"accordion__panel-{index}")

    @allure.step("Открыть главную страницу Самоката")
    def open(self):
        self.driver.get(self.url)

    @allure.step("Принять куки, если окно появилось")
    def accept_cookies(self):
        try:
            WebDriverWait(self.driver, 3).until(EC.element_to_be_clickable(self.COOKIE_ACCEPT_BUTTON)).click()
        except:
            pass

    @allure.step("Кликнуть на вопрос номер {index}")
    def click_question(self, index):
        question_locator = self.get_question_locator(index)
        element = self.driver.find_element(*question_locator)
        self.driver.execute_script("arguments.scrollIntoView();", element)
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(question_locator)).click()

    @allure.step("Получить текст ответа номер {index}")
    def get_answer_text(self, index):
        answer_locator = self.get_answer_locator(index)
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_to_be_clickable(answer_locator))
        return self.driver.find_element(*answer_locator).text