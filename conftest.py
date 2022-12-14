import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(scope='class')
def browser():
    print('\n start browser...')
    browser = webdriver.Chrome(ChromeDriverManager().install())
    yield browser
    print('\n quit browser...')
    browser.quit()