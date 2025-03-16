import pytest

from pages.policy_page import PolicyPage


@pytest.mark.usefixtures("setup")
class TestPolicyCreation:
    def test_create_policy(self, setup):
        driver = setup
        policy_page = PolicyPage(driver)
        success_message = policy_page.create_policy("Health Insurance")
        assert "Policy created successfully" in success_message
