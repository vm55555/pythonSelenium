from selenium.webdriver.common.by import By


class MainPageLocators:
    CATALOGUE_LINK = (By.XPATH, "//a[.='Все товары']")


class LoginPageLocators:
    LOGIN_FORM = (By.ID, 'login_form')
    REGISTER_FORM = (By.ID, 'register_form')
    LOGIN_LINK = (By.ID, 'login_link')
    ID_REGISTRATION_EMAIL = (By.ID, 'id_registration-email')
    ID_REGISTRATION_PASSWORD1 = (By.ID, 'id_registration-password1')
    ID_REGISTRATION_PASSWORD2 = (By.ID, 'id_registration-password2')
    REGISTRATION_SUBMIT_BTN = (By.XPATH, '//button[@name="registration_submit"]')
    REGISTER_MSG = (By.CSS_SELECTOR, 'div[class="alertinner wicon"]')
