import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from pages.base_page import BasePage
from locators.order_page_locators import OrderPageLocators

class OrderPage(BasePage):  # Класс с большой буквы, наследуется от BasePage

    def select_metro_station(self, station_name):
        self.fill_field(OrderPageLocators.METRO_STATION_INPUT, station_name)
        station_locator = (By.XPATH, f".//div[text()='{station_name}']/parent::button")
        self.click_element(station_locator, timeout=5)

    def select_rent_duration(self, duration_text):
        self.click_element(OrderPageLocators.RENT_DURATION_DROPDOWN)
        duration_option = (By.XPATH, f".//div[@class='Dropdown-option' and text()='{duration_text}']")
        self.click_element(duration_option, timeout=5)

    @allure.step("Заполнить первую форму 'Для кого самокат'")
    def fill_customer_info(self, name, surname, address, metro_station, phone):
        self.fill_field(OrderPageLocators.NAME_INPUT, name)
        self.fill_field(OrderPageLocators.SURNAME_INPUT, surname)
        self.fill_field(OrderPageLocators.ADDRESS_INPUT, address)
        self.select_metro_station(metro_station)
        self.fill_field(OrderPageLocators.PHONE_INPUT, phone)
        self.click_element(OrderPageLocators.NEXT_BUTTON)

    def fill_client_info(self, name, surname, address, metro_station, phone):
        self.fill_customer_info(name, surname, address, metro_station, phone)

    @allure.step("Заполнить вторую форму 'Про аренду' и подтвердить заказ")
    def fill_rent_info(self, date, duration, comment=""):
        date_field = self.find_element(OrderPageLocators.DATE_INPUT)
        date_field.send_keys(date)
        date_field.send_keys(Keys.ENTER)
        
        self.select_rent_duration(duration)
        if comment:
            self.fill_field(OrderPageLocators.COMMENT_INPUT, comment)
            
        self.click_element(OrderPageLocators.ORDER_BUTTON)
        self.click_element(OrderPageLocators.CONFIRM_YES_BUTTON, timeout=5)

    @allure.step("Получить текст успешного оформления заказа")
    def get_success_modal_text(self):
        element = self.find_element(OrderPageLocators.ORDER_SUCCESS_MODAL)
        return element.text

