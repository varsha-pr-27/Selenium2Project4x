# Automation for the Registration Page of the AwesomeQA.com / UI

import time

from selenium import webdriver
from selenium.webdriver.common.by import By


def test_with_registration():
    driver = webdriver.Chrome()
    driver.get("https://awesomeqa.com/ui/index.php?route=account/register")

    first_name = driver.find_element(By.ID, "input-firstname")
    first_name.send_keys("Varsha")

    last_name = driver.find_element(By.ID, "input-lastname")
    last_name.send_keys("P R ")

    user_email = driver.find_element(By.ID, "input-email")
    user_email.send_keys("panathalevarsha@gmail.com")

    user_telephone = driver.find_element(By.ID, "input-telephone")
    user_telephone.send_keys("912345678")

    user_password = driver.find_element(By.ID, "input-password")
    user_password.send_keys("admin@12345")

    user_password_confirm = driver.find_element(By.ID, "input-confirm")
    user_password_confirm.send_keys("admin@12345")

    # here user will check the agree check box
    driver.find_element(By.XPATH, "//input[@name ='agree']").click()

    # here user will click on Continue button
    driver.find_element(By.XPATH, "//input[@class ='btn btn-primary']").click()

    time.sleep(5)
    page_source_data = driver.page_source
    assert "Your Account Has Been Created!" in page_source_data
    print(page_source_data)

    time.sleep(10)
    driver.quit()
