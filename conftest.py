import pytest
import datetime
from selenium import webdriver
from webdrivermanager import ChromeDriverManager, GeckoDriverManager, EdgeDriverManager


@pytest.fixture(scope="session")
def driver(browser='chrome'):
    if browser == 'chrome':
        driver_manager = ChromeDriverManager()
        driver_manager.download_and_install()
        driver = webdriver.Chrome()
    elif browser == 'firefox':
        driver_manager = GeckoDriverManager()
        driver_manager.download_and_install()
        driver = webdriver.Firefox()
    elif browser == 'edge':
        driver_manager = EdgeDriverManager()
        driver_manager.download_and_install()
        driver = webdriver.Edge()
    else:
        raise ValueError(f'Unsupported browser: {browser}')
    driver.get('https://rahulshettyacademy.com/loginpagePractise/')
    yield driver
    driver.quit()


def pytest_configure(config):
    now = datetime.datetime.now()
    timestamp = now.strftime('%Y-%m-%d_%H-%M-%S')
    html_report = f'reports/report_{timestamp}.html'
    config.option.htmlpath = html_report
