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

    driver.execute_script("window.scrollBy(0,500);")

    time.sleep(5)
    driver.quit()
    