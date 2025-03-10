# Automation script to find all the buttons of APP.VWO webpage using the TAG_NAME

import time

import allure
from selenium import webdriver
from selenium.webdriver.common.by import By


@allure.title("Find all the buttons by TagName")
@allure.description("Verify that FREE Trail button is clicked, Navigated to next page")
def test_4():
    driver = webdriver.Chrome()
    driver.get("https://app.vwo.com/#/login")

    # tag Name
    buttons = driver.find_elements(By.TAG_NAME, "button")
    print(len(buttons))
    for i in buttons:
        print(i.text)

    time.sleep(5)
    driver.quit()
