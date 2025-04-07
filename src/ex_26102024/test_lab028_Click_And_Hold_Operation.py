import time

import allure
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By


@allure.title("Actions P3")
@allure.description("Verify Click and hold operation")
def test_verify_action_keyboard():
    driver = webdriver.Chrome()
    driver.get("https://awesomeqa.com/selenium/mouse_interaction.html")

    element_to_hold = driver.find_element(By.ID, "draggable")

    actions = ActionChains(driver=driver)
    actions.click_and_hold(on_element=element_to_hold)
    actions.perform()

    time.sleep(5)
    driver.quit()
