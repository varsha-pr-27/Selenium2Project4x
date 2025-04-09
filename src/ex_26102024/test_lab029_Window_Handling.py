import time

import allure
from selenium import webdriver
from selenium.webdriver.common.by import By


@allure.title("Actions P3")
@allure.description("Verify Click and Hold")
def test_verify_window_handling():
    # ChromeOptions - --incognito
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--incognito")

    driver = webdriver.Chrome(chrome_options)
    driver.get("https://the-internet.herokuapp.com/windows")
    driver.maximize_window()

    parent_window = driver.current_window_handle  # 1
    print(parent_window)

    link = driver.find_element(By.LINK_TEXT, "Click Here")
    link.click()

    child_window = driver.window_handles  # 2
    print(child_window)

    for handle in child_window:
        driver.switch_to.window(handle)
        if "New Window" in driver.page_source:
            print("Testcase Passed")
            break

    time.sleep(5)
    driver.quit()
