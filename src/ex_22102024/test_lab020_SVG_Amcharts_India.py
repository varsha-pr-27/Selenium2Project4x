import time

import allure
from selenium import webdriver
from selenium.webdriver.common.by import By


@allure.title("SVG")
@allure.description("Verify svg")
def test_verify_svg():
    driver = webdriver.Chrome()
    driver.get("https://www.amcharts.com/svg-maps/?map=india")

    # name() or local-name()

    # //*[name()='svg']/*[name()='g'][7]/*[name()='g']/*[name()='g']/*[name()='path']

    list_of_states = driver.find_elements(By.XPATH,
                                          "//*[name()='svg']"
                                          "/*[name()='g'][7]/*[name()='g']"
                                          "/*[name()='g']/*[name("
                                          ")='path']")
    for state in list_of_states:
        print(state.get_attribute("aria-label"))
        if "Tripura" in state.get_attribute("aria-label"):
            state.click()
            break

    time.sleep(5)
