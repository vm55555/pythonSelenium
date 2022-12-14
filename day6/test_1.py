import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://www.saucedemo.com/")


def test_title():
    assert driver.title == "Swag Labs"


def test_login_form():
    driver.find_element(By.ID, 'user-name').send_keys('standard_user')
    driver.find_element(By.ID, 'password').send_keys('secret_sauce')
    driver.find_element(By.ID, 'login-button').click()

    assert driver.current_url == 'https://www.saucedemo.com/inventory.html'

    driver.quit()

