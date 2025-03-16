from selenium.webdriver.common.by import By

from .base_page import BasePage


class PolicyPage(BasePage):
    POLICY_NAME = (By.ID, "policy_name")
    CREATE_BUTTON = (By.ID, "create_policy")
    SUCCESS_MESSAGE = (By.ID, "success_message")

    def create_policy(self, policy_name):
        self.send_keys(self.POLICY_NAME, policy_name)
        self.click(self.CREATE_BUTTON)
        return self.get_text(self.SUCCESS_MESSAGE)
