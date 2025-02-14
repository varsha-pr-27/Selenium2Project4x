# Create a Selenium Script to verify the title for
# Open the Page - https://katalon-demo-cura.herokuapp.com/
# Verify the current URL, current title
# In the page source add a assertion that “CURA Healthcare Service” exist in the page.
# driver.pageSource() - String
import time

import allure
from selenium import webdriver


@allure.title("Verification of page source text 'CURA Healthcare Service'")
def test_cura_healthcare_login():
    driver = webdriver.Chrome()
    driver.get("https://katalon-demo-cura.herokuapp.com/")
    assert driver.current_url == "https://katalon-demo-cura.herokuapp.com/"
    assert driver.title == "CURA Healthcare Service"
    print(driver.current_url)
    print(driver.title)
    page_source_data = driver.page_source
    assert "CURA Healthcare Service" in page_source_data

    time.sleep(10)
    driver.quit()
