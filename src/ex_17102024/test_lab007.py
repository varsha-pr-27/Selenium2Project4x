# Find the element using the Locators

import time

from selenium import webdriver
from selenium.webdriver.common.by import By


def test_chrome_current_url_verification():
    driver = webdriver.Chrome()
    driver.get("https://katalon-demo-cura.herokuapp.com/")

    # 1 Find the element with the anchor tag
    # <a > id="btn-make-appointment"
    # href="./profile.php#login"
    # class="btn btn-dark btn-lg">
    # Make Appointment</a>

    # 2 Find the unique element
    make_appointment_element = driver.find_element(By.ID, "btn-make-appointment")

    # 3 Click on the element
    make_appointment_element.click()

    # 4 Verify the url changes
    assert driver.current_url == "https://katalon-demo-cura.herokuapp.com/profile.php#login"
    time.sleep(10)
    driver.quit()
