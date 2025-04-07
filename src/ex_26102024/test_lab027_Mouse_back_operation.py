import time

import allure
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionBuilder
from selenium.webdriver.common.actions.mouse_button import MouseButton
from selenium.webdriver.common.by import By


@allure.title("Actions P2")
@allure.description("Verify MouseBack")
def test_verify_action_keyboard():
    driver = webdriver.Chrome()
    driver.get("https://awesomeqa.com/selenium/mouse_interaction.html")

    atag = driver.find_element(By.ID, "click")
    atag.click()

    # click - Normal Driver, will find the element and click on it. release it.

    time.sleep(2)

    # MOUSE_BACK_OPERATION
    actions_builders = ActionBuilder(driver=driver)
    actions_builders.pointer_action.pointer_up(MouseButton.BACK)
    actions_builders.perform()

    time.sleep(10)
    driver.quit()
