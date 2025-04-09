import time

import allure
from selenium import webdriver


@allure.title(" JS ")
@allure.description("Verify JS ")
def test_verify_js():
    # ChromeOptions - --incognito
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--incognito")

    driver = webdriver.Chrome(chrome_options)
    driver.get("https://app.vwo.com")
    driver.maximize_window()

    driver.execute_script("alert(1)")

    time.sleep(5)
    driver.quit()
