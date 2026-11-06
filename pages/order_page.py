import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

class OrderPage:
    def __init__(self, driver):
        self.driver = driver

    # --- Первая страница формы: "Для кого самокат" ---
    NAME_INPUT = (By.XPATH, ".//input[@placeholder='* Имя']")
    SURNAME_INPUT = (By.XPATH, ".//input[@placeholder='* Фамилия']")
    ADDRESS_INPUT = (By.XPATH, ".//input[@placeholder='* Адрес: куда привезти заказ']")
    METRO_STATION_INPUT = (By.XPATH, ".//input[@placeholder='* Станция метро']")
    PHONE_INPUT = (By.XPATH, ".//input[@placeholder='* Телефон: на него позвонит курьер']")
    NEXT_BUTTON = (By.XPATH, ".//button[text()='Далее']")

    # --- Вторая страница формы: "Про аренду" ---
    DATE_INPUT = (By.XPATH, ".//input[@placeholder='* Когда привезти самокат']")
    RENT_DURATION_DROPDOWN = (By.XPATH, ".//div[@class='Dropdown-control']")
    COMMENT_INPUT = (By.XPATH, ".//input[@placeholder='Комментарий для курьера']")
    ORDER_BUTTON = (By.XPATH, ".//div[contains(@class, 'Order_Buttons')]/button[text()='Заказать']")
    
    CONFIRM_YES_BUTTON = (By.XPATH, ".//button[text()='Да']")
    ORDER_SUCCESS_MODAL = (By.XPATH, ".//div[contains(@class, 'Order_ModalHeader')]")

    def select_metro_station(self, station_name):
        self.driver.find_element(*self.METRO_STATION_INPUT).send_keys(station_name)
        station_locator = (By.XPATH, f".//div[text()='{station_name}']/parent::button")
        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(station_locator)).click()

    def select_rent_duration(self, duration_text):
        self.driver.find_element(*self.RENT_DURATION_DROPDOWN).click()
        duration_option = (By.XPATH, f".//div[@class='Dropdown-option' and text()='{duration_text}']")
        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(duration_option)).click()

    @allure.step("Заполнить первую форму 'Для кого самокат'")
    def fill_customer_info(self, name, surname, address, metro_station, phone):
        self.driver.find_element(*self.NAME_INPUT).send_keys(name)
        self.driver.find_element(*self.SURNAME_INPUT).send_keys(surname)
        self.driver.find_element(*self.ADDRESS_INPUT).send_keys(address)
        self.select_metro_station(metro_station)
        self.driver.find_element(*self.PHONE_INPUT).send_keys(phone)
        self.driver.find_element(*self.NEXT_BUTTON).click()

    @allure.step("Заполнить вторую форму 'Про аренду' и подтвердить заказ")
    def fill_rent_info(self, date, duration, comment=""):
        date_field = self.driver.find_element(*self.DATE_INPUT)
        date_field.send_keys(date)
        date_field.send_keys(Keys.ENTER)
        
        self.select_rent_duration(duration)
        if comment:
            self.driver.find_element(*self.COMMENT_INPUT).send_keys(comment)
            
        self.driver.find_element(*self.ORDER_BUTTON).click()
        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(self.CONFIRM_YES_BUTTON)).click()

    @allure.step("Получить текст успешного оформления заказа")
    def get_success_modal_text(self):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_to_be_clickable(self.ORDER_SUCCESS_MODAL))
        return self.driver.find_element(*self.ORDER_SUCCESS_MODAL).text