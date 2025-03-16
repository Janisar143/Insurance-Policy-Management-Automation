from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class BasePage:
    def __init__(self, driver):
        self.driver = driver

        def click(self, locator):
            WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(locator)).click()

        def send_keys(self, locator, text):
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator)).send_keys(text)
