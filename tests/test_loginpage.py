import pytest
from pages.login_page import LoginPage


@pytest.mark.login
def test_login(driver):
    login_page = LoginPage(driver)
    login_page.enter_username('rahulshettyacademy')
    login_page.enter_password('learning')
    login_page.click_login()
