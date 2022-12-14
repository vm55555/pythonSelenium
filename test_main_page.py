from .pages.main_page import MainPage
from .pages.login_page import LoginPage

link1 = 'https://selenium1py.pythonanywhere.com/ru/'


# class TestMainPage:

#    def setup(self):

# @pytest.mark.open_page
# @pytest.mark.smoke
def test_guest_can_go_to_catalogue(browser):
    page = MainPage(browser, link1)
    page.open_page()
    page.should_be_view_products()
    page.go_to_catalogue()


def test_guest_can_go_to_login_page(browser):
    page = LoginPage(browser, link1)
    page.open_page()
    page.go_to_login_page()
    page.should_be_login_page()


def test_register_user(browser):
    page = LoginPage(browser, link1)
    page.open_page()
    page.go_to_login_page()
    page.should_be_login_page()
    page.register_user('viktorii1iia@gmail.com', 'qazwsxedc123#$')

    # @pytest.mark.view_products

#
# def test_2(browser):
#     browser.get(link)
#
#     assert browser.find_element(By.XPATH, "//h1[.='Все товары']").text == 'Все товары', 'assertion error'

# @pytest.mark.xfail
# def test_3(self, browser):
#     browser.get(link)
#     browser.find_element(By.XPATH, "//a[.='Все товары']").click()
#     assert browser.find_element(By.XPATH, "//h1[.='Все товары']").text == 'Все товары', 'assertion error'

# def teardown(self):
#     self.driver.quit()
