import time

import allure
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By


@allure.title("Actions P3")
@allure.description("Verify Drag and Drop operation")
def test_verify_action_keyboard():
    driver = webdriver.Chrome()
    driver.get("https://awesomeqa.com/selenium/mouse_interaction.html")

    element_to_drag = driver.find_element(By.ID, "draggable")
    element_to_drop = driver.find_element(By.ID, "droppable")

    actions = ActionChains(driver)
    actions.drag_and_drop(element_to_drag, element_to_drop)
    actions.perform()

    time.sleep(5)
    driver.quit()
