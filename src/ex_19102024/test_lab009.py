# Automation script to locate the webelements using ID, Name and ClassName of APP.VWO webpage

import time

import allure
from selenium import webdriver
from selenium.webdriver.common.by import By


@allure.description("Verify the error message when entering the login credentials")
def test_chrome_negative_test_case_verification():
    driver = webdriver.Chrome()
    driver.get("https://app.vwo.com")  # Navigate to the url

    login_id_web_element = driver.find_element(By.ID, "login-username")
    login_id_web_element.send_keys("abc@gmail.com")

    password_id_web_element = driver.find_element(By.NAME, "password")
    password_id_web_element.send_keys("password@1234")

    submit_btn_web_element = driver.find_element(By.ID, "js-login-btn")
    submit_btn_web_element.click()

    time.sleep(3)

    error_message_web_element = driver.find_element(By.ID, "js-notification-box-msg")
    assert error_message_web_element.text == "Your email, password, IP address or location did not match"
    time.sleep(10)
    driver.quit()
