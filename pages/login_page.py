import time

from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):

    def should_be_login_page(self):
        self.should_be_login_link()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_link(self):
        print(self.browser.current_url)
        assert self.browser.current_url.endswith('login/'), print(self.browser.current_url)

    def should_be_login_form(self):
        assert self.element_is_present(*LoginPageLocators.LOGIN_FORM)

    def should_be_register_form(self):
        assert self.element_is_present(*LoginPageLocators.REGISTER_FORM)

    def go_to_login_page(self):
        self.browser.find_element(*LoginPageLocators.LOGIN_LINK).click()

    def register_user(self, email='email', password='password'):
        self.browser.find_element(*LoginPageLocators.ID_REGISTRATION_EMAIL).send_keys(email)
        self.browser.find_element(*LoginPageLocators.ID_REGISTRATION_PASSWORD1).send_keys(password)
        self.browser.find_element(*LoginPageLocators.ID_REGISTRATION_PASSWORD2).send_keys(password)
        self.browser.find_element(*LoginPageLocators.REGISTRATION_SUBMIT_BTN).click()
        time.sleep(5)
        assert 'Спасибо за регистрацию!' in self.browser.find_element(*LoginPageLocators.REGISTER_MSG).text
