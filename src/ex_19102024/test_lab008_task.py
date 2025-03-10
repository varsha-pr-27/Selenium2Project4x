import time

from selenium import webdriver
from selenium.webdriver.common.by import By


def test_katalon_login_verification_project1():
    driver = webdriver.Chrome()
    driver.get("https://katalon-demo-cura.herokuapp.com/")

    make_appointment_element = driver.find_element(By.ID, "btn-make-appointment")
    make_appointment_element.click()

    Username = driver.find_element(By.ID, "txt-username")
    Username.send_keys("John Doe")

    Password = driver.find_element(By.ID, "txt-password")
    Password.send_keys("ThisIsNotAPassword")

    Login = driver.find_element(By.ID, "btn-login")
    Login.click()

    # 4.Verify that url changes
    assert driver.current_url == "https://katalon-demo-cura.herokuapp.com/#appointment"

    time.sleep(5)
    driver.quit()
