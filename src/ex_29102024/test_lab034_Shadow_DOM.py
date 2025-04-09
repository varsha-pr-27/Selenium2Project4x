import time

import allure
from selenium import webdriver
from selenium.webdriver.common.by import By


@allure.title("test_shadow_dom_js")
@allure.description("Verify test_shadow_dom_js")
def test_shadow_dom_js():
    # ChromeOptions - --incognito
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--incognito")

    driver = webdriver.Chrome(chrome_options)
    driver.get("https://selectorshub.com/xpath-practice-page/")
    driver.maximize_window()

    # Scroll into the view where div is present
    username_div = driver.find_element(By.ID, "userName")
    driver.execute_script("arguments[0].scrollIntoView(true);", username_div)

    input_box = driver.execute_script(
        "return document.querySelector('div#userName').shadowRoot.querySelector('#app2').shadowRoot.querySelector('#pizza');")
    input_box.send_keys("farmhouse")

    time.sleep(5)
    driver.quit()
