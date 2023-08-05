from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def click(self, by, locator):
        element = self.wait.until(EC.element_to_be_clickable((by, locator)))
        element.click()

    def send_keys(self, by, locator, keys):
        element = self.wait.until(EC.visibility_of_element_located((by, locator)))
        element.send_keys(keys)