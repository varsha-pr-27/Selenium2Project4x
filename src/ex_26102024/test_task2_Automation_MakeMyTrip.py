# Automation of  Make My Trip Website

import time

import allure
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


@allure.title("Actions P3")
@allure.description("Verify Click and Hold")
def test_verify_action_make_my_trip():
    # ChromeOptions - --incognito
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--incognito")

    driver = webdriver.Chrome(chrome_options)
    driver.get("https://www.makemytrip.com/")
    driver.maximize_window()

    # //span[@data-cy="closeModal"] wait -> click
    WebDriverWait(driver=driver, timeout=5).until(
        EC.visibility_of_element_located((By.XPATH, "//span[@data-cy='closeModal']"))
    )

    driver.find_element(By.XPATH, "//span[@data-cy='closeModal']").click()

    time.sleep(2)

    fromCity = driver.find_element(By.ID, "fromCity")
    # fromCity = driver.find_element(By.XPATH, "//input[@id='fromCity']")

    # move the mouse to fromCity - Input Box
    # click on it
    # DEL enter
    # Arrow - first ( up and down)
    # Enter

    actions = ActionChains(driver)
    (actions.
     move_to_element(fromCity)
     .click().send_keys_to_element(fromCity, "del")
     .perform())

    time.sleep(2)

    (actions.move_to_element(fromCity)
     .key_down(Keys.ARROW_DOWN)
     .key_down(Keys.ENTER).perform())

    time.sleep(10)
    driver.quit()
