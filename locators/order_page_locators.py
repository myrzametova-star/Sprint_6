from selenium.webdriver.common.by import By

class OrderPageLocators:
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
