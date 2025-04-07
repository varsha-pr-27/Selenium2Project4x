import time

import allure
from selenium import webdriver
from selenium.webdriver.common.by import By


@allure.title("SVG")
@allure.description("Verify svg")
def test_svg():
    driver = webdriver.Chrome()
    driver.get("https://www.flipkart.com/")

    search_box = driver.find_element(By.NAME, "q")
    search_box.send_keys("macmini")

    list_svg_elements = driver.find_elements(By.XPATH, "//*[name()='svg']")
    list_svg_elements[0].click()

    time.sleep(5)
