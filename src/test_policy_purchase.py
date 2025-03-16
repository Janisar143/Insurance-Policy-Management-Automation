from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


def test_policy_purchase():
    driver = webdriver.Chrome()
    driver.get("https://www.icicilombard.com/")

    # Login
    driver.find_element(By.ID, "loginEmail").send_keys("Janisar00")
    driver.find_element(By.ID, "Password").send_keys("Janisar@00", Keys.RETURN)

    # Nevigate to policy purchase
    driver.find_element(By.LINK_TEXT, "Buy Policy").click()

    # Fill Policy Details
    driver.find_element(By.ID, "policy_type").send_keys("Vehicle Insurance")
    driver.find_element(By.ID, "vehicle_number").send_keys("KA01AB1234")
    driver.find_element(By.ID, "purchase").click()

    # Assert Success Message
    success_message = driver.find_element(By.ID, "success").text
    assert "Policy Purchase Successfully" in success_message

    driver.quit()
