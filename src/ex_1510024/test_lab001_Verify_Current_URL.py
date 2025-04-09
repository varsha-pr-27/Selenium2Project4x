import time

import allure
from selenium import webdriver


@allure.title("Verify the URL of the webpage SDET Club")
def test_sample_login():
    driver = webdriver.Chrome()
    driver.get("https://sdet.live")

    driver = webdriver.Edge()
    driver.get("https://google.com")
    assert driver.current_url == "https://www.google.com/"

    time.sleep(5)
    driver.quit()
