import time

import allure
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


@pytest.mark.positive
@allure.title("Test sign up button")
@allure.description("Testing sign up button using LINK_TEXT option of find element")
def test_project3_sign_up_button_vwo_com():
    driver = webdriver.Chrome()
    driver.get("https://app.vwo.com/#/login")

    # LINK_TEXT= Exact match
    # sign_up_web_element= driver.find_element(By.LINK_TEXT, "Start a free trial")
    # sign_up_web_element.click()

    # PARTIAL_LINK_TEXT
    sign_up_web_element = driver.find_element(By.PARTIAL_LINK_TEXT, "free trial")
    sign_up_web_element.click()
    # verify that it navigates to next page of start free trial

    assert driver.current_url == "https://vwo.com/free-trial/?utm_medium=website&utm_source=login-page&utm_campaign=mof_eg_loginpage"

    time.sleep(5)
    driver.quit()
