import time

import allure
from selenium import webdriver


@allure.title("Window Scroll")
@allure.description("Verify Window Scroll")
def test_verify_window_scroll():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--incognito")

    driver = webdriver.Chrome(chrome_options)
    driver.get("https://selectorshub.com/xpath-practice-page/")
    driver.maximize_window()

    title = driver.execute_script("return document.title")
    print(title)

    current_url = driver.execute_script("return document.URL")
    print(current_url)

    time.sleep(5)
    driver.quit()
