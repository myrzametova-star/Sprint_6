import pytest
from selenium import webdriver

@pytest.fixture
def driver():
    # Запуск браузера Mozilla Firefox по ТЗ
    driver = webdriver.Firefox()
    driver.maximize_window()
    yield driver
    driver.quit()